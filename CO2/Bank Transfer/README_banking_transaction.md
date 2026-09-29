# Banking Transaction System Using PEP 484 Type Hints

## Scenario

A banking system processes transactions such as **deposit** and **withdrawal**. Developers want to reduce programming errors by using **static type checking**.

PEP 484-style type hints are applied to the transaction function to specify the expected types of its parameters and return value.

## Objective

Apply PEP 484-style type hints to a banking transaction function so that:

- `account_balance` is a `float`
- `amount` is a `float`
- `transaction_type` is a `str`
- The function returns a `float`

## Example

A customer has an account balance of `10000.0` and wants to withdraw `2500.0`.

The transaction function checks the transaction type and updates the account balance.

## Algorithm

1. Start.
2. Define a `transaction()` function with PEP 484 type hints.
3. Accept `account_balance`, `amount`, and `transaction_type`.
4. Check whether the transaction type is `"deposit"` or `"withdraw"`.
5. If it is a deposit, add the amount to the balance.
6. If it is a withdrawal:
   - Check whether sufficient balance is available.
   - If sufficient, subtract the amount.
   - Otherwise, display `"Insufficient balance"`.
7. If the transaction type is invalid, display `"Invalid transaction type"`.
8. Return the updated balance.
9. Display the updated balance.
10. Stop.

## Python Code

```python
def transaction(account_balance: float,
                amount: float,
                transaction_type: str) -> float:

    if transaction_type == "deposit":
        account_balance += amount

    elif transaction_type == "withdraw":
        if amount <= account_balance:
            account_balance -= amount
        else:
            print("Insufficient balance")

    else:
        print("Invalid transaction type")

    return account_balance


balance: float = 10000.0
amount: float = 2500.0
transaction_type: str = "withdraw"

balance = transaction(balance, amount, transaction_type)

print("Updated Balance:", balance)
```

## Output

```text
Updated Balance: 7500.0
```

## Explanation of PEP 484 Type Hints

The function is defined as:

```python
def transaction(
    account_balance: float,
    amount: float,
    transaction_type: str
) -> float:
```

- `account_balance: float` — account balance should be a floating-point value.
- `amount: float` — transaction amount should be a floating-point value.
- `transaction_type: str` — transaction type should be a string.
- `-> float` — the function is expected to return a floating-point value.

## Advantages

1. **Early error detection** — static type checkers can identify incorrect argument types before execution.
2. **Better readability** — developers can immediately understand what types a function expects.
3. **Improved maintainability** — type information makes larger banking applications easier to maintain.
4. **Fewer runtime errors** — many type-related mistakes can be detected during development.
5. **IDE support** — editors can provide better code completion and warnings.

## Static Type Checking

A tool such as `mypy` can be used to check the type hints.

Example:

```bash
mypy banking_transaction.py
```

Type hints do not enforce types by themselves at runtime; they provide information that static type checkers and development tools can use.

## Time Complexity

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

The transaction performs a fixed number of operations regardless of the account balance or transaction amount.
