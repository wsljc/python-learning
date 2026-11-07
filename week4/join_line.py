pairs = [["book", "书"], ["apple", "苹果"], ["water", "水"]]
with open("vocab.txt", "w", encoding="utf-8") as f:
    for pair in pairs:
        f.write(",".join(pair) + "\n")
