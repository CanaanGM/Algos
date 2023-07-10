from typing import List


def bubble_sort(li: List) -> List:
    list_len = len(li)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, list_len):
            if li[i -1 ] > li[i]:
                li[i-1], li[i] = li[i], li[i -1]
                swapped = True
        list_len -= 1

    return li




from dummy_data import hundred_k

bubble_sort(hundred_k)