# ex 143
def are_anagrams(first, second)->bool:
    if len(first) != len(second):
        return False

    first_letters = dict()
    second_letters = dict()
    i = 0
    first = first.upper()
    second = second.upper()
    while i < len(first):
        if first[i] in first_letters:
            first_letters[first[i]] += 1
        else:
            first_letters[first[i]] = 1

        if second[i] in second_letters:
            second_letters[second[i]] += 1
        else:
            second_letters[second[i]] = 1

        i += 1

    if first_letters == second_letters:
        return True

    return False

if __name__ == '__main__':
    first_word = input("Enter first word: ")
    second_word = input("Enter second word: ")
    if are_anagrams(first_word, second_word):
        print(f"{first_word} and {second_word} are anagrams")
    else:
        print(f"{first_word} and {second_word} are not anagrams")