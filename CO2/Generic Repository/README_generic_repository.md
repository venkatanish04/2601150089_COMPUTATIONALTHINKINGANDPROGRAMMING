# Generic Repository for Customer, Product, and Employee

## 1. Scenario

An enterprise application needs repositories for different objects such as **Customer, Product, and Employee**.

Each object requires common repository operations such as:

- Adding an object
- Getting all objects

Instead of creating a separate repository with the same logic for each object, **generic types** can be used to create one reusable repository.

### Random Example

A company has:

- **Customer:** Rahul
- **Product:** Laptop
- **Employee:** Priya

The same repository logic can manage all three:

```text
CustomerRepository → stores customers
ProductRepository  → stores products
EmployeeRepository → stores employees
```

Instead of writing three separate repository classes, we create one generic repository:

```text
Repository[T]
```

Here, `T` represents the type of object being stored.

## 2. Objective

Apply **generic types** to create a reusable repository that can work with:

- `Customer`
- `Product`
- `Employee`

## 3. Algorithm

1. Start.
2. Import `Generic` and `TypeVar`.
3. Create a type variable `T`.
4. Define a generic `Repository[T]` class.
5. Create an empty list to store objects.
6. Create an `add()` method to add objects.
7. Create a `get_all()` method to return all objects.
8. Create `Customer`, `Product`, and `Employee` classes.
9. Create a repository for each object type.
10. Add objects to the appropriate repository.
11. Display the stored objects.
12. Stop.

## 4. Python Code

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items


class Customer:
    def __init__(self, name):
        self.name = name


class Product:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, name):
        self.name = name


customer_repo = Repository[Customer]()
product_repo = Repository[Product]()
employee_repo = Repository[Employee]()

customer_repo.add(Customer("Rahul"))
product_repo.add(Product("Laptop"))
employee_repo.add(Employee("Priya"))

print("Customers:", [c.name for c in customer_repo.get_all()])
print("Products:", [p.name for p in product_repo.get_all()])
print("Employees:", [e.name for e in employee_repo.get_all()])
```

## 5. Output

```text
Customers: ['Rahul']
Products: ['Laptop']
Employees: ['Priya']
```

## 6. Explanation

The important part is:

```python
T = TypeVar("T")
```

`T` represents a type that can be substituted with different classes.

Then:

```python
class Repository(Generic[T]):
```

makes `Repository` a **generic class**.

The same repository can be reused for different types:

```python
Repository[Customer]
Repository[Product]
Repository[Employee]
```

Therefore, the same `add()` and `get_all()` logic works for customers, products, and employees.

## 7. Advantages

1. **Code Reusability** — one repository can handle many object types.
2. **Less Code Duplication** — separate repository classes are not required.
3. **Type Safety** — generic type information helps static type checkers detect incorrect types.
4. **Maintainability** — changes to common repository logic only need to be made in one place.
5. **Scalability** — new object types can use the same repository structure.

## 8. Complexity

- **Add operation:** `O(1)` amortized
- **Get all:** `O(n)`
- **Space Complexity:** `O(n)`

where `n` is the number of objects stored in the repository.
