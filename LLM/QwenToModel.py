import dashscope
from dashscope import Generation
"""
通过pip install dashscope库访问在线千问大模型
"""
# 1. 设置你的 API Key
dashscope.api_key = "sk-2db88a2dc4564fcdbf47bc2f1b3e6355"  # 建议实际使用时通过环境变量读取，避免硬编码

# 2. 发起请求
try:
    response = Generation.call(
        model='qwen-max',
        messages=[
            {'role': 'system', 'content': '你是一个乐于助人的AI助手。'},
            {'role': 'user', 'content': '请用Python写一个快速排序函数。'}
        ],
        temperature=0.7,  # 【新增】控制创造性，值越高越有创意，越低越严谨
        max_tokens=1000 # 【新增】限制单次回复的最大长度，防止“滔滔不绝”
    )

    # 3. 打印结果（适配 DashScope 官方返回格式）
    if response.status_code == 200:
        print("模型回复:")
        # 通义千问的标准返回格式是 response.output.text
        print(response.output.text)
    else:
        print("请求失败:", response.code, response.message)

except Exception as e:
    print("调用异常:", e)
    # 调试小技巧：如果依然报错，可以取消下面这行的注释，看看接口到底返回了什么
    # print("完整返回对象:", response)