# Next bigger number with the same digits
# https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n):
    s = list(str(n))

    for i in range(len(s)-2, -1, -1):
        if s[i] < s[i+1]:
            break
    else:
        return -1

    right = s[i+1:]
    pivot = s[i]

    candidate = min(x for x in right if x > pivot)
    right.remove(candidate)
    right.append(pivot)
    right.sort()

    return int(''.join(s[:i] + [candidate] + right))

number = input("Enter number: ")
print(f"Next bigger number with the same digits of {number}")
print(next_bigger(number))