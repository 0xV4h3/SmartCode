# Exercise 176:The NATO Phonetic Alphabet
from typing import List

def word_to_phonetic(word : str) -> str:
    nato_alphabet = {
        'A': 'Alpha',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliett',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'X-ray',
        'Y': 'Yankee',
        'Z': 'Zulu'
    }
    if len(word) == 1:
        return nato_alphabet[word[0].upper()]
    else:
        if not word[0].isalpha():
            return word_to_phonetic(word[1:])
        else:
            if len(word) == 2 and not word[-1].isalpha():
                return nato_alphabet[word[0].upper()]
            else:
                return nato_alphabet[word[0].upper()] + ' ' + word_to_phonetic(word[1:])

def phonetic_to_word(phonetic : List[str]) -> str:
    nato_reverse = {
        'Alpha': 'A',
        'Bravo': 'B',
        'Charlie': 'C',
        'Delta': 'D',
        'Echo': 'E',
        'Foxtrot': 'F',
        'Golf': 'G',
        'Hotel': 'H',
        'India': 'I',
        'Juliett': 'J',
        'Kilo': 'K',
        'Lima': 'L',
        'Mike': 'M',
        'November': 'N',
        'Oscar': 'O',
        'Papa': 'P',
        'Quebec': 'Q',
        'Romeo': 'R',
        'Sierra': 'S',
        'Tango': 'T',
        'Uniform': 'U',
        'Victor': 'V',
        'Whiskey': 'W',
        'X-ray': 'X',
        'Yankee': 'Y',
        'Zulu': 'Z'
    }
    if len(phonetic) == 1:
        return nato_reverse[phonetic[0]]
    else:
        return nato_reverse[phonetic[0]] + phonetic_to_word(phonetic[1:])

if __name__ == "__main__":
    word = input("Enter word: ")
    phonetic = word_to_phonetic(word)
    print(phonetic)
    phonetic = phonetic.split(' ')
    print(phonetic_to_word(phonetic))