def snail(snail_map):
    pass

"""
n*n 
k:  [  -> a.length
        take the last elemnts of each sub array (loop till k.length)
        go left c.length
        go up k.length -1 cause u already took 1
        go right b.length -1 cause u already took 6
       a: [1, 2, 3],
       b: [4, 5, 6],
       c: [7, 8, 9],
    ]
   result =  [1,2,3,6,9,8,7,4,5]
   
   1 -> 2 -> 3 
   go down untill the end of the matrix
   6 -> 9
   go left untill the end
   8 -> 7 
   go up untill u reach the traversed element 1
   4
   go right
   5
]

"""


if __name__ == "__main__":
    pass
