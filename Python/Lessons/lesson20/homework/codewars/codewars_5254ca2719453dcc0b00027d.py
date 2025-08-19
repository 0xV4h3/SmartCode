# So Many Permutations!
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

def permutations(s):
    p = set()
    s = list(s)

    def backtrack(start):
        if start == len(s):
            p.add("".join(s))
            return
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]

    backtrack(0)
    return list(p)

my_string = input("Enter string: ")
print(f"Shufflings of {my_string}")
print(permutations(my_string))