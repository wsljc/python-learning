first = ["book","书"]
first = ",".join(first)
second = ["apple","苹果"]
second = ",".join(second)
third = ["water","水"]
third = ",".join(third)
with open("vocab.txt","w",encoding="utf-8") as f:
    f.write(f"{first}\n")
    f.write(f"{second}\n")
    f.write(f"{third}\n")