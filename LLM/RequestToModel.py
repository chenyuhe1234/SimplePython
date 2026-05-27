import requests

"""
通过构建请求 去访问本地部署的qwen3:latest 模型-单条信息
"""
# 准备请求数据
data = {
    "model": "qwen3",  # 确保你本地已经拉取了这个模型 (ollama pull qwen3)
    "prompt": "你是谁?",
    "stream": False  # 关闭流式输出，一次性返回完整结果
}

try:
    # 发送 POST 请求，设置 120 秒超时
    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json=data,
        timeout=120
    )

    # 检查 HTTP 状态码是否为 200 (请求成功)
    response.raise_for_status()

    # 解析并打印结果
    result = response.json()
    print("模型回复：")
    print(result.get("response", "未获取到回复内容"))

except requests.exceptions.Timeout:
    print("请求超时！模型响应时间过长，请稍后再试。")
except requests.exceptions.ConnectionError:
    print("连接失败！请检查 Ollama 软件是否已经正常启动。")
except Exception as e:
    print(f"发生未知错误：{e}")
