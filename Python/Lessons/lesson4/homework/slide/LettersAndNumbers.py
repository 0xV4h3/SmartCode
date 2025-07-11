text = input("Enter text: ")
letters = 0
digits = 0
symbols = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print(f"Letters : {letters}\nDigits : {digits}\nSymbols : {symbols}\n")