from typing import List


def insertion_sort(li : List) -> List:
    for i in range(1, len(li)):
        t = li[i]
        j = i -1
        # reversing the < to > makes it sort in reverse
        while t < li[j] and j > -1:
            li[j + 1] = li[j] 
            li[j] = t
            j -= 1
    return li