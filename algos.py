import numpy
from numpy.core.fromnumeric import sort 

class SearchingAlgos:
    def __repr__(self) -> str:
        return "Simple implementation of algos"

    def binary_search(self,sorted_list, target):
        """
            Takes in a Sorted list
            returns None ; !taget
            returns the index of the target
        """

        min = 0 
        max = len(sorted_list) -1 

        while (min <= max):
            mid = (min + max) //2  # middle of the list
            guess = sorted_list[mid]
            if (guess == target):
                return mid
            if (guess > target):
                max = mid - 1 
            if (guess < target):
                min = mid  + 1 
        return -1
    
class SortingAlgos:
    def __repr__(self) -> str:
        return "Simple implementaion of sorting algoritms"

    def bubble_sort(self,unsorted_list:list) -> list :
        """
            Takes in an unsorted list
            returns a sorted version of the same list but sorted
            sorts the bigger values first
            O(n^2)

            finds the biggest value and sorted at the start or the end epending on the comparison
            [1,0,-9,(99),12] -> 99 
            [1,0,-9,(12),99] -> 12
            [(1),0,-9,12,99] -> 1
            [(0),-9,1,12,99] -> 0
            [-9,0,1,12,99] -> goes another loop to check
            [-9,0,1,12,99] -> stops cause we're sorted ~!

        """
        for index, i in enumerate( unsorted_list):
            for jdex, j in enumerate(unsorted_list):
                if unsorted_list[index] > unsorted_list[jdex]: # reverse the comparison to desc/asc
                    temp = unsorted_list[jdex]
                    unsorted_list[jdex] = unsorted_list[index]
                    unsorted_list[index] = temp
                    
        return unsorted_list

    def selection_sort(self, unsorted_list:list) -> list:
        """
            Takes in an unsorted list
            returns a sorted version of the same list but sorted
            normal implementation
            sorts the lower values first 
         finds the lowest value and sorted at the start or the end epending on the comparison
            [1,0,(-9),99,12] -> -9 
            [1,(0),12,99,-9] -> 0
            [(1),12,99,0,-9] -> 1
            [(12),99,1,0,-9] -> 12
            [99,12,1,0,-9] -> goes another loop to check
            [99,12,1,0,-9] -> stops cause we're sorted ~!
        """
        for i in range(len(unsorted_list)):
            for j in range(len(unsorted_list) -i -1 ):
                if unsorted_list[j] > unsorted_list[i + 1]:
                    unsorted_list[j] =  unsorted_list[j+1]
                    unsorted_list[i] =   unsorted_list[j]
        return unsorted_list

    def selection_sort_canaan(self, unsorted_list : list) -> list:
        """
            have an empty array []
            find and save the minimum value of the given array in a var
            append that var to the new array
            remove that var from the old array

            or 

            while the length of the given array != 0 
            find the lowest value and split the array from it i.e: array[:1] ; should update the given array inplace
            like this u lowered the length of the array (no endless looping) and gotten the lowest value

            once done return the sorted array
        """
        return unsorted_list


    def insertion_sort(self, unsorted_list:list) -> list:
        """
        sorts by placing the small values at the start of the list which creates an always sorted left side
        so any new values that comes in can find its place really quickly

        it works by starting from the second value in the list and compares it to its left 
            swaps if the the left is bigger and goes from there

            Builds up the sort by gradually creating a larger left half which is always sorted
            [ 5, (3), 4, 1, 2 ]
            [ 3, 5, (4), 1, 2 ]
            [ 3, 4, 5, (1), 2 ]
            [ 1, 3, 4, 5,(2) ]
            [ 1, 2, 3, 4, 5 ] -> sorted !


        """
        holder : int = 0
        for i in range(1, len(unsorted_list)):
            j = i -1
            holder = unsorted_list[i]
            while j >= 0 and holder < unsorted_list[j]:
                unsorted_list[j] = unsorted_list[j+1]
                j -= 1
            unsorted_list[j+1] = holder
        return unsorted_list

    def merge_sort(self, unsorted_list : list) -> list:
        """
            divides the given array in half
                [6,3,4,5,2,1]
            right           left
            [6,3,4]         [5,2,1]
            right  left     right     left
            [6]    [3,4]    [5]       [2,1]
                right  left         right   left
                [3]    [4]          [2]      [1]
            left and right untill the halved list are one in length
            then u compare both lists and place the lower on the right and the higher on the left
                    
                    [1,2,3,4,5,6]
               [3,4,6]   +     [1,2,5]
             [3,4] + [6]      [2,1] + [5]
            [6]  >  [3,4]   [5]   >   [2,1]           
             [3]  <  [4]       [2]  >  [1]    from here up cause recursion!

        """
        if len(unsorted_list) > 1:
            mid = len(unsorted_list) // 2
            right_side = unsorted_list[mid:]
            left_side = unsorted_list[:mid]
            
            self.merge_sort(right_side)
            self.merge_sort(left_side)

            i=j=k = 0  # i,j,k = 0 will result in exception not enoupg values to unpack

            while i < len(left_side) and j < len(right_side):
                if left_side[i] < right_side[j]:
                    unsorted_list[k] = left_side[i]
                    i += 1
                else:
                    unsorted_list[k] = right_side[j]
                    j += 1
                k += 1

            while i < len(left_side):
                unsorted_list[k] = left_side[i]
                i +=1 
                k +=1

            while j < len(right_side):
                unsorted_list[k] = right_side[j]
                j += 1
                k += 1
        return unsorted_list

    def quick_sort(self,unsorted_list:list, start , end) -> list:
       """
        pick an element and move the numbers less than it to its left and bigger to the right
        [0,3,8,(9),334,6] -> 9
        [0,3,8,6,9,334]

       """
       if len(unsorted_list) == 1:
           return unsorted_list
       if  start < end:
           pivot_index = self._pivot(unsorted_list, start, end)
           self.quick_sort(unsorted_list, start, pivot_index - 1)
           self.quick_sort(unsorted_list, pivot_index +1, end)
       return unsorted_list

    def _pivot(self, arr:list, start:int , end:int) -> int:
        """
        helper for quick_sort, return the index of the pivot 
        """
        pivot = arr[end]
        swap_index = start - 1
        for i in range(start, end):
            if arr[i] <= pivot:
                swap_index += 1
                arr[swap_index] , arr[i] = arr[i], arr[swap_index] # swap the values
        arr[swap_index +1] , arr[end] = arr[end], arr[swap_index +1]
        return swap_index + 1

    def radix_sort(self, unsorted_list:list) -> list:
        """
        takes in an unsorted list. 
        makes 0-9 buckets  [[],[],[],[],[],[],[],[],[] ]
        divide the values from the unsorted list into them on their last number 12(3) this goes to buckets[2] recurivly 

        input : [213,345,576,998,231,34,0,56,12]
        makes the buckets : [[],[],[],[],[],[],[],[],[],[] ] 0 ~ 9 
        divide the values on their Last digit into the buckets
          [21(3),34(5),57(6),99(8),23(1),3(4),(0),5(6),1(2)]
            [[],[],[],[],[],[],[],[],[], [] ]
             0  1   2  3  4  5  6  7  8   9

           [[0],[231],[12],[213],[34],[345],[576,56],[],[998], [] ]
           then it compares again this time on the second to last digit : 1(2)3 if the value doesn't have one it goes to the zero bucket

           [[(null)0],[2(3)1],[(1)2],[2(1)3],[(3)4],[3(4)5],[5(7)6,(5)6],[],[9(9)8], [] ]
            [[0,],[12, 213],[213],[34],[345],[],[56],[576],[], [998] ]
             0        1       2     3    4    5   6    7    8    9

        then again utill they're sorted in the right place
        
        """
        max1 = max(unsorted_list)
        exp = 1 
        while max1 / exp > 0:
            self.counting_sort(unsorted_list, exp)
            exp *= 10
        return unsorted_list

    def counting_sort(self, unsorted_list:list, exp : int):
        list_length = len(unsorted_list)

        sorted_list = [0] *(list_length)
        count = [0] * 10 # buckets

        for i in range(0, list_length):
            index = unsorted_list[i] // exp 
            count[index% 10 ] += 1

        for i in range(1,10):
            count[i] += count[i-1]

        i = list_length - 1
        while i >= 0:
            index = unsorted_list[i] // exp 
            sorted_list[count[index % 10] - 1] = unsorted_list[i]
            count[index % 10] -= 1
            i -= 1
        i = 0
        for i in range(0, list_length):
            unsorted_list[i] = sorted_list[i]
        # return unsorted_list

    def _get_digit(self, number:int, place_in_number : int) -> int:
        """
            finds and returns the value at the place_in_number index
            get_digit( [1,2,3,4,5], 0) -> 5
            get_digit( [1,2,3,4,5], 1) -> 4
            get_digit( [1,2,3,4,5], 2) -> 3
            get_digit( [1,2,3,4,5], 3) -> 2
            get_digit( [1,2,3,4,5], 4) -> 1
            get_digit( [1,2,3,4,5], 5) -> None 

        Mathie way is faster by a shit ton but this is the way !

        """
        # if len(str( number) ) < place_in_number or number < place_in_number: return number
        # string_number = str(number)[::-1]
        # return string_number[place_in_number]

        import math
        return math.floor(abs(number) / pow(10, place_in_number)) % 10

    def _get_digit_count(self, number: int) -> int:
        """
        takes in a number
        returns its count
        12432 -> 5
        math strikes again, it's faster still than my way щ(ʘ╻ʘ)щ
        """
        # return len(str( abs(number)))
        import math
        if number == 0 : return 1
        return math.floor( math.log10(abs(number))) + 1

    def _get_larget_number(self, arr:list) -> int:
        """
        gets the count of digits for the longest number 
        did i say math is fast ? ? ? 
        """
        maximum :int = 0
        for i in arr:
            maximum = max(maximum, self._get_digit_count(i))
        return maximum

