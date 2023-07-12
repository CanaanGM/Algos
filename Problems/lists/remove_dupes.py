def remove_duplicates(nums):
    """
        replaces the first section of the array with sorted incrementing numbers
    """
    if not nums:
        return 0
 
    write_pointer = 1
 
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
 
    return write_pointer


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [10, 10, 19, 19, 21, 22, 22, 33, 43, 54]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]

"""

#  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] 
 
#  [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]