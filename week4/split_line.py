line = "apple,苹果\n"
line = line.strip("\n")
parts = line.split(",")
print(f"单词：{parts[0]}\n释义：{parts[1]}")
