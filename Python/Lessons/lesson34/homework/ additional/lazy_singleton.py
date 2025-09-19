import threading

class LazySingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    print("LazySingleton is created!")
        return cls._instance

    def show_message(self):
        print("Hello from Vahe's LazySingleton!")

if __name__ == "__main__":
    s1 = LazySingleton()
    s1.show_message()

    s2 = LazySingleton()
    s2.show_message()

    if s1 is s2:
        print("Both references point to the same instance!")