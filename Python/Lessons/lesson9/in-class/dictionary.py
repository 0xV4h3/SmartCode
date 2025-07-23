# alpha_num = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# alpha_num_sorted =dict(sorted(alpha_num, key= alpha_num.get, reverse=True))
#
# i = 0
# for key, value in alpha_num_sorted:
#     print(f"{key} : {value}")
#     i += 1
#     if i == 3:
#         break
from Tools.scripts.generate_re_casefix import alpha

# workbook 145
# alphabet = dict()
#
# alphabet.update(dict.fromkeys(list("AEILNORSTU"), 1))
# alphabet.update(dict.fromkeys(list("DG"), 2))
# alphabet.update(dict.fromkeys(list("BCMP"), 3))
# alphabet.update(dict.fromkeys(list("FHVWY"), 4))
# alphabet.update(dict.fromkeys(list("K"), 5))
# alphabet.update(dict.fromkeys(list("JX"), 8))
# alphabet.update(dict.fromkeys(list("QZ"), 10))
#
# text = input("Enter text: ")
# value = 0
#
# for letter in text:
#     value += alphabet.get(letter.upper())
#
# print(f"Text: {text}\nValue: {value}")




