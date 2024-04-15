def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 
        mid_val = arr[mid] 

        if mid_val == key:
            return mid  
        elif mid_val < key:
            low = mid + 1 
        else:
            high = mid - 1 

    return -1 

# Example usage:
sorted_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
key = 17
index = binary_search(sorted_list, key)

if index != -1:
    print("Key", key, "found at index:", index)
else:
    print("Key", key, "not found in the list.")
