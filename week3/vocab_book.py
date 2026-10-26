vocab_book = {
    "apple" : "苹果",
    "water" : "水",
    "desk" : "桌子",
}
while True:
    number = input("请输入你需要的功能（1.查词 2.添加单词 3.退出）:")
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
    elif number == "3":
        print("退出程序")
        break
    else:
        print("无效选择")

