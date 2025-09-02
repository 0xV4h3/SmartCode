from functools import wraps

def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function '{func.__name__}' has been called {wrapper.calls} time(s).")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@counter
def divide(x: int, y: int) -> float:
    """Divides two numbers"""
    return round((x / y), 2)

@counter
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(12, 7))
    print(add(2, 3))
    print(add(5, 7))
    print(divide(12, 7))
    print(add(10, 20))