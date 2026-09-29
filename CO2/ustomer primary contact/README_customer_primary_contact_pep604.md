# Customer Primary Contact Using PEP 604 Union Type

## 1. Scenario

A banking application stores the **primary contact information** of its customers. A customer may provide either a **mobile number** or an **email address** as their primary contact.

### Example

- **Customer:** Rahul
  - **Primary Contact:** `9876543210`
  - **Contact Type:** Mobile Number

- **Customer:** Priya
  - **Primary Contact:** `priya@gmail.com`
  - **Contact Type:** Email Address

Therefore, the application needs to model the contact information so that it can accept either an integer or a string.

## 2. Objective

Apply the **PEP 604 union type syntax** to represent contact information that can be either:

- `int` → Mobile number
- `str` → Email address

The PEP 604 syntax is:

```python
int | str
```

## 3. Algorithm

1. Start.
2. Define a function to accept the customer's primary contact.
3. Use the PEP 604 union type `int | str` for the contact parameter.
4. Accept either a mobile number or an email address.
5. Store the contact information.
6. Display the primary contact.
7. Stop.

## 4. Python Code

```python
def set_contact(contact: int | str) -> None:
    print("Primary Contact:", contact)


customer1: int | str = 9876543210
customer2: int | str = "priya@gmail.com"

set_contact(customer1)
set_contact(customer2)
```

## 5. Output

```text
Primary Contact: 9876543210
Primary Contact: priya@gmail.com
```

## 6. Explanation

The important part of the program is:

```python
int | str
```

This is the **PEP 604 union type syntax**. It means the variable can contain either an `int` or a `str`.

```python
customer1: int | str = 9876543210
```

Here, the customer provides a mobile number.

```python
customer2: int | str = "priya@gmail.com"
```

Here, the customer provides an email address.

The function:

```python
def set_contact(contact: int | str) -> None:
```

indicates that the `contact` parameter can accept either type.

## 7. PEP 604

Before PEP 604, a union could be written using:

```python
Union[int, str]
```

PEP 604 provides the shorter syntax:

```python
int | str
```

This makes type annotations simpler and easier to read.

**Note:** In a real banking application, phone numbers are often stored as strings because they may contain country codes such as `+91` or leading zeros. The `int | str` representation is used here to demonstrate the requested PEP 604 union type.

## 8. Complexity

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

The program performs a fixed number of operations, so its time and space requirements remain constant.
