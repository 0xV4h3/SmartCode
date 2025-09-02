import datetime
from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Doc: {func.__doc__}")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open("logs.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.datetime.now()} | {func.__name__} | {type(e).__name__}: {e}\n")
            return None
    return wrapper

@logging
def divide(x: int, y: int) -> float:
    """Divides two numbers"""
    return x / y

@logging
def to_upper(text: str) -> str:
    """Converts text to uppercase"""
    return text.upperr()

@logging
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(5, 0))
    print(to_upper("hello"))
    print(add(3, 7))
