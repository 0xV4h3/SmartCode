# ex4
def simple_rle(data_stream) -> list:
    compressed = []
    i = 0
    while i < len(data_stream):
        repetition = 1
        while i + 1 < len(data_stream) and data_stream[i] == data_stream[i + 1]:
            repetition += 1
            i += 1
        compressed.append(repetition)
        i += 1
    return compressed

if __name__ == '__main__':
    numbers = []
    number = input("Enter number: ")
    while number != '' and number.isdigit():
        numbers.append(int(number))
        number = input("Enter number: ")

    if not numbers:
        print("There is no number to compress")
    else:
        compress = simple_rle(numbers)
        while len(compress) != 1:
            print(compress)
            compress = simple_rle(compress)
        print(compress)

