from typing import List

def simple_rle(numbers: List[int], next_list: List[int] = [], previous: int = -1) -> List[int]:
    if len(next_list) == 1 and not numbers:
        return next_list

    if not numbers:
        return simple_rle(next_list, [], -1)

    current = numbers[0]
    if not next_list:
        next_list.append(1)
    elif current == previous:
        next_list[-1] += 1
    else:
        next_list.append(1)

    return simple_rle(numbers[1:], next_list, current)

if __name__ == "__main__":
    print(simple_rle([2,2,2,1,5,6,3,3,7,7,8,1,1]))