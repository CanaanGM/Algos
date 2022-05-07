

def longest_cons_nums_sub_array(array:list[int]) -> int :
    nums = set(array)
    answer = 0
    for n in nums:
        if n-1 not in nums:
            start = n
            while start in nums:
                start += 1
            answer = max(answer, start - n)
    return answer 

if __name__ == "__main__":
    dummy_array = [4, 1,2,3,7,6]
    print(longest_cons_nums_sub_array(dummy_array))