import random

answer = random.randint(0, 100)
guess = 0      # ①
count = 0

while guess != answer:         # ②
    guess = int(input("猜一个 1-100 的数："))
    count = count + 1    # ③没出现一次count就多一次

    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        print("猜对了")

print(f"你一共猜了 {count} 次")
