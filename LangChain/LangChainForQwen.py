from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
"""
   通过LangChain框架 来问千问模型问题-样例代码1
"""
# 初始化通义千问模型
model = ChatOpenAI(
    model="qwen-max",  # 可替换为 qwen-turbo, qwen-max 等
    openai_api_key="sk-2db88a2dc4564fcdbf47bc2f1b3e6355",
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=0.7
)

# 构造角色化对话消息
messages = [
    SystemMessage(content="你是一个情感专家"),
    HumanMessage(content="异性之间如何才能相处的融洽")
]

# 调用并输出结果
response = model.invoke(messages)
print(response.content)