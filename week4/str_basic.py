# 1. strip：去掉两端的空白
text = "   hello world   "
print(f"[{text}]")
print(f"[{text.strip()}]")

# 2. split：按分隔符切开
line = "apple,苹果"
print(line.split(","))

# 3. join：把一堆东西拼成一个
words = ["a", "b", "c"]
print("-".join(words))
