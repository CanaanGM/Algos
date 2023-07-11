# Set: Find Pairs ( ** Interview Question)

# You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

# Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.

# Input

# Your function should take in the following inputs:

#     arr1: a list of integers

#     arr2: a list of integers

#     target: an integer


# Output

# Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.


# Example

# Here's an example of what your function should return:

#     arr1 = [1, 2, 3, 4, 5]
#     arr2 = [2, 4, 6, 8, 10]
#     target = 7
     
#     pairs = find_pairs(arr1, arr2, target)
#     print (pairs)
#     # Output: [(5, 2), (3, 4), (1, 6)]


# In this example, the pairs (5, 2) , (3, 4) , and (1, 6) are the only pairs of numbers (one from arr1 and one from arr2) whose sum is 7.



def find_pairs(arr1, arr2, target):
    """
        returns all the pairs that sum up to the target from both arrays
    """
    res = []
    numbers = set(arr1)
    for num in arr2:
        if target - num in numbers:
            res .append((target - num, num))
    return res



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7


# answer = [ (5,2), (3,4), (1,6) ]
pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""


