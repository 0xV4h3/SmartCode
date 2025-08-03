# 186 from The Python Workbook
from typing import List
from run_length_decoding import rle_decode

def rle_encode(data: List) -> List:
    if not data:
        return []
    else:
        i = 0
        symbol = data[i]
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
        return [symbol, i + 1] + rle_encode(data[i + 1:])


if __name__ == "__main__":
    data = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
    compressed = rle_encode(data)
    print(compressed)
    decompressed = rle_decode(compressed)
    print(decompressed)
    if decompressed == data:
        print("RLE is working")
    else:
        print("Data lose")