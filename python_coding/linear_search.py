def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example Usage
input_list = list(map(int, input("Enter the list elements separated by spaces: ").split()))
target_element = int(input("Enter the element to search: "))

result = linear_search(input_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
