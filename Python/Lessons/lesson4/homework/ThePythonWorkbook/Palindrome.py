#75 from The Python Workbook
word = input("Enter word: ")

is_palindrome = True

for i in range(0, len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

