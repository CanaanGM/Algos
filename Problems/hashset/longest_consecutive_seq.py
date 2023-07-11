# Set: Longest Consecutive Sequence ( ** Interview Question)

# Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

# Use sets to optimize the runtime of your solution.

# Input: An unsorted array of integers, nums.

# Output: An integer representing the length of the longest consecutive sequence in nums.

# Example:


#     Input: nums = [100, 4, 200, 1, 3, 2]
#     Output: 4
#     Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.


def longest_consecutive_sequence(arr1) -> int:
    """
    finds and returns the longest chain of numbers
    """
    arr = set(arr1)
    
    streak = 0

    for num in arr1:
        if  num - 1 not in arr:
            cur_num = num
            curr_streak = 1
            while cur_num + 1 in arr:
                cur_num += 1
                curr_streak += 1
            streak = max(streak, curr_streak)
    return streak


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""