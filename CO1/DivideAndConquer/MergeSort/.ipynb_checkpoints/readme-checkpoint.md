# Project: Student Scholarship Eligibility System (Merge Sort)

An implementation of a stable Merge Sort algorithm in descending order to sort student marks and determine scholarship recipients.

## 1. Problem Statement
Given a database of students with their names and marks:
* Anitha: 95
* Vivek: 83
* Laksmi: 67
* Teja: 97
* Kumar: 85

Sort the list of students in **descending order** of their marks using the **Merge Sort** algorithm, and select the students who are eligible for a scholarship (eligibility threshold: marks $\ge 90$).

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: A stable Merge Sort implementation modified to sort student tuples `(name, marks)` in descending order of marks.
* **Data Store & Input Setup**: Sets up the student database list and scholarship criteria threshold.
* **Sample Edge Cases (Test Cases)**: Conceptual descriptions of tests to verify the sorting logic under different conditions.
* **Driver Logic (Main)**: The interactive console driver that executes the sorting, filters eligible students, and accepts dynamic custom user inputs.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **Student Database**: A list of `(name, marks)` tuples.
- **Scholarship threshold**: The minimum marks required (90).
- **Split and Merge Indexes**: Boundaries (`left`, `right`, `mid`) to track division of subproblems.

### No Needs (Irrelevant Information)
- Student demographic details (roll numbers, address, contact details).
- Enrollment and attendance info.
- Scholarship financial specifics (funding source, award amount).

## 4. Algorithm
1. **Divide**: If the list length is $\le 1$, return it (base case). Otherwise, divide the list into two halves at the midpoint: `mid = len(arr) // 2`.
2. **Conquer**: Recursively apply Merge Sort to the left half and right half.
3. **Combine (Merge)**: Merge the two sorted halves back into a single sorted list in descending order:
   - Compare elements at the pointers of both halves.
   - If the marks of the student in the left half are greater than or equal to the marks of the student in the right half, insert the left student into the temporary list (preserving stability). Otherwise, insert the right student.
   - Copy any remaining students from either half.
4. **Scholarship Filtering**: Traverse the sorted list and select students with `marks >= 90`.

## 5. Core Logic
```text
FUNCTION merge_sort_students(arr)
    IF length of arr <= 1 THEN
        RETURN arr
    END IF

    mid = length of arr / 2
    left_half = sub-array of arr from index 0 to mid
    right_half = sub-array of arr from index mid to end

    left_sorted = merge_sort_students(left_half)
    right_sorted = merge_sort_students(right_half)

    merged = Empty List
    i = 0
    j = 0

    WHILE i < length of left_sorted AND j < length of right_sorted DO
        IF left_sorted[i].marks >= right_sorted[j].marks THEN
            APPEND left_sorted[i] TO merged
            i = i + 1
        ELSE
            APPEND right_sorted[j] TO merged
            j = j + 1
        END IF
    END WHILE

    APPEND remaining elements of left_sorted to merged
    APPEND remaining elements of right_sorted to merged

    RETURN merged
END FUNCTION
```

## 6. Data Store & Input Setup
```text
STUDENTS_DATABASE = [
    ("Anitha", 95),
    ("Vivek", 83),
    ("Laksmi", 67),
    ("Teja", 97),
    ("Kumar", 85)
]

SCHOLARSHIP_THRESHOLD = 90
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Student List (Provided Example)
* **Input**: `[("Anitha", 95), ("Vivek", 83), ("Laksmi", 67), ("Teja", 97), ("Kumar", 85)]`
* **Expected Sorted List**: `[("Teja", 97), ("Anitha", 95), ("Kumar", 85), ("Vivek", 83), ("Laksmi", 67)]`
* **Expected Scholarship Recipients**: `[("Teja", 97), ("Anitha", 95)]`

### Test Case 2: Empty Student List
* **Input**: `[]`
* **Expected Sorted List**: `[]`
* **Expected Scholarship Recipients**: `[]`

### Test Case 3: Single Student List
* **Input**: `[("Anitha", 95)]`
* **Expected Sorted List**: `[("Anitha", 95)]`
* **Expected Scholarship Recipients**: `[("Anitha", 95)]`

### Test Case 4: None Eligible for Scholarship
* **Input**: `[("Vivek", 83), ("Laksmi", 67)]`
* **Expected Sorted List**: `[("Vivek", 83), ("Laksmi", 67)]`
* **Expected Scholarship Recipients**: `[]`

### Test Case 5: Identical Marks (Stability Verification)
* **Input**: `[("StudentA", 90), ("StudentB", 90)]`
* **Expected Sorted List**: `[("StudentA", 90), ("StudentB", 90)]` (preserving original relative order)

## 8. Driver Logic (Main)
To run the driver logic, open the [MergeSort.ipynb](MergeSort.ipynb) notebook and execute the cells.

## Sample Input and Output

### Interactive Output (Sample Run)
```text
=============================================
        DYNAMIC INPUT / INTERACTIVE MODE
=============================================
Enter scholarship eligibility marks threshold [default: 90]: 90
Enter number of custom students to add [default: 0 to skip to preset database]: 0

Initial Student Database: [('Anitha', 95), ('Vivek', 83), ('Laksmi', 67), ('Teja', 97), ('Kumar', 85)]

Students Sorted in Descending Order of Marks:
  - Teja: 97
  - Anitha: 95
  - Kumar: 85
  - Vivek: 83
  - Laksmi: 67

Scholarship Recipients (Marks >= 90):
  * Teja (97) - ELIGIBLE
  * Anitha (95) - ELIGIBLE
=============================================
```
