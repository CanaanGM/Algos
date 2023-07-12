def find_longest_string(string_list):
    
    _max = len(string_list[0])
    res = ""
    for string in string_list:
        if len(string) > _max:
           res = string
    return res


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""