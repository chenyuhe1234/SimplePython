from openai import OpenAI
import json

"""
   LLM(在线千问模型) + 工具调用 ----- > 样例代码 更好的理解工具调用
"""
# 1. 配置客户端 (推荐使用 DashScope 的 OpenAI 兼容模式)
client = OpenAI(
    api_key="sk-2db88a2dc4564fcdbf47bc2f1b3e6355",  # 替换为你的实际 Key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# 2. 定义本地工具函数 (真正干活的"工人")
def get_current_weather(location: str) -> str:
    """模拟天气查询API"""
    return f"{location}今天是晴天，气温 25℃，微风。"


# 工具映射表，方便后续通过名称查找并执行对应的函数
TOOL_MAP = {
    "get_current_weather": get_current_weather,
}

# 3. 注册工具到模型 (告诉模型有哪些工具可用)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "当你想查询指定城市的天气时非常有用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市名称，例如：北京、杭州"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# 4. 核心交互循环
messages = [
    {"role": "system", "content": "你是一个智能助手，可以帮用户查询天气信息。"},
    {"role": "user", "content": "杭州今天天气怎么样？"}
]

# 第一次调用：让模型判断是否需要工具
response = client.chat.completions.create(
    model="qwen-max",
    messages=messages,
    tools=tools,
    temperature=0.7
)

message = response.choices[0].message



 # 1. 使用 .model_dump() 将 Pydantic 对象转换为标准 Python 字典
response_dict = response.model_dump()
# 2. 将字典序列化为 JSON 字符串
# ensure_ascii=False 确保中文字符正常显示，不被转义为 Unicode
json_string = json.dumps(response_dict, ensure_ascii=False, indent=2)
print(f"[模型判断是否调用工具]:{json_string}")

# 如果模型决定不调用工具，直接返回回答
if not message.tool_calls:
    print("模型直接回复:", message.content)
else:
    # 模型决定调用工具，解析参数并在本地执行
    messages.append(message)  # 将模型的调用请求加入历史对话

    for tool_call in message.tool_calls:
        func_name = tool_call.function.name
        func_args = json.loads(tool_call.function.arguments)

        # 执行对应工具获取真实数据
        if func_name in TOOL_MAP:
            result = TOOL_MAP[func_name](**func_args)
        else:
            result = json.dumps({"error": f"未知工具：{func_name}"})

        print(f"[系统日志] 正在执行工具: {func_name}, 参数: {func_args},结果:{result}")

        # 将工具执行的结果追加到对话上下文中
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })

    # 第二次调用：让模型根据工具返回的真实数据，生成自然语言回复
    final_response = client.chat.completions.create(
        model="qwen-max",
        messages=messages
    )
    print("最终回复:", final_response.choices[0].message.content)