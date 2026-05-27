import requests

"""
通过构建请求 去访问本地部署的qwen3:latest 模型-多轮对话 可以记住前面的信息
"""
# 如果是 /api/chat 接口，data 需要这样写：
data = {
    "model": "qwen3",
    "messages": [
        {"role": "user", "content": "你好，我叫小明。"},
        {"role": "assistant", "content": "你好小明，很高兴认识你！"},
        {"role": "user", "content": "我叫什么名字？"}
    ],
    "stream": False
}
try:
    # 发送 POST 请求，设置 120 秒超时
    response = requests.post(
        "http://127.0.0.1:11434/api/chat",
        json=data,
        timeout=120
    )

    # 检查 HTTP 状态码是否为 200 (请求成功)
    response.raise_for_status()

    # 解析并打印结果
    result = response.json()
    print("模型回复：")
    print(response.json().get("message", {}).get("content", ""))

except requests.exceptions.Timeout:
    print("请求超时！模型响应时间过长，请稍后再试。")
except requests.exceptions.ConnectionError:
    print("连接失败！请检查 Ollama 软件是否已经正常启动。")
except Exception as e:
    print(f"发生未知错误：{e}")
