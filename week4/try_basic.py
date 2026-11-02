try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("不能除以零")

try:
    with open("hihi","r",encoding="utf-8"):
        print("成功打开")
except FileNotFoundError:
    print("文件不存在")