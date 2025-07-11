def vowelOrConsonant(x):
    if x.lower() in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

if __name__ == '__main__':
    character = input('Enter a character: ')
    if (not character.isalpha()) or (len(character) != 1):
        print("Invalid character")
    else:
        print(f"Character is {vowelOrConsonant(character)}")
