from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict
@dataclass
class BankAccount(ABC):
    account_number: int
    account_holder: str
    balance: float = 0.0
    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        pass
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        pass
    def get_balance(self) -> float:
        return self.balance
    def display_details(self) -> None:
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance        : ₹{self.balance:.2f}")
@dataclass
class SavingsAccount(BankAccount):
    interest_rate: float = 4.0
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
    def add_interest(self) -> None:
        interest: float = self.balance * self.interest_rate / 100
        self.balance += interest

@dataclass
class CurrentAccount(BankAccount):
    overdraft_limit: float = 5000.0
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
class Bank:
    def __init__(self) -> None:
        self.accounts: Dict[int, BankAccount] = {}
    def add_account(self, account: BankAccount) -> None:
        self.accounts[account.account_number] = account
    def find_account(self, account_number: int) -> BankAccount:
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]
    def deposit(self, account_number: int, amount: float) -> None:
        account: BankAccount = self.find_account(account_number)
        account.deposit(amount)
    def withdraw(self, account_number: int, amount: float) -> None:
        account: BankAccount = self.find_account(account_number)
        account.withdraw(amount)
    def display_account(self, account_number: int) -> None:
        account: BankAccount = self.find_account(account_number)
        account.display_details()
def main() -> None:
    bank: Bank = Bank()
    savings: SavingsAccount = SavingsAccount(
        account_number=1001,
        account_holder="Anish",
        balance=10000.0,
        interest_rate=4.0
    )
    current: CurrentAccount = CurrentAccount(
        account_number=1002,
        account_holder="Venkat",
        balance=15000.0,
        overdraft_limit=5000.0
    )
    bank.add_account(savings)
    bank.add_account(current)
    bank.deposit(1001, 5000)
    bank.withdraw(1001, 2000)
    savings.add_interest()
    bank.deposit(1002, 3000)
    bank.withdraw(1002, 4000)
    print("===== SAVINGS ACCOUNT =====")
    bank.display_account(1001)
    print("\n===== CURRENT ACCOUNT =====")
    bank.display_account(1002)
if __name__ == "__main__":
    main()