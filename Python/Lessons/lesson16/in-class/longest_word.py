# Exercise 153: Find the LongestWord in a File
def longest_word():
    command = input("> ").strip()
    if not command:
        raise Exception("Empty command")

    words = command.split()

    if words[0] != 'numline':
        raise Exception("Wrong command")

    if len(words) < 3:
        raise Exception("Incomplete arguments provided")

if __name__ == "__main__":
    longest_word()