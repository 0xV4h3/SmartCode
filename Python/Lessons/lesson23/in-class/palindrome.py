def palindrome(s : str) -> bool:
    return s == s[::-1]

word = input('Input word: ')
if palindrome(word):
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")