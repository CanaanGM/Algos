#include <iostream>


def greedy_approach(array:list[int]) -> int:
    """
    
    """
    answer:int = array[1]
    current_sum:int = 0
    holder = []
    for number in array[1:]:
        current_sum += number
        if current_sum > answer:
            answer = current_sum
        if current_sum < 0:
            current_sum = 0;
    return answer

def partial_sum(array:list[int]) -> int:
    partial_sum = [0] * (len(array) +1) # adding an extra index so no outta bounds
    for idx in range(len(array)):
        partial_sum[idx+1] = partial_sum[idx] + array[idx]

    upper_max = partial_sum[-1]
    res = 0

    for i in range(len(partial_sum) -2, -1, -1):
        upper_max = max(upper_max, partial_sum[i+1])
        res = max(res or upper_max-partial_sum[i], upper_max-partial_sum[i])
    return res
 
if __name__ == "__main__":
    dummy_list = [3, -1, 2, -1, 3]  #[5, -6, 3, 4, -2, 3, -3] # max sub array is 8
    #print(greedy_approach(dummy_list))
    print(partial_sum(dummy_list))