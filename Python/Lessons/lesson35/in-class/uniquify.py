from typing import List

def uniquify(vals: List[any]) -> List[any]:
    if not vals: return []
    rest = uniquify(vals[1:])
    return [vals[0]] + rest if vals[0] not in rest else rest

if __name__ == "__main__":
    print(uniquify([42, 'spam', 42, 5, 42, 5, 'spam', 42, 5, 5, 5]))
    print(uniquify([0, 1, 2, 3, 0, 1, 2]))