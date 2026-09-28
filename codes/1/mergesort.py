# Merge Sort using Divide and Conquer

def merge_sort(arr):
    # Base condition
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements from both arrays
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


# Main program
n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

print("Original Array:", arr)

sorted_arr = merge_sort(arr)

print("Sorted Array:", sorted_arr)

print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")
print("Space        : O(n)")