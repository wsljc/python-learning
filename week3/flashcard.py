flashcard = {
    "hello" : "你好",
    "water" : "水",
    "phone" : "手机"
}
word = input("请输入你要查询的英语单词：")
if word in flashcard:
    print(flashcard[word])
else:
    print("没收录")