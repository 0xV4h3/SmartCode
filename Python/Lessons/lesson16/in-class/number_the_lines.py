# Exercise 152: Number the Lines in a File
def num_lines():
    command = input("> ").strip()
    if not command:
        raise Exception("Empty command")

    words = command.split()

    if words[0] != 'numline':
        raise Exception("Wrong command")

    if len(words) < 3:
        raise Exception("Incomplete arguments provided")

    source = words[1]
    destination = words[2]

    errors = []

    try:
        with open(source, mode='r') as fs:
            old_lines = fs.readlines()
            try:
                with open(destination, mode='w') as fd:
                    for i in range(len(old_lines)):
                        fd.write(f"{i + 1}: {old_lines[i]}")
            except FileNotFoundError:
                errors.append(f"file '{fd}' not found")
            except Exception as e:
                errors.append(f"error reading '{fd}': {e}")
    except FileNotFoundError:
        errors.append(f"file '{fs}' not found")
    except Exception as e:
        errors.append(f"error reading '{fs}': {e}")

    if errors:
        for err in errors:
            print(err)



if __name__ == "__main__":
    num_lines()