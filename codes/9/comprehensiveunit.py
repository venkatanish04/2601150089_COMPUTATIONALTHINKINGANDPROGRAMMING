import pytest

from hypothesis import given, strategies as st

from bank import Bank, BankAccount


# =========================================================
# FIXTURE
# =========================================================

@pytest.fixture
def account() -> BankAccount:
    return BankAccount(
        account_number=1001,
        holder_name="Anish",
        balance=1000.0
    )


@pytest.fixture
def bank() -> Bank:
    bank = Bank()

    bank.create_account(
        1001,
        "Anish",
        1000.0
    )

    bank.create_account(
        1002,
        "Venkat",
        500.0
    )

    return bank


# =========================================================
# UNIT TESTS - DEPOSIT
# =========================================================

def test_deposit(account: BankAccount) -> None:
    account.deposit(500)

    assert account.balance == 1500


def test_multiple_deposits(account: BankAccount) -> None:
    account.deposit(100)
    account.deposit(200)

    assert account.balance == 1300


def test_deposit_zero(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.deposit(0)


def test_deposit_negative(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.deposit(-100)


# =========================================================
# UNIT TESTS - WITHDRAW
# =========================================================

def test_withdraw(account: BankAccount) -> None:
    account.withdraw(300)

    assert account.balance == 700


def test_withdraw_entire_balance(account: BankAccount) -> None:
    account.withdraw(1000)

    assert account.balance == 0


def test_withdraw_more_than_balance(
    account: BankAccount
) -> None:

    with pytest.raises(ValueError):
        account.withdraw(2000)


def test_withdraw_zero(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.withdraw(0)


def test_withdraw_negative(account: BankAccount) -> None:
    with pytest.raises(ValueError):
        account.withdraw(-100)


# =========================================================
# PARAMETERIZED TEST
# =========================================================

@pytest.mark.parametrize(
    "amount, expected",
    [
        (100, 1100),
        (200, 1200),
        (500, 1500),
        (1000, 2000),
    ]
)
def test_deposit_multiple_values(
    account: BankAccount,
    amount: float,
    expected: float
) -> None:

    account.deposit(amount)

    assert account.balance == expected


# =========================================================
# HYPOTHESIS PROPERTY-BASED TESTS
# =========================================================

@given(
    st.floats(
        min_value=0.01,
        max_value=100000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_deposit_preserves_balance(
    amount: float
) -> None:

    account = BankAccount(
        account_number=1,
        holder_name="Test",
        balance=1000.0
    )

    old_balance = account.balance

    account.deposit(amount)

    assert account.balance == old_balance + amount


@given(
    st.floats(
        min_value=0.01,
        max_value=1000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_withdraw_decreases_balance(
    amount: float
) -> None:

    account = BankAccount(
        account_number=1,
        holder_name="Test",
        balance=1000.0
    )

    old_balance = account.balance

    account.withdraw(amount)

    assert account.balance == old_balance - amount


# =========================================================
# INTEGRATION TEST - ACCOUNT CREATION
# =========================================================

def test_create_account(bank: Bank) -> None:

    account = bank.get_account(1001)

    assert account.account_number == 1001
    assert account.holder_name == "Anish"
    assert account.balance == 1000


# =========================================================
# INTEGRATION TEST - ACCOUNT TRANSFER
# =========================================================

def test_transfer(bank: Bank) -> None:

    bank.transfer(
        sender=1001,
        receiver=1002,
        amount=300
    )

    sender = bank.get_account(1001)
    receiver = bank.get_account(1002)

    assert sender.balance == 700
    assert receiver.balance == 800


# =========================================================
# INTEGRATION TEST - INVALID TRANSFER
# =========================================================

def test_transfer_insufficient_balance(
    bank: Bank
) -> None:

    with pytest.raises(ValueError):

        bank.transfer(
            sender=1002,
            receiver=1001,
            amount=1000
        )


# =========================================================
# INTEGRATION TEST - DUPLICATE ACCOUNT
# =========================================================

def test_duplicate_account(bank: Bank) -> None:

    with pytest.raises(ValueError):

        bank.create_account(
            1001,
            "Another User",
            500
        )


# =========================================================
# INTEGRATION TEST - UNKNOWN ACCOUNT
# =========================================================

def test_unknown_account(bank: Bank) -> None:

    with pytest.raises(ValueError):
        bank.get_account(9999)