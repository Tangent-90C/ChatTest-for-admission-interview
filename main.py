from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent
from dotenv import load_dotenv
import os

# 自行把 QWEN_API 写入 .env 文件中
load_dotenv()

model = ModelFactory.create(
  model_platform=ModelPlatformType.QWEN,
  model_type=ModelType.QWEN_PLUS,
  api_key=os.getenv('QWEN_API'),
)

agent = ChatAgent(model=model)

response_1 = agent.step("出一个计算机网络的题目")
print(response_1.msgs[0].content)
# The GitHub link to the CAMEL framework is
# [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel).