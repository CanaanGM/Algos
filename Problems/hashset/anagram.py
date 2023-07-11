# HT: Group Anagrams ( ** Interview Question)

# You have been given an array of strings, where each string may contain only lowercase English letters. 
# You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). 
# The function should return a list of lists, where each inner list contains a group of anagrams.

# For example,
#  if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], t
# he function should return [["eat","tea","ate"],["tan","nat"],["bat"]] 
# because the first three strings are anagrams of each other, the next two strings are anagrams of each other,
#  and the last string has no anagrams in the input array.

# You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.



def group_anagrams(string_list) :
    """
        takes in a list of strings, grtoups up the similar words in length and chars
        then returns them
    """

    words = {}

    for word in string_list:
        sorted_word = ''.join(sorted(word))

        if sorted_word in words:
            words[sorted_word].append(word)
        else:
            words[sorted_word] = [word]
    
    return list(words.values())



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""

