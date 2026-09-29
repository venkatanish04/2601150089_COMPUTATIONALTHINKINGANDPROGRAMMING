# Library Book Arrangement using Merge Sort

## Problem Statement

A library receives thousands of books with different accession numbers and needs them arranged in ascending order.

To perform this efficiently, this project uses the **Merge Sort** algorithm.

## Why Merge Sort?

Merge Sort is suitable for large amounts of data because its time complexity is consistently **O(n log n)**.

It uses the **divide-and-conquer** approach:

1. Divide the list into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.
4. The final result is an ascending ordered list.

## Example

1. Divide the array
[105, 23, 78, 12, 56, 9, 101]
              ↓
       [105, 23, 78]    [12, 56, 9, 101]

Divide again:

[105] [23, 78]    [12, 56] [9, 101]

Divide until each part has one element:

[105] [23] [78] [12] [56] [9] [101]
2. Merge in sorted order

Merge:

[23] + [78] → [23, 78]

[12] + [56] → [12, 56]

[9] + [101] → [9, 101]

Now:

[105] [23, 78] [12, 56] [9, 101]

Merge the left side:

[105] + [23, 78]
       ↓
[23, 78, 105]

Merge the right side:

[12, 56] + [9, 101]
          ↓
[9, 12, 56, 101]
3. Final merge
[23, 78, 105] + [9, 12, 56, 101]
```

## Algorithm

```text
MERGE_SORT(arr)

1. If length of arr <= 1:
       return arr

2. Find middle of arr

3. Divide arr into:
       left half
       right half

4. left = MERGE_SORT(left)
5. right = MERGE_SORT(right)

6. Merge left and right in ascending order

7. Return merged list
```

## Python Code

```
def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Find the middle
    mid = len(arr) // 2

    # Divide into two halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge sorted halves
    return merge(left, right)

# Example library accession numbers
books = [105, 23, 78, 12, 56, 9, 101]

print("Before sorting:", books)

sorted_books = merge_sort(books)

print("After sorting:", sorted_books)

```
##Input:
        [105, 23, 78, 12, 56, 9, 101]

##Output:
        [9, 12, 23, 56, 78, 101, 105]


        
## Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

**Space Complexity:** O(n)


