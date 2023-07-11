# Given an array of integers nums and an integer target,
#  return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.



# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].



from typing import List


def first_two(given_list: List, target: int) -> int :
    for index, number in enumerate( given_list):
        temp = given_list[index]
        number = given_list[index + 1] 

        if  temp + number == target:
            return[
                given_list.index(given_list[index]), 
                given_list.index(number)
            ]
        
    return []
import math

def second_attempt(given_list: List, target: int) -> int :
    """
        {
            9: 1

        }
    """    

    numbers_present = { k:1 for k in given_list  }

    for number in given_list:
        abs_number = abs(number - target)
        if abs_number in numbers_present.keys():
            second_idx = given_list.index(abs_number)
            return [given_list.index(number), second_idx]
        
    return []
        

def after_tea(given_list: List, target: int) -> int :
    """
        {
            9: index

        }
    """    

    numbers_present = { k:i for k, i in zip(given_list, range(0, len(given_list)))  }

    for number in given_list:
        abs_number = abs(number - target)
        if abs_number in numbers_present.keys():
            second_idx = numbers_present[abs_number]
            return [
                 numbers_present[number], 
                 second_idx 
                 ]
        
    return []
        


def actual_solution(given_list, target):
    num_map = {}

    for idx, num in enumerate(given_list):
        compliment = target - num
        if compliment in num_map:
            return [num_map[compliment], idx]
        num_map[num] = idx
    return []

# print(first_two([2,11, 7,15], 9))
# print(second_attempt([2,11, 7,15], 9))
# print(after_tea([2,11, 7,15], 9))

print ( actual_solution([2, 7, 11, 15], 9) )
print ( actual_solution([3, 2, 4], 6) )
print ( actual_solution([3, 3], 6) )
print ( actual_solution([1, 2, 3, 4, 5], 10) )
print ( actual_solution([1, 2, 3, 4, 5], 7) )
print ( actual_solution([1, 2, 3, 4, 5], 3) )
print ( actual_solution([], 0) )