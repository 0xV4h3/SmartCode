# word = input("Enter word: ")
# words = []
#
# while word != "":
#     if word not in words:
#         words.append(word)
#
#     word = input("Enter word: ")
#
# print(words)

# x = [7, 7, 4, 4, 4, 4, 4, 4, 4, 1, 2, 2, 2, 10, 10, 2, 8, 6, 5, 7]
#
# for i in range(len(x)-1,-1,-1):
#     print(x[i])
#     if x[i] % 2 == 0:
#         x.pop(i)
#
# print(x)

#134 from Workbook

# x = [1, 2, 3, 4]
# combinations = [[]]
#
# for i in range(len(x)):
#     for j in range(i + 1 , len(x) + 1):
#         combination = []
#         for z in range(i, j):
#             combination.append(x[z])
#
#         combinations.append(combination)
#
# combinations.sort(key=len)
# print(combinations)



