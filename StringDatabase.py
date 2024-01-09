class StringDatabase:
    def readFile():
        with open("four_letters.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            words = []
            for line in lines:
                word = line.split()
                words.extend(word)
        return words
    