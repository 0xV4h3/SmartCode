def common_member(first, second)-> bool:
    for member in first:
        if member in second:
            print(f"Common member: {member}")
            return True
    return False

if __name__ == '__main__':
    first_list = []
    print("First list members")
    item = input("Enter item: ")
    while item != '':
        first_list.append(item)
        item = input("Enter item: ")

    second_list = []
    print("Second list members")
    item = input("Enter item: ")
    while item != '':
        second_list.append(item)
        item = input("Enter item: ")

    print(first_list)
    print(second_list)
    print(common_member(first_list, second_list))

