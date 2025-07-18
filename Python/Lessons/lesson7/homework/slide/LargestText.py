text_list = []

text = input("Enter text: ")
while text != '':
    text_list.append(text)
    text = input("Enter text: ")

print(f"List: {text_list}")
text_list.sort(key=len, reverse=True)
print(f"Largest text from a list: {text_list[0]}")