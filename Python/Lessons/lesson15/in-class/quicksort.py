from typing import List

def quicksort(numbers : List[int], reverse = False) -> List[int]:
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[0]
        less = []
        great = []
        equal = []
        for num in numbers:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                great.append(num)
            else:
                equal.append(num)

        if reverse:
            return quicksort(great, reverse) + equal + quicksort(less, reverse)
        else:
            return quicksort(less) + equal + quicksort(great)

if __name__ == "__main__":
    print('Enter list')
    num_list = []
    sorted = []
    num = input()
    while num != '':
        num_list.append(int(num))
        num = input()

    if num_list:
        is_reverse = bool(input("Reverse or not - True/False : "))
        if is_reverse:
            sorted = quicksort(num_list, is_reverse)
        else:
            sorted = quicksort(num_list)
        print(f"List: {num_list}")
        print(f"Sorted List: {sorted}")
    else:
        print("Nothing to sort")
