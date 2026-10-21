import random
answer = random.randint(1,100)
guess = 0
count = 0
while guess != answer :
    guess = int(input("请输入你猜的数字："))
    count = count + 1
    if guess > answer:
        print("猜大了")
    elif guess < answer:
        print("猜小了")
print("猜对了")
print(f"猜了{count}次")