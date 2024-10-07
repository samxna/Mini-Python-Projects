# Samina Ahmed | 220023354 | 04/2023
# IN0007 Lab 2 Assessment | Q5 Bubble Sort

def bubble_sort(input_list):
    # To get the length of the list
    n = len(input_list)

    # Perform n-1 iterations of the bubble sort algorithm
    for i in range(n-1):
        # At each iteration, compare adjacent elements and 
        # swap them if they are in the wrong order
        for j in range(n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

    # Return the sorted list
    return input_list

List = [0, 14, 3, 21, 1, 8, 60, 45, 30]
sorted_list = bubble_sort(List)
print("\nSorted list: ", sorted_list)


# Now we can take the sorted list and define how to find a target number
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Search for number 15 in the list
result_a = binary_search(sorted_list, 15)
print("\nIs 15 in the list? ", result_a)

# Search for number 30 in the list
result_b = binary_search(sorted_list, 30)
print("Is 30 in the list? ", result_b)


