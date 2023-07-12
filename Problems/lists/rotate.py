def rotate(array, steps):
    """
    shifts the elements in the array depending on the steps provided
       [1, 2, 3, 4, 5, 6, 7], k = 3 
    -> [5, 6, 7, 1, 2, 3, 4] 
    """
    
    steps = steps % len(array)
    
    array[:] = array[-steps:] + array[:-steps]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""