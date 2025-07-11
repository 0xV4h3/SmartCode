word = input("Enter a word: ")
count = 0
for letter in word:
    if letter.lower() in "aeiou":
        count += 1
print(f"Number of vowels: {count}")
