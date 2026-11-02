vocab = {}
with open("vocab.txt","r",encoding="utf-8") as f:
    word = f.read()
    word = word.split("\n")
    for line in word:
        if line == "":
            continue
        parts = line.split(",")
        vocab[parts[0]] = parts[1]
print(vocab)