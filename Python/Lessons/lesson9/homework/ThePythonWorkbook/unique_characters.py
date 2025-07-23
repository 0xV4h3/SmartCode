# ex 142
def unique(text)->int:
    if text == '':
        return 0
    symbols = dict.fromkeys(list(text), 0)
    return len(symbols)

if __name__ == '__main__':
    test_text = input("Enter text: ")
    count = unique(test_text)
    print(f"Number of unique characters: {count}")