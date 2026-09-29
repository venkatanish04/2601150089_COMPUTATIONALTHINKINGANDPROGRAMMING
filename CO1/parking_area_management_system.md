# Parking Area Management System

A Python-based parking management system for a parking area containing **100 parking slots**.

## Features

The system can:

- Show available parking slots
- Allocate a parking slot to a vehicle
- Release a slot when a vehicle leaves
- Calculate parking charges
- Display all parked vehicles
- Find a vehicle and its slot
- Identify whether the parking area is full
- Validate user input

## Parking Charges

The program uses the following pricing:

- First hour: **₹30**
- Every additional hour: **₹20 per hour**

For example, for 3 hours:

```text
₹30 + (2 × ₹20) = ₹70
```

### 1. Parking Slots

The parking area contains 100 slots:

```python
TOTAL_SLOTS = 100
```

Each slot initially has no vehicle:

```text
Slot 1   -> Available
Slot 2   -> Available
Slot 3   -> Available
...
Slot 100 -> Available
```

### 2. Show Availability

The system displays:

- Total slots
- Occupied slots
- Available slots
- Available slot numbers

Example:

```text
========== PARKING AVAILABILITY ==========
Total Slots    : 100
Occupied Slots : 3
Available Slots: 97

Available Slot Numbers:
[4, 5, 6, 7, ...]
===========================================
```

### 3. Allocate a Slot

When a vehicle enters, the system asks for its vehicle number.

Example:

```text
Enter vehicle number: AP39AB1234
```

The system automatically assigns the first available slot:

```text
========== SLOT ALLOCATED ==========
Vehicle Number : AP39AB1234
Parking Slot   : 1
====================================
```

### 4. Release a Slot

When the vehicle leaves, the user enters the vehicle number:

```text
Enter vehicle number leaving: AP39AB1234
Enter number of hours parked: 3
```

The system calculates the charge and releases the slot:

```text
========== VEHICLE EXIT ==========
Vehicle Number : AP39AB1234
Parking Slot   : 1
Hours Parked   : 3.00
Parking Charge : ₹70.00
Slot Released Successfully.
==================================
```

Slot 1 is then available for another vehicle.

### 5. Parking Full Check

The system checks whether all 100 slots are occupied.

If all slots are occupied:

```text
PARKING AREA IS FULL!
No parking slots are available.
```

Otherwise:

```text
Parking is not full.
Available slots: 25
```

### 6. Find a Vehicle

The user can search for a currently parked vehicle:

```text
Enter vehicle number to search: AP39AB1234

========== VEHICLE FOUND ==========
Vehicle Number : AP39AB1234
Parking Slot   : 1
===================================
```

## Main Menu

When the program starts, it displays:

```text
========================================
       PARKING AREA MANAGEMENT SYSTEM
========================================
1. Show Parking Availability
2. Allocate Slot to Vehicle
3. Release Slot / Vehicle Exit
4. Show Parked Vehicles
5. Find Vehicle
6. Check if Parking is Full
7. Exit
========================================
```

## Python Concepts Used

This project demonstrates:

- Variables
- Dictionaries
- Lists
- Functions
- `if`, `elif`, and `else`
- `for` loops
- `while` loops
- `input()`
- String formatting
- Exception handling using `try` and `except`
- Data validation
- Basic data management

## Data Structures

The parking slots are stored in a dictionary:

```python
parking_slots = {
    1: None,
    2: None,
    3: None,
    # ...
    100: None
}
```

The `None` value means that the slot is available.

When a vehicle is allocated:

```python
parking_slots[1] = "AP39AB1234"
```

The vehicle information is also stored separately:

```python
vehicles = {
    "AP39AB1234": {
        "slot": 1
    }
}
```

## Project Flow

```text
Start
  |
  v
Display Main Menu
  |
  +--> View Availability
  |
  +--> Allocate Vehicle
  |
  +--> Release Vehicle
  |       |
  |       +--> Enter Hours
  |       +--> Calculate Charge
  |       +--> Release Slot
  |
  +--> View Parked Vehicles
  |
  +--> Find Vehicle
  |
  +--> Check Parking Full
  |
  +--> Exit
```

## Example

Suppose the following vehicles enter:

```text
AP39AB1234
TS08CD5678
KA01EF9012
```

They receive:

```text
Slot 1 -> AP39AB1234
Slot 2 -> TS08CD5678
Slot 3 -> KA01EF9012
```

If `AP39AB1234` leaves after 4 hours:

```text
First hour       = ₹30
Additional hours = 3 × ₹20
Total            = ₹90
```

Slot 1 becomes available again:

```text
Slot 1 -> Available
Slot 2 -> TS08CD5678
Slot 3 -> KA01EF9012
```
