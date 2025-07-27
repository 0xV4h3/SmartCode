#brackets problem
text = input("Enter text with brackets: ")
brackets_open = {'{': 1, '(': 2, '[': 3}
brackets_close = {'}': 1, ')': 2, ']': 3}
brackets = []

for char in text:
    if char in brackets_open or char in brackets_close:
        brackets.append(char)

print(f"Text: {text}")
if len(brackets) % 2 != 0:
    print("Syntax error")
else:
    while brackets:
        close_b = brackets.pop()
        open_b = brackets.pop()
        if open_b not in brackets_open or close_b not in brackets_close:
            print("Syntax error")
            break
        if brackets_open[open_b] != brackets_close[close_b]:
            print("Syntax error")
            break
    else:
        print("Valid syntax")


