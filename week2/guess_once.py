import random
dice = random.randint(1,100)
guess = int(input("请输入你猜的数字："))
if guess>100 or guess < 1:
    print("请重新输入位于1至100之间的数")
elif guess > dice:
    print("猜大了")
elif guess < dice:
    print("猜小了")
else:
    print("猜对了")
print(f"答案是{dice}")

