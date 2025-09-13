import uuid
from typing import List, Dict, Optional

class BankCard:
    def __init__(self, account: "BankAccount", name: str, surname: str, card_number: str, cvv: str, pin: str):
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("card_number must be exactly 16 digits")
        if len(cvv) not in (3, 4) or not cvv.isdigit():
            raise ValueError("CVV must be a 3- or 4-digit string")
        self.__account = account
        self.__name = name
        self.__surname = surname
        self.__card_number = card_number
        self.__cvv = cvv
        self.__pin = pin
        self.__trials = 0
        self.__max_trials = 3
        self.__is_authenticated = False
        self.__unique_id: Optional[str] = None

    def can_attempt(self) -> bool:
        return self.__trials < self.__max_trials

    def make_action(self, pin: str) -> bool:
        if self.__is_authenticated:
            print("Authenticated.")
            return True
        if not self.can_attempt():
            print("Maximum attempts exceeded.")
            return False
        if pin == self.__pin:
            self.__unique_id = str(uuid.uuid4())
            self.__is_authenticated = True
            self.__trials = 0
            print("Authenticated.")
            return True
        else:
            self.__trials += 1
            remaining = max(0, self.__max_trials - self.__trials)
            print(f"Invalid PIN. Attempt {self.__trials}/{self.__max_trials}. Remaining attempts: {remaining}")
            return False

    def withdraw(self, amount: int) -> bool:
        if not self.__is_authenticated:
            print("Not authenticated.")
            return False
        success = self.__account.withdraw(amount, card_number=self.__card_number)
        if success:
            print(f"Withdrew ${amount}.")
        else:
            print("Withdrawal failed.")
        return success

    def deposit(self, amount: int) -> bool:
        if not self.__is_authenticated:
            print("Not authenticated.")
            return False
        success = self.__account.deposit(amount, card_number=self.__card_number)
        if success:
            print(f"Deposited ${amount}.")
        else:
            print("Deposit failed.")
        return success

    def exit(self):
        self.__is_authenticated = False
        print("Logged out.")

    @property
    def balance(self) -> Optional[int]:
        if not self.__is_authenticated:
            print("Not authenticated.")
            return None
        return self.__account.balance

    @property
    def transactions(self) -> Optional[List[str]]:
        if not self.__is_authenticated:
            print("Not authenticated.")
            return None
        return self.__account.transactions

    @property
    def card_number(self) -> str:
        return self.__card_number

    @property
    def unique_id(self) -> Optional[str]:
        if not self.__is_authenticated:
            print("Not authenticated.")
            return None
        return self.__unique_id

    @property
    def owner(self) -> str:
        return f"{self.__name} {self.__surname}"

class BankAccount:
    def __init__(self, name: str, surname: str, account_number: str, balance: int = 0, transactions: Optional[List[str]] = None):
        self.__name = name
        self.__surname = surname
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = transactions if transactions is not None else []
        self.__cards: Dict[str, BankCard] = {}

    def add_card(self, card: BankCard):
        self.__cards[card.card_number] = card

    def remove_card(self, card_number: str):
        if card_number in self.__cards:
            del self.__cards[card_number]

    @property
    def cards(self) -> List[BankCard]:
        return list(self.__cards.values())

    def deposit(self, amount: int, card_number: Optional[str] = None) -> bool:
        if amount > 0:
            self.__balance += amount
            if card_number:
                self.__transactions.append(f"Deposit: +${amount} (card {card_number})")
            else:
                self.__transactions.append(f"Deposit: +${amount}")
            return True
        return False

    def withdraw(self, amount: int, card_number: Optional[str] = None) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            if card_number:
                self.__transactions.append(f"Withdrawal: -${amount} (card {card_number})")
            else:
                self.__transactions.append(f"Withdrawal: -${amount}")
            return True
        return False

    def transfer(self, other_account: "BankAccount", amount: int) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Transfer to {other_account.account_number}: -${amount}")
            other_account.__balance += amount
            other_account.__transactions.append(f"Transfer from {self.account_number}: +${amount}")
            return True
        return False

    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def owner(self) -> str:
        return f"{self.__name} {self.__surname}"

    @property
    def transactions(self) -> List[str]:
        return self.__transactions.copy()

    def generate_statement(self):
        print(f"Account: {self.owner} [{self.account_number}]")
        print(f"Balance: ${self.balance}")
        transactions = self.transactions
        if transactions:
            for transaction in transactions:
                print(transaction)
        else:
            print(f"No transactions for account {self.account_number}")
        if self.__cards:
            print("Linked cards:")
            for card in self.__cards.values():
                print(f"- {card.owner}, Card #{card.card_number}")

    def clear_transactions(self):
        self.__transactions.clear()

def main():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    card_num = input("Enter card number (16 digits): ")
    cvv = input("Enter CVV (3 or 4 digits): ")
    user_pin = input("Set PIN (will be used to authenticate): ")

    try:
        account = BankAccount(name, surname, "ACC1234567", 1000)
        card = BankCard(account, name, surname, card_num, cvv, user_pin)
    except ValueError as e:
        print(f"Initialization error: {e}")
        return

    authenticated = False
    while not authenticated and card.can_attempt():
        pin = input("Enter PIN: ")
        authenticated = card.make_action(pin)

    if not authenticated:
        print("Access denied.")
        return

    account.add_card(card)

    card.deposit(100)
    card.withdraw(50)
    balance = card.balance
    if balance is not None:
        print("Card balance:", balance)
    transactions = card.transactions
    if transactions is not None:
        print("Card transactions:", transactions)
    card.exit()

    account.deposit(200)
    account.withdraw(100)
    account.generate_statement()

if __name__ == "__main__":
    main()
