
def swap (lis, idx1, idx2):
    temp = lis[idx1]
    lis[idx1] = lis[idx2]
    lis[idx2] = temp   


def pivot(lis, pivot_index, end_index):
    swap_idx  = pivot_index
    for idx  in range(pivot_index + 1, end_index + 1):
        if lis[idx] < lis[pivot_index]:
            swap_idx += 1
            swap(lis, swap_idx, idx)
    swap(lis, pivot_index, swap_idx)
    return swap_idx


def quick_sort_helper(lis, left , right):
    if left < right:
        pivot_index = pivot(lis, left , right)
        quick_sort_helper(lis, left , pivot_index-1)
        quick_sort_helper(lis, pivot_index+1 , right)
    return lis


def quick_sort(lis):
    return quick_sort_helper(lis, 0, len(lis) -1)

from dummy_data import ten_ten
print(quick_sort(ten_ten))