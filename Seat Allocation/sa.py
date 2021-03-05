 # max of the list of votes

# Example code: 

# ----------

# def solve (Q, k, s, n):
#     # Write your code here

# n, k = raw_input().split()
# s = raw_input()
# q = input()
# Q = map(int, raw_input().split())

# out_ = solve(Q, k, s, n)
# print '\n'.join(map(str, out_))

# ----------

# USING HEAPQ IMPORT 

# make list with 3 values (coefficient, partyID, seats party has)
# Give it the value it has to compare by, then order by the first value...
# Can you also use list of lists? https://docs.python.org/3/library/heapq.html


# ----------


# USING ALG4 LIBRARY IMPORT 

from itu.algs4.sorting.max_pq import MaxPQ

import sys

# How many parties and how many seats are there?
# line_1 = sys.stdin.readlines()

# -------------- GET N and M -------------- 

# with open('input.txt', 'r') as f: 
#     for line in f.readlines(): 
#         print(line)
#         # line_1 =  line.split()
#             # print(line_1)
#         n = line[0]

#             # print(n)
#         m = line[2]
#             # print(m)
#         n= int(n)
#         m= int(m) 

# To begin with, each party's quotient is v_i/1
# You push them into the queue. 
# Then you have to delegate the seats to the parties - you'll do this by: popping the highest party quotient from the maxpq, 


n = 2
m = 2

class Party:
    
    def __init__(self, party, seats, votes):
        self.party = party 
        self.seats = seats 

        self.votes = votes 
        self.coefficient = self.votes/(self.seats+1)
        
    def calculate_coefficient(self):
        pass 
    
    def __lt__(self, opposit):
        print(self.coefficient)
#         print(opposit.coefficient)
        if self.coefficient < opposit.coefficient:
            return True
        
        # opposite is a party... we try to compare the coefficient
            # self is a new object... what would be the other one?
#             return True
        else:
            return False

maxPQ = MaxPQ()

for i in range(n):
    v = input()
    v = int(v)
    maxPQ.insert(Party(i, m, v))

# then give the seat to that party, recalculate the party's quotient v_i/(s_i+1), 
# and now push the new quotient into the maxpq

for i in range(1, m+1): # how is this a heap??
    print("Allocating first seat:", seat)
    seat = maxPQ.del_max()
    #print(seat)
    maxPQ.insert(Party(seat.party, seat.votes, seat.seats + 1))

# # This way, your maxpq will have one item per party, and the item will be the party's current quotient. 
# This way, 
# # you'll always be able to pop the highest quotient from the maxpq, which corresponds to the party that will 
# get the next seat

# # And you can either use the implementation they have provided in the library: 
# https://github.com/itu-algorithms/itu.algs4/blob/master/itu/algs4/sorting/max_pq.py
# # Or you can use the builtin Python module: https://docs.python.org/3/library/heapq.html 
# # It's basically the same thing, but it's just to say that you don't have to implement the 
# entire data structure yourself