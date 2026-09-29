# Generic Data Store Using PEP 695

## 1. Scenario

A product engineering team is developing a reusable application component for storing different types of data. Instead of creating a separate container for every object type, the team wants to create a generic `DataStore` class.

The same `DataStore` can store different types of values, such as product names and product prices.

PEP 695, introduced in Python 3.12, provides a new syntax for declaring type parameters directly in generic classes, functions, and type aliases.

## 2. Random Example

A product company wants to maintain:

**Product names:**
- Laptop
- Mouse

**Product prices:**
- 55000
- 1200

Instead of creating separate storage classes for names and prices, one generic `DataStore[T]` can store both types.

## 3. Objective

Apply **PEP 695 generic syntax** to create a reusable `DataStore` class that can store values of different types.

## 4. Algorithm

1. Start.
2. Define a generic `DataStore[T]` class using PEP 695 syntax.
3. Create an empty list to store data.
4. Define an `add()` method to insert data.
5. Define a `get_all()` method to retrieve all stored data.
6. Create a `DataStore[str]` for product names.
7. Create a `DataStore[int]` for product prices.
8. Add values to each data store.
9. Display the stored values.
10. Stop.

## 5. Python Code

> Requires Python 3.12 or newer.

```python
class DataStore[T]:
    def __init__(self):
        self.data: list[T] = []

    def add(self, item: T) -> None:
        self.data.append(item)

    def get_all(self) -> list[T]:
        return self.data


products = DataStore[str]()
prices = DataStore[int]()

products.add("Laptop")
products.add("Mouse")

prices.add(55000)
prices.add(1200)

print("Products:", products.get_all())
print("Prices:", prices.get_all())
```

## 6. Output

```text
Products: ['Laptop', 'Mouse']
Prices: [55000, 1200]
```

## 7. Explanation

The main PEP 695 syntax is:

```python
class DataStore[T]:
```

Here, `T` is the type parameter of the generic class.

PEP 695 allows type parameters to be declared directly inside square brackets after the class name. There is no need to separately create a `TypeVar` or inherit from `Generic` for this basic pattern.

When we write:

```python
DataStore[str]()
```

the data store is intended to contain strings.

When we write:

```python
DataStore[int]()
```

the data store is intended to contain integers.

The method:

```python
def add(self, item: T) -> None:
```

uses the same type parameter `T` for the item being added.

The method:

```python
def get_all(self) -> list[T]:
```

returns a list containing values of type `T`.

## 8. Advantages

1. **Reusability** — one class can store different data types.
2. **Type Safety** — static type checkers can identify inappropriate types.
3. **Less Code** — separate classes for each data type are not required.
4. **Maintainability** — common storage logic is implemented only once.
5. **Modern Python Syntax** — PEP 695 provides a simpler way to declare generic type parameters.

## 9. Complexity

- **Add operation:** `O(1)` amortized
- **Get all:** `O(n)`
- **Space Complexity:** `O(n)`

where `n` is the number of items stored in the data store.

## 10. Python Version

This example requires **Python 3.12 or newer**, because PEP 695 was introduced in Python 3.12.

Reference: PEP 695 — Type Parameter Syntax.