if __name__ == "__main__":
    search_alogs = SearchingAlgos()
    sort_algos = SortingAlgos()

    test_sorted_list = numpy.arange(1, 1_000_000_000) # calling tolist() on this is a big mistake!
    test_unsroted_list = numpy.random.randint(1_0, size=5).tolist()
    # test_unsroted_list = test_unsroted_list.tolist()
    test_nearly_sorted_list = [9,1,2,3,4,5,6,7,8]  
    # print(test_unsroted_list, "unsorted list")
    # print(sort_algos.quick_sort(test_unsroted_list, 0 , len(test_unsroted_list) -1 ), "Quick sort")
    print(sort_algos.radix_sort([23,45,665,32,7,9,92]), "radix sort")
    # print(sort_algos._get_digit(123, 1), "get digit")
    # print(sort_algos._get_larget_number([1,222,333,-12314214,123]), "get largest  number ")



    # print(sort_algos.merge_sort(test_unsroted_list), "Merge sort mine")
    # print(sort_algos.mergeSort(test_unsroted_list), "Merge sort GFG")
    # print(search_alogs.binary_search(test_sorted_list, 9))
    # print(sort_algos.bubble_sort(test_unsroted_list), "Bubble")
    # print(sort_algos.selection_sort(test_unsroted_list), "Selection")
    # print(sort_algos.insertion_sort(test_unsroted_list), "Insertion")
