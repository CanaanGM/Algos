from typing import List


def selection_sort(li : List):

    for i in range(len(li) -1 ):
        min_index  = i
        for k in range( i + 1, len(li)):
            if li[k] < li[min_index]:
                min_index = k
        if i != min_index:
            li[i], li[min_index] = li[min_index], li[i]


    return li

from dummy_data import ten_ten
print(selection_sort(ten_ten))