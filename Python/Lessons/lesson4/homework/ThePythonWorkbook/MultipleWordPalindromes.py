#76 from The Python Workbook
phrase = input("Enter a phrase: ")

cleaned = ""
for char in phrase:
    if char.isalnum():
        cleaned += char.lower()

is_palindrome = True

for i in range(0, len(cleaned) // 2):
    if cleaned[i] != cleaned[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("The phrase is a palindrome.")
else:
    print("The phrase is not a palindrome.")
