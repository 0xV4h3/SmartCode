# 87 from The Python Workbook
def shipping_calculator(items : int) -> float:
    return 10.95 + (items - 1) * 2.95

if __name__ == "__main__":
    item = int(input("Enter purchased items: "))
    print(f"Charge: {shipping_calculator(item)}")