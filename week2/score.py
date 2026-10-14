score = float(input("请输入你的考试分数："))

if score < 0 or score > 100:
    print("输入的分数必须在 0-100 之间！")
elif 100 >= score >= 90:
    print("优秀")
elif 90 > score >= 60:
    print("及格")
elif 60 > score:
    print("不及格")
