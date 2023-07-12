def find_max_min(arr):
    """ travereses the list and returns a Tuble<MAX, MIN> """

    _max = 0
    _min = 1
    
    for number in arr:
        if number > _max:
            _max = number
        if number < _min:
            _min = number
    return (_max, _min)
print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""