def item_in_common(lisA, lisB) -> bool :
    
    items_from_lisA = { k:i for k,i in zip(lisA, range(len(lisA))) }
    
    for num in lisB:
        if num in items_from_lisA.keys():
            return True
    return False
    

list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))