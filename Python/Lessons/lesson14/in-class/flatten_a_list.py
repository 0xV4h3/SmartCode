# 184 from The Python Workbook
from typing import List
def flatten(nested_list: List) -> List:
    if not nested_list:
        return []
    elif isinstance(nested_list[0], list):
        return flatten(nested_list[0]) + flatten(nested_list[1:])
    else:
        return [nested_list[0]] + flatten(nested_list[1:])

if __name__ == "__main__":
    mylist = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
    print(flatten(mylist))