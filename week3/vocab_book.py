vocab_book = {
    "apple" : "苹果",
    "water" : "水",
    "desk" : "桌子",
}

while True:
    number = input("请输入你需要的功能（1.查词 2.添加单词 3.删除单词 4.退出 5.查看全部）:")
    if number == "1":
       word = input("请输入你要查询的单词:")
       if word in vocab_book:
           print(vocab_book[word])
       else:
           print("没有收录")
    elif number == "2":
        meaning = input("请输入单词的释义：")
        word = input("请输入单词：")
        vocab_book[word] = meaning
    elif number == "3" :
        word = input("请输入你要删除的词：")
        if word in vocab_book:
            del vocab_book[word]
            print(f"已删除{word}")
        else :
            print("没有收录")
    elif number == "4":
        print("退出程序")
        break
    elif number == "5" :
        for word, meaning in vocab_book.items():
            print(f"{word} : {meaning}")

    else:
        print("无效选择")

