# Exercise 155:Words that OccurMost
from typing import List

def freq_word() -> (int, List[str]):
    command = input("> ").strip()
    if not command:
        raise Exception("Empty command")

    arguments = command.split()
    if arguments[0] != 'freq_word':
        raise Exception("Wrong command")

    write_result = False
    if len(arguments) < 2:
        raise Exception("No arguments provided")
    elif len(arguments) > 3:
        raise Exception("Too many arguments provided")
    elif len(arguments) == 3:
        write_result = True

    count = {}
    errors = []

    def words(sentence: str) -> List[str]:
        unclean_words = sentence.split()
        clean_words = []
        def clean(word: str) -> str:
            while word and not word[-1].isalnum():
                word = word[:-1]
            while word and not word[0].isalnum():
                word = word[1:]
            return word.lower()
        for unclean_word in unclean_words:
            cleaned = clean(unclean_word)
            if cleaned:
                clean_words.append(cleaned)
        return clean_words

    source = arguments[1]
    try:
        with open(source, mode='r') as s:
            for line in s:
                line_words = words(line.strip())
                for word in line_words:
                    count[word] = count.get(word, 0) + 1

        if not count:
            if write_result:
                destination = arguments[2]
                try:
                    with open(destination, mode='w') as d:
                        d.write("Source is empty\n")
                except Exception as e:
                    errors.append(f"error writing '{destination}': {e}")
            return 0, []

        quantities = sorted(set(count.values()))
        most_number = quantities[-1]

        result = {num: [] for num in quantities}
        for word, number in count.items():
            result[number].append(word)

        most_words = result[most_number]

        if write_result:
            destination = arguments[2]
            try:
                with open(destination, mode='w') as d:
                    for key, value in result.items():
                        d.write(f"{key} : {value}\n")
            except Exception as e:
                errors.append(f"error writing '{destination}': {e}")

        if errors:
            for err in errors:
                print(err)

        return most_number, most_words

    except FileNotFoundError:
        errors.append(f"file '{source}' not found")
    except Exception as e:
        errors.append(f"error reading '{source}': {e}")

    for err in errors:
        print(err)
    return None

if __name__ == "__main__":
    print(freq_word())
