with open("demo.txt","r",encoding ="utf-8") as f:
    print(f.read())
    f.seek(0)
    for line in f:
        print(repr(line))