# Project: Student Attendance Analysis System

A procedural, function-based student attendance analysis system demonstrating data structures, input validation, and statistical analysis.

## 1. Problem Statement
An educational institution needs a Python-based program to analyze student attendance. The system should accept student name, total classes conducted, and total classes attended. It needs to calculate individual attendance percentages, identify students with attendance below 75%, find the student(s) with the highest attendance, and calculate the overall class attendance metrics.

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: Clean, decoupled functions for attendance record insertion and calculations (`add_student`, `calculate_percentage`).
* **Computational Logic**: Functions for filtering and statistics (`get_low_attendance_students`, `get_highest_attendance_students`, `calculate_overall_attendance`).
* **Data Store & Input Setup**: Defines the student registry data structure representing conducted and attended classes.
* **Driver Logic (Main)**: An interactive console menu loop that drives the operations.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **Student Name**: String used as an identifier.
- **Classes Conducted**: Integer representing the total lectures held for the student.
- **Classes Attended**: Integer representing the number of lectures attended.
- **Attendance Percentage Threshold**: Floating-point threshold (75.0%) for identifying low attendance.

### No Needs (Irrelevant Information)
- Student grades, phone numbers, email addresses, or physical addresses.
- Course codes, names of professors, schedules, or classroom locations.
- System logs, login passwords, or UI styling.

## 4. Algorithm
1. Initialize an empty dictionary `student_db` to store student records.
2. Accept choice input from the user (1-6):
   - Option 1 (Add Student Record): Prompt for Name, Conducted classes, and Attended classes. Validate inputs (Name not empty, Conducted $> 0$, $0 \le \text{Attended} \le \text{Conducted}$). Store the record.
   - Option 2 (View Attendance Report): For each student, compute attendance percentage and print in a formatted table.
   - Option 3 (Identify Low Attendance): Filter and print students with attendance percentage $< 75.0\%$.
   - Option 4 (Find Highest Attendance): Find the maximum attendance percentage and list all students matching that value (handling ties).
   - Option 5 (Calculate Overall Metrics): Calculate the simple average of individual percentages, and the overall aggregate attendance rate ($\frac{\sum \text{Attended}}{\sum \text{Conducted}} \times 100$).
   - Option 6 (Exit): Terminate the program.

## 5. Core Logic
```python
def add_student(student_db, name, conducted, attended):
    name = name.strip()
    if not name:
        raise ValueError("Student name cannot be empty.")
    if conducted <= 0:
        raise ValueError("Total conducted classes must be greater than zero.")
    if attended < 0:
        raise ValueError("Total attended classes cannot be negative.")
    if attended > conducted:
        raise ValueError("Attended classes cannot exceed conducted classes.")
    student_db[name] = {"conducted": conducted, "attended": attended}

def calculate_percentage(conducted, attended):
    if conducted == 0:
        return 0.0
    return (attended / conducted) * 100.0

def get_low_attendance_students(student_db, threshold=75.0):
    low_list = []
    for name, info in student_db.items():
        pct = calculate_percentage(info["conducted"], info["attended"])
        if pct < threshold:
            low_list.append((name, pct))
    return low_list

def get_highest_attendance_students(student_db):
    if not student_db:
        return []
    max_pct = -1.0
    highest_list = []
    for name, info in student_db.items():
        pct = calculate_percentage(info["conducted"], info["attended"])
        if pct > max_pct:
            max_pct = pct
            highest_list = [(name, pct)]
        elif pct == max_pct:
            highest_list.append((name, pct))
    return highest_list

def calculate_overall_attendance(student_db):
    if not student_db:
        return {"average_percentage": 0.0, "overall_rate": 0.0}
    total_pct_sum = 0.0
    total_conducted = 0
    total_attended = 0
    for name, info in student_db.items():
        pct = calculate_percentage(info["conducted"], info["attended"])
        total_pct_sum += pct
        total_conducted += info["conducted"]
        total_attended += info["attended"]
    return {
        "average_percentage": total_pct_sum / len(student_db),
        "overall_rate": (total_attended / total_conducted) * 100.0 if total_conducted > 0 else 0.0
    }
```

## 6. Data Store & Input Setup
```python
student_db = {
    "Aravind": {"conducted": 40, "attended": 32},
    "Bhavana": {"conducted": 40, "attended": 38},
    "Chaitanya": {"conducted": 45, "attended": 30}
}
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Verification
* **Input**: "Alice" with 50 conducted and 40 attended (80.0%), "Bob" with 50 conducted and 35 attended (70.0%).
* **Expected Output**: Alice percentage = 80.0%, Bob percentage = 70.0%. Bob identified as below 75%.

### Test Case 2: Zero Attendance
* **Input**: "Charlie" with 20 conducted and 0 attended.
* **Expected Output**: percentage = 0.0%. Identified as below 75%.

### Test Case 3: Perfect Attendance
* **Input**: "Diana" with 30 conducted and 30 attended.
* **Expected Output**: percentage = 100.0%.

### Test Case 4: Invalid Input Validations
* **Input**: "Eva" with conducted = -5, or attended = 15 when conducted = 10.
* **Expected Output**: System rejects input, raises `ValueError`, and prompts user to re-enter correctly.

### Test Case 5: Multiple Students Tie for Highest Attendance
* **Input**: Alice (80%), Diana (100%), Eric (100% - conducted 40, attended 40).
* **Expected Output**: Highest attendance shows both Diana and Eric at 100.0%.

## 8. Driver Logic (Main)
To run the driver logic, open the [AttendanceAnalyzer.ipynb](AttendanceAnalyzer.ipynb) notebook and execute the cells.

## Sample Input and Output

### Interactive Dynamic Input Output (Sample Run)
```text
--- STUDENT ATTENDANCE MENU ---
1. Add Student Record
2. View Attendance Report
3. Find Students Below 75% (Low Attendance)
4. Find Student(s) with Highest Attendance
5. Calculate Overall Class Attendance
6. Exit
Enter choice (1-6): 2
-----------------------------------------------------------------
Student Name         Conducted  Attended   Percentage   Status    
-----------------------------------------------------------------
Aravind              40         32         80.00%       Good      
Bhavana              40         38         95.00%       Good      
Chaitanya            45         30         66.67%       Low (<75%)
-----------------------------------------------------------------
```. 
