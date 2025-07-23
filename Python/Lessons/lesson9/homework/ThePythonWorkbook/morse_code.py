# ex 139
def morse_code(text)->str:
    if text == '':
        return ''

    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    code = ''
    for letter in text:
        if letter.upper() in morse:
            code += (morse[letter.upper()] + ' ')
    return code

if __name__ == '__main__':
    test_text = input("Enter text: ")
    test_code = morse_code(test_text)
    print(f"morse code: {test_code}")