for i in range(1,21):
    if i % 3 == 0 and i & 5 == 0 :
        print("FizzBuzz")
    else:
        print(i)
    if i % 3 == 0 :
        print("Fizz")
    else:
        print(i)
    if i % 5 ==0:
        print("Buzz")
    else:
        print(i)