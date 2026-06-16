from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_classic.chains import LLMChain
"""
   通过LangChain框架 来问千问模型问题-样例代码3
   使用LangChain链进行处理 
"""
# 1. 初始化通义千问模型
model = ChatOpenAI(
    model="qwen-max",
    openai_api_key="sk-2db88a2dc4564fcdbf47bc2f1b3e6355",
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=0.7
)

# 2. 创建提示词模板 (保持你原来的双模板结构)
# 定义系统消息模板
system_template = "你是一个情感专家"
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

# 定义人类消息模板
human_template = "{question}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 【关键步骤】将两者组合成一个完整的聊天提示词模板
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# 3. 使用 LLMChain 进行组装和调用

# 执行调用
input_question = "异性之间如何才能相处的融洽"
chain = chat_prompt | model  # 使用 | 运算符组合
response = chain.invoke({"question": input_question})  # 使用 invoke() 替代 run()
print(response)