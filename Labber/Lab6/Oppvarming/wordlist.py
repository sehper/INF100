def filter_wordlist(path, search_string):
    words = []

    with open(path, encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            if search_string in word:
                words.append(word)

    return words