from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
"""
   通过LangChain框架 来问千问模型问题-样例代码2
   这样做的好处是将提示词的结构与模型调用分离
    代码被清晰地分为了三个部分：模型初始化、提示词模板构建、以及调用执行
"""
# 1. 初始化通义千问模型
model = ChatOpenAI(
    model="qwen-max",
    openai_api_key="sk-2db88a2dc4564fcdbf47bc2f1b3e6355",
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=0.7
)

# 2. 创建提示词模板
# 定义系统消息模板，固定角色设定
system_template = "你是一个情感专家"
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

# 定义人类消息模板，使用 {question} 作为占位符
human_template = "{question}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 将两者组合成一个完整的聊天提示词模板
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# 3. 使用模板生成消息并调用模型
# 传入具体的变量值来填充模板
input_question = "异性之间如何才能相处的融洽"
messages = chat_prompt.format_messages(question=input_question)

# 调用并输出结果
response = model.invoke(messages)
print(response.content)