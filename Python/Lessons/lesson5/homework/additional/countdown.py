def dots(begin, end):
    digits = ''
    for i in range(begin, end - 1, -1):
        digits += str(i)
    return len(digits) - len(str(begin))

def countdown(begin, end=0,separator=" "):
    if end == begin:
        print(f"{begin}{begin}")
        return
    elif end > begin:
        end, begin = begin, end

    max_dots = dots(begin, end)

    for step in range(0, begin - end + 1):
        left = ''
        for i in range(begin, begin - step - 1, -1):
            left += str(i)
        right = ''
        for i in range(begin - step, begin + 1):
            right += str(i)
        dots_count = (max_dots - len(left) + len(str(begin)))
        middle = separator * dots_count * 2
        print(left + middle + right)

if __name__ == '__main__':
    start = int(input("Enter start number: "))
    finish = int(input("Enter finish number: "))
    punc = input("Enter punctuator: ")
    countdown(start, finish, punc[0])