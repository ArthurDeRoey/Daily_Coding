from itu.algs4.sorting.insertion_sort import sort
from itu.algs4.stdlib.stdio import readString, readInt
import sys

m = readInt()
list = []

for i in range(m):
    n = readString()
    g = readString()
    list.append([g,n])
    # print("name: ", n,"grade: ", g)
    
list.sort()

for i in list:
    print(i[-1])   