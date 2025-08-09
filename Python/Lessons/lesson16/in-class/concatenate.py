# Exercise 151: Concatenate Multiple Files
def cat():
    command = input("> ").strip()
    if not command:
        raise Exception("Empty command")

    words = command.split()
    if words[0] != 'cat':
        raise Exception("Wrong command")

    if len(words) < 2:
        raise Exception("No arguments provided")

    result = ''
    errors = []

    for fname in words[1:]:
        try:
            with open(fname, mode='r') as f:
                result += f.read()
        except FileNotFoundError:
            errors.append(f"file '{fname}' not found")
        except Exception as e:
            errors.append(f"error reading '{fname}': {e}")

    if errors:
        for err in errors:
            print(err)
    else:
        print(result)


if __name__ == "__main__":
    cat()
