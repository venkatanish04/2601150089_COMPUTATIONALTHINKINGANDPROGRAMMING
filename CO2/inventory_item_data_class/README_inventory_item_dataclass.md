# Inventory Item Using Dataclass

## 1. Scenario

An inventory system stores information about products. Each inventory item has:

- Product ID
- Product Name
- Quantity
- Price

The class mainly stores data and requires little custom initialization logic. Therefore, Python's `@dataclass` is suitable for modeling the inventory item.

## 2. Random Example

Suppose a store has the following product:

- **Product ID:** 101
- **Product Name:** Laptop
- **Quantity:** 25
- **Price:** ₹55,000

The inventory system can represent this product as one `InventoryItem` object.

## 3. Objective

Apply Python's **`@dataclass`** decorator to model an inventory item with product ID, product name, quantity, and price.

## 4. Algorithm

1. Start.
2. Import `dataclass` from the `dataclasses` module.
3. Define an `InventoryItem` dataclass.
4. Declare the product ID, product name, quantity, and price fields.
5. Create an inventory item object.
6. Display the inventory information.
7. Stop.

## 5. Python Code

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    product_id: int
    product_name: str
    quantity: int
    price: float


item = InventoryItem(101, "Laptop", 25, 55000.0)

print(item)
```

## 6. Output

```text
InventoryItem(product_id=101, product_name='Laptop', quantity=25, price=55000.0)
```

## 7. Explanation

The important part is:

```python
@dataclass
class InventoryItem:
```

The `@dataclass` decorator automatically generates useful methods such as `__init__()` and `__repr__()` based on the declared fields.

The fields are:

```python
product_id: int
product_name: str
quantity: int
price: float
```

The object can then be created directly:

```python
item = InventoryItem(101, "Laptop", 25, 55000.0)
```

There is no need to manually write an `__init__()` method for these simple data fields.

## 8. Advantages

1. **Less Code** — no need to manually write `__init__()`.
2. **Easy to Read** — all inventory fields are clearly declared.
3. **Automatic Representation** — `print()` displays a useful representation of the object.
4. **Easy Maintenance** — fields can be added or removed easily.
5. **Suitable for Data Classes** — ideal when a class mainly stores data and has little custom behavior.

## 9. Complexity

- **Object creation:** `O(1)`
- **Field access:** `O(1)`
- **Space Complexity:** `O(1)`

The inventory item contains a fixed number of fields, so these operations take constant time and space.

## 10. Conclusion

The `@dataclass` decorator provides a simple and clean way to model an inventory item. It removes boilerplate initialization code while keeping the class readable and focused on storing product data.

Reference: Python `dataclasses` documentation.
