vowels = ('a', 'e', 'i', 'o', 'u')
text = 'hteahnfuqeajktehinbzvqoyhtnuunqj'
# text = 'hteahnfuqeajktehnbzvqoyhtnuunqj'

left = 0
vowel = 0
for i in range(len(text)):
    if text[i] == 'a':
        left = i
        i += 1
        while vowel != 4 and i < len(text):
            if text[i] in vowels:
                if text[i] == vowels[vowel + 1]:
                    vowel += 1
                else:
                    break
            i += 1
        if vowel == 4:
            print(True)
            break

if vowel != 4:
    print(False)
