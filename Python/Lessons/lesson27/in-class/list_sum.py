from functools import wraps

def pair_summer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pairs = args[0] if args else []
        return [func(a, b, *args[1:], **kwargs) for a, b in pairs]
    return wrapper

@pair_summer
def add(a: int, b: int) -> int:
    return a + b

print(add([(7, 4), (8, 8), (10, 26), (22, -4)]))

# from functools import wraps
#
# def pair_summer(func):
#     @wraps(func)
#     def wrapper(pairs: list[tuple[int, int]]) -> list[int]:
#         return [func(a, b) for a, b in pairs]
#     return wrapper
#
# @pair_summer
# def add(a: int, b: int) -> int:
#     return a + b
#
# print(add([(7, 4), (8, 8), (10, 26), (22, -4)]))

