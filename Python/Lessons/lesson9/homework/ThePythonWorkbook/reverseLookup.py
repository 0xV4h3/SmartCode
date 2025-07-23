# ex 136
def reverseLookup(dictionary, target_value)->list:
    key_list = []
    for key in dictionary:
        if dictionary[key] == target_value:
            key_list.append(key)

    return key_list

if __name__ == '__main__':
    test_dict = {}
    num_entries = int(input("Enter the number of entries you want to add: "))

    for _ in range(num_entries):
        test_key = input("Enter the key: ")
        test_value = int(input("Enter the value: "))
        test_dict[test_key] = test_value

    if not test_dict:
        print("Dictionary is empty")
    else:
        print(test_dict)
        test_target_value = int(input("Enter the value to find keys for: "))
        test_list = reverseLookup(test_dict, test_target_value)
        if not test_list:
            print(f"There are no key with {test_target_value}")
        else:
            print(f"List of key(s) with {test_target_value}")
            print(test_list)

