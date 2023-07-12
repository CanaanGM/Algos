def merge(listA, listB):
    combined_list = []

    a_list_pointer = 0
    b_list_pointer = 0

    while (
        a_list_pointer < len(listA)
        and b_list_pointer < len(listB)
    ):
        if listA[a_list_pointer] < listB[b_list_pointer]:
            combined_list.append(listA[a_list_pointer])
            a_list_pointer += 1
        else:
            combined_list.append(listB[b_list_pointer])
            b_list_pointer += 1

    while a_list_pointer < len(listA):
        combined_list.append(listA[a_list_pointer])
        a_list_pointer += 1

    while b_list_pointer < len(listB):
        combined_list.append(listB[b_list_pointer])
        b_list_pointer += 1

    return combined_list

def merge_sort(arr):
    
    if len(arr) == 1:
        return arr
    
    mid_idx = int(len(arr) /2)
    left = merge_sort(arr[:mid_idx])
    right = merge_sort(arr[mid_idx:])
    return merge(left, right)

from dummy_data import ten_ten


print(merge_sort(ten_ten))