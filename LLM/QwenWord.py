from transformers import AutoTokenizer
"""
   分词
"""
# 加载 Qwen 的分词器（这里以 Qwen2.5-7B 为例）
model_name = "Qwen/Qwen2.5-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

# 定义要测试的文本
text = "我喜欢你"

# 核心方法：计算 token 数量
token_count = len(tokenizer.encode(text))

print(f"文本: '{text}'")
print(f"占用 Token 数量: {token_count}")

# 【可选】如果你想看看具体被切分成了哪些 token，可以打印详情：
# text = "我喜欢你"
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)
print(f"Token 切分结果: {tokens}") # Token 切分结果: ['我', '喜欢你']
print(f"对应的 Token ID: {token_ids}") # 对应的 Token ID: [109366, 56568]