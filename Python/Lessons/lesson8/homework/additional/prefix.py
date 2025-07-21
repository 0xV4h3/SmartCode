# ex1
def common_prefix(words):
    if not words:
        return ''
    for j in range(len(words[0])):
        for i in range(1, len(words)):
            if words[i][:j] != words[0][:j]:
                return words[0][:j - 1]
    return word[0]

if __name__ == '__main__':
    word_list = []
    com_prefix = ""

    word = input("Enter word: ")
    while word != '':
        word_list.append(word)
        word = input("Enter word: ")

    com_prefix = common_prefix(word_list)
    print(word_list)
    print(f"Common prefix: {com_prefix}")







