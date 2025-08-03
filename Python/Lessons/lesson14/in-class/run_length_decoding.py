# 185 from The Python Workbook
from typing import List

def rle_decode(compressed_data : List) -> List:
    if not compressed_data:
        return []
    else:
        return [compressed_data[0]] * compressed_data[1] + rle_decode(compressed_data[2:])

if __name__ == "__main__":
    data = ["A", 12, "B", 4, "A", 6, "B", 1]
    print(rle_decode(data))

