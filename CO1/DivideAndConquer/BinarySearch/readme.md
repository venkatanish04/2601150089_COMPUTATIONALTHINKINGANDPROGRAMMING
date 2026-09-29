# Project: University Library Book Search (Binary Search)

An efficient search implementation to find a book in a sorted database of 10 lakh books.

## 1. Problem Statement
A university library has 1,000,000 (10 lakhs) books arranged in increasing order (e.g., 1, 2, ..., 1,000,000). A student wants to find book number `750000`. Using Binary Search, the system should find and return the exact index/location of this book if present, or output that the book was "Not Found".

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: A clean, decoupled function containing the primary binary search logic.
* **Data Store & Input Setup**: Sets up the book list database (simulating 10 lakh sorted book IDs) and query parameters.
* **Sample Edge Cases (Test Cases)**: Conceptual descriptions of tests to verify the search logic under extreme conditions.
* **Driver Logic (Main)**: The interactive console driver that accepts dynamic user inputs and runs search queries.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **List of Book IDs**: A sorted collection of book IDs.
- **Target Book ID**: The specific book ID to search for (`750000`).
- **Control Pointers**: Indices (`low`, `high`, `mid`) to track and halve the search space.

### No Needs (Irrelevant Information)
- Book details (titles, authors, cover design, page counts).
- Physical attributes (shelf rack numbers, library floor).
- Student info (borrower ID, checkout history).

## 4. Algorithm
1. Initialize two pointers: `low = 0` and `high = len(books) - 1`.
2. While `low <= high`:
   a. Compute middle index: `mid = low + (high - low) // 2`.
   b. Compare the element at `mid` with the target:
      - If `books[mid] == target`, return `mid` (Found).
      - If `books[mid] < target`, set `low = mid + 1` (Discard lower half).
      - If `books[mid] > target`, set `high = mid - 1` (Discard upper half).
3. If the loop terminates without finding the target, return `-1` (Not Found).

## 5. Core Logic
```text
FUNCTION binary_search_books(books, target_id)
    low = 0
    high = length of books - 1
    
    WHILE low <= high DO
        mid = low + (high - low) / 2
        IF books[mid] equals target_id THEN
            RETURN mid
        ELSE IF books[mid] < target_id THEN
            low = mid + 1
        ELSE
            high = mid - 1
        END IF
    END WHILE
    
    RETURN -1
END FUNCTION
```

## 6. Data Store & Input Setup
```text
BOOKS_DATABASE = Array of integers from 1 to 1000000
DEFAULT_TARGET = 750000
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Search (Book Found)
* **Input**:
  * `books` = [1, 2, 3, ..., 1000000]
  * `target` = 750000
* **Expected Output**: Book 750000 found at index 749999 (Position 750000)

### Test Case 2: Standard Search (Book Not Found)
* **Input**:
  * `books` = [1, 2, 3, ..., 1000000]
  * `target` = 1500000
* **Expected Output**: Book 1500000 not found (return -1)

### Test Case 3: Empty Database
* **Input**:
  * `books` = []
  * `target` = 5
* **Expected Output**: Book 5 not found (return -1)

### Test Case 4: Single Book Database (Match)
* **Input**:
  * `books` = [42]
  * `target` = 42
* **Expected Output**: Book 42 found at index 0 (Position 1)

### Test Case 5: Single Book Database (No Match)
* **Input**:
  * `books` = [42]
  * `target` = 10
* **Expected Output**: Book 10 not found (return -1)

### Test Case 6: Target at Lower Boundary
* **Input**:
  * `books` = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  * `target` = 1
* **Expected Output**: Book 1 found at index 0 (Position 1)

### Test Case 7: Target at Upper Boundary
* **Input**:
  * `books` = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  * `target` = 10
* **Expected Output**: Book 10 found at index 9 (Position 10)

## 8. Driver Logic (Main)
To run the driver logic, open the [BinarySearch.ipynb](BinarySearch.ipynb) notebook and execute the cells.

## Sample Input and Output

### Interactive Dynamic Input Output (Sample Run)
```text
=============================================
        DYNAMIC INPUT / INTERACTIVE MODE
=============================================
Enter the total number of books in the library [default: 1000000]: 1000000
Generating sorted library of 1000000 books (IDs 1 to 1000000)...
Enter the book ID to search for (1 to 1000000) [default: 750000]: 750000
Searching for book 750000 using Binary Search...

SUCCESS: Book 750000 found at index 749999 (Position 750000 in the sorted list).
=============================================
```
