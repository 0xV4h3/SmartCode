# ex 144
def are_phrases_anagrams(first, second)->bool:
    first_letters = dict()
    second_letters = dict()
    i = 0
    first = first.upper()
    second = second.upper()
    while i < len(first):
        if first[i].isalnum():
            if first[i] in first_letters:
                first_letters[first[i]] += 1
            else:
                first_letters[first[i]] = 1
        i += 1

    i = 0
    while i < len(second):
        if second[i].isalnum():
            if second[i] in second_letters:
                second_letters[second[i]] += 1
            else:
                second_letters[second[i]] = 1
        i += 1

    if first_letters == second_letters:
        return True

    return False

if __name__ == '__main__':
    first_phrase = input("Enter first phrase: ")
    second_phrase = input("Enter second phrase: ")
    if are_phrases_anagrams(first_phrase, second_phrase):
        print(f"{first_phrase} and {second_phrase} are anagrams")
    else:
        print(f"{first_phrase} and {second_phrase} are not anagrams")