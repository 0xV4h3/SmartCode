from typing import List

class BankAccount:
    def __init__(self, account_number: str, balance: int = 0, transactions: List[str] = None):
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = transactions if transactions is not None else []

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposit: +${amount}")
            return True
        return False

    def withdraw(self, amount: int) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawal: -${amount}")
            return True
        return False

    def transfer(self, other_account: "BankAccount", amount: int) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(
                f"Transfer to {other_account.get_account_number()}: -${amount}"
            )
            other_account.__balance += amount
            other_account.__transactions.append(
                f"Transfer from {self.get_account_number()}: +${amount}"
            )
            return True
        return False

    def get_balance(self) -> int:
        return self.__balance

    def get_account_number(self) -> str:
        return self.__account_number

    def get_transactions(self) -> List[str]:
        return self.__transactions.copy()

    def generate_statement(self):
        print(f"Balance: ${self.get_balance()}")
        transactions = self.get_transactions()
        if transactions:
            for transaction in transactions:
                print(transaction)
        else:
            print(f"User {self.__account_number} has no transactions")

    def clear_transactions(self):
        self.__transactions.clear()
