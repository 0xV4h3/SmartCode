import random

user = input("Enter your choice(Rock/Paper/Scissors) : ")
pc = random.choice(['Rock', 'Paper', 'Scissors'])
print(f"PC's choice : {pc}")

if user == 'Rock':
    if pc == 'Rock':
        print("Draw")
    if pc == 'Paper':
        print("You lost!")
    if pc == 'Scissors':
        print("You win!")
elif user == 'Paper':
    if pc == 'Rock':
        print("You win!")
    if pc == 'Paper':
        print("Draw")
    if pc == 'Scissors':
        print("You lost!")
elif user == 'Scissors':
    if pc == 'Rock':
        print("You lost!")
    if pc == 'Paper':
        print("You win!")
    if pc == 'Scissors':
        print("Draw")
else:
    print(f"Invalid choice : {user}")