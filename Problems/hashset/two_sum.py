# HT: Two Sum ( ** Interview Question)

# two_sum()

# Problem:
# Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

# The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.

# Input:

#     A list of integers nums .

#     A target integer target.

# Output:

#     A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].



def two_sum(given_list, target: int) -> int :
    """
        {
            9: index

        }
    """    

    num_map = {}


    for idx, number in enumerate(given_list):
        complement = target - number
        if complement in num_map:
            return [num_map[complement], idx]
        num_map[number] = idx
        
    return []


print ( two_sum([2, 7, 11, 15], 9) )
print ( two_sum([3, 2, 4], 6) )
print ( two_sum([3, 3], 6) )
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [0, 1]
    [1, 2]
    [0, 1]
    []
    [2, 3]
    [0, 1]
    []

"""