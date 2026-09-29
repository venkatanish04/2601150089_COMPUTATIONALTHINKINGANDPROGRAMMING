# Banking Database System 

## Scenario

A banking application opens a database connection to update customer transactions. If an exception occurs while the transaction is being processed, the database connection may remain open if it is not handled correctly.

A **context manager** solves this problem by automatically managing the database resource. Python's `with` statement is commonly used for this purpose.

In this example, SQLite is used because it is built into Python and does not require a separate database server.

---

## (a) How does a context manager solve the problem? 

A context manager manages resources such as database connections automatically. It ensures that the resource is properly handled and released after the `with` block finishes, even when an exception occurs.

The `with` statement makes resource management safer because the programmer does not have to remember to close the connection manually.

---

## (b) Database operation using the `with` statement 

Example:

```python
import sqlite3

try:
    with sqlite3.connect("bank.db") as connection:
        cursor = connection.cursor()

        cursor.execute('''
            UPDATE customers
            SET balance = balance + ?
            WHERE customer_id = ?
        ''', (1000, 1))

        print("Transaction successful!")

except Exception as e:
    print("Error:", e)
```

Here, the database connection is managed by the context manager.

---

## (c) What happens when an exception occurs? 

If an exception occurs inside the `with` block:

1. Python exits the `with` block.
2. The SQLite connection context manager rolls back the pending transaction.
3. The exception is passed to the `except` block if one is present.
4. The connection is closed when the `with` statement finishes.

### Advantage over manual resource management

Context managers reduce the possibility of resource leaks and make code shorter, safer, and easier to maintain. Manual management requires `try`, `except`, and `finally` code to commit/rollback and close the connection.

---

# Algorithm

### Algorithm: Banking Database Transaction Using Context Manager

**Step 1:** Start.

**Step 2:** Open/connect to the SQLite database.

**Step 3:** Enter the database connection using the `with` statement.

**Step 4:** Create a cursor.

**Step 5:** Execute the required banking transaction, such as depositing or withdrawing money.

**Step 6:** If the operation completes successfully, the transaction is committed when the `with` block exits normally.

**Step 7:** If an exception occurs, the transaction is rolled back.

**Step 8:** Exit the `with` block and release/close the database connection.

**Step 9:** Display the result or error message.

**Step 10:** Stop.

---

# Flow of the Algorithm

```text
START
  |
  v
Open Database Connection
  |
  v
Enter `with` Block
  |
  v
Create Cursor
  |
  v
Execute Banking Transaction
  |
  v
Exception?
 /       \
No       Yes
 |         |
 v         v
Commit   Rollback
 \       /
  \     /
   v   v
Exit `with` Block
  |
  v
Connection Automatically Closed
  |
  v
STOP
```

---

# Python Program

Code
```
import sqlite3

# Create/open the SQLite database.
# The with statement manages the connection and transaction.
with sqlite3.connect('bank.db') as connection:
    cursor = connection.cursor()

    # Create the customers table if it does not already exist.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    ''')

    # Add a sample customer only if the ID does not already exist.
    cursor.execute('''
        INSERT OR IGNORE INTO customers (customer_id, name, balance)
        VALUES (?, ?, ?)
    ''', (1, 'Teja', 10000.0))

print('Database and customer table are ready.')

import sqlite3

try:
    with sqlite3.connect('bank.db') as connection:
        cursor = connection.cursor()

        amount = 2000.0
        customer_id = 1

        cursor.execute('''
            UPDATE customers
            SET balance = balance + ?
            WHERE customer_id = ?
        ''', (amount, customer_id))

        print('Transaction successful!')
        print(f'Amount deposited: ₹{amount:.2f}')

except Exception as e:
    print('Transaction failed:', e)

print('Database resource was handled by the context manager.')

# Display the customer's current balance.
with sqlite3.connect('bank.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT customer_id, name, balance FROM customers WHERE customer_id = ?', (1,))
    customer = cursor.fetchone()

print(f'Customer ID: {customer[0]}')
print(f'Name: {customer[1]}')
print(f'Balance: ₹{customer[2]:.2f}')

import sqlite3

# First, record the balance before the failed transaction.
with sqlite3.connect('bank.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT balance FROM customers WHERE customer_id = ?', (1,))
    balance_before = cursor.fetchone()[0]

print(f'Balance before failed transaction: ₹{balance_before:.2f}')

try:
    with sqlite3.connect('bank.db') as connection:
        cursor = connection.cursor()

        # This update is part of the transaction.
        cursor.execute('''
            UPDATE customers
            SET balance = balance - ?
            WHERE customer_id = ?
        ''', (1000.0, 1))

        print('Amount deducted inside the transaction.')

        # Deliberately cause an exception.
        result = 10 / 0

except Exception as e:
    print('Exception occurred:', e)

# Check the balance after the exception.
with sqlite3.connect('bank.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT balance FROM customers WHERE customer_id = ?', (1,))
    balance_after = cursor.fetchone()[0]

print(f'Balance after failed transaction: ₹{balance_after:.2f}')
print('The failed transaction was rolled back, so the ₹1000 deduction was not saved.')
print('The database connection was also cleaned up automatically.')

import sqlite3

connection = sqlite3.connect('bank.db')

try:
    cursor = connection.cursor()

    cursor.execute('''
        UPDATE customers
        SET balance = balance + ?
        WHERE customer_id = ?
    ''', (500.0, 1))

    connection.commit()
    print('Transaction successful!')

except Exception as e:
    connection.rollback()
    print('Error:', e)

finally:
    connection.close()
    print('Connection manually closed.')
    
    
```
The accompanying Jupyter Notebook contains:

1. Creation of the SQLite banking database.
2. Creation of the `customers` table.
3. A successful deposit transaction.
4. Display of the customer's balance.
5. A transaction that deliberately raises an exception.
6. Demonstration of rollback.
7. Comparison with manual database resource management.

## Files

- `Banking_Database_Context_Manager.ipynb` — Complete Python/Jupyter Notebook.
- `README_Banking_Database_System.md` — Scenario, theory, algorithm, flow, and answers for the 8-mark question.

##Time Complexity

| Operation                                 |                                                                      Time Complexity |
| ----------------------------------------- | -----------------------------------------------------------------------------------: |
| Open database connection                  |                                                               **O(1)** approximately |
| Create cursor                             |                                                                             **O(1)** |
| `UPDATE` for a customer using primary key |                                                               **O(1)** approximately |
| `SELECT` customer using primary key       |                                                               **O(1)** approximately |
| Commit/Rollback                           | **O(1)** for this simple example, though actual cost depends on the database/storage |
| Closing connection using context manager  |                                                               **O(1)** approximately |


No external Python package is required because `sqlite3` is part of the Python standard library.
