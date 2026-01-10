import pandas as pd
import os
import subprocess
from urllib.parse import urlparse

def download_repos():
    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(base_dir, 'data_sources.xlsx')
    datas_dir = os.path.join(base_dir, 'datas')

    # Ensure datas directory exists
    if not os.path.exists(datas_dir):
        os.makedirs(datas_dir)
        print(f"Created directory: {datas_dir}")

    # Read Excel file
    try:
        df = pd.read_excel(excel_path)
    except Exception as e:
        print(f"Error reading {excel_path}: {e}")
        return

    # Check if '数据源' column exists
    if '数据源' not in df.columns:
        print("Column '数据源' not found in the Excel file.")
        return

    # Iterate over links
    for link in df['数据源']:
        if not isinstance(link, str) or not link.strip():
            continue
        
        link = link.strip()
        
        # Simple validation
        if not link.startswith('http'):
            print(f"Skipping invalid link: {link}")
            continue

        # Extract repo name from URL to use as folder name
        # e.g., https://github.com/user/repo -> repo
        path = urlparse(link).path
        repo_name = os.path.basename(path)
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        
        if not repo_name:
            print(f"Could not determine repo name from {link}")
            continue

        target_dir = os.path.join(datas_dir, repo_name)

        if os.path.exists(target_dir):
            print(f"Directory {target_dir} already exists. Skipping {link}")
            continue

        print(f"Cloning {link} into {target_dir}...")
        try:
            subprocess.run(['git', 'clone', link, target_dir], check=True)
            print(f"Successfully cloned {link}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone {link}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while cloning {link}: {e}")

if __name__ == "__main__":
    download_repos()
