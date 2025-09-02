import time
import requests
from functools import wraps
from bs4 import BeautifulSoup

def delay(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting {seconds} second(s) before calling {func.__name__}...")
            time.sleep(seconds)
            result = func(*args, **kwargs)
            print(f"{func.__name__} has finished.")
            return result
        return wrapper
    return decorator

@delay(2)
def fetch_decorator_intent() -> str:
    url = "https://refactoring.guru/design-patterns/decorator"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    intent_header = soup.find("h2", id="intent")
    if not intent_header:
        return "Could not find the Intent section"

    intent_paragraph = intent_header.find_next("p")
    return intent_paragraph.get_text(strip=True)

if __name__ == "__main__":
    fragment = fetch_decorator_intent()
    print("Intent section text:\n", fragment)
