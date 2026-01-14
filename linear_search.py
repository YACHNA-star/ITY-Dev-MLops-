def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   
    return -1        
nums = [10, 25, 7, 42, 3]
print(linear_search(nums, 42))   # Output: 3

