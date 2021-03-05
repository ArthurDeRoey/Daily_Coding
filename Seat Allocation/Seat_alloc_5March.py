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
line1 = sys.stdin.readlines()
print(line1)
n = line1[0]
# m = line1[1]
n= int(n) #, int(m)

# To begin with, each party's quotient is v_i/1
# You push them into the queue. 
# Then you have to delegate the seats to the parties - you'll do this by: popping the highest party quotient from the maxpq, 

class Party:
    
    def __init__(self, party, votes):
        self.party = party 
        self.seats = seats 

        self.votes = votes 
        self.coefficient = self.votes/(self.seats+1)
        
    def calculate_coefficient(self):
        pass # ???
    
    def __lt__(self, opposit):
        if self.coefficient < opposit: # opposite is a party... we try to compare the coefficient
            # self is a new object... what would be the other one?
            return True
        else:
            return False

maxPQ = MaxPQ()

for i in range(n):
    v = input()
    v = int(v)
    maxPQ.insert(Party(i, v))

# then give the seat to that party, recalculate the party's quotient v_i/(s_i+1), and now push the new quotient into the maxpq

for i in range(1, m+1): # how is this a heap??
    seat = maxPQ.del_max()
    maxPQ.insert(Party(seat.party, seat.votes, seat.seats + 1))

# This way, your maxpq will have one item per party, and the item will be the party's current quotient. This way, 
# you'll always be able to pop the highest quotient from the maxpq, which corresponds to the party that will get the next seat

# And you can either use the implementation they have provided in the library: https://github.com/itu-algorithms/itu.algs4/blob/master/itu/algs4/sorting/max_pq.py
# Or you can use the builtin Python module: https://docs.python.org/3/library/heapq.html 
# It's basically the same thing, but it's just to say that you don't have to implement the entire data structure yourself




# ----- NaN -----


# # Array with the original values
# parties = []
# # Array that will be changed throughout the script
# temp = []

# Get the needed data for each list


# for i in range(1, nParties+1):
#     append = 'th' if i > 3 else ('rd' if i == 3 else ('nd' if i == 2 else 'st'))
#     name = input("Name of the "+str(i)+append+" party?")
#     votes = int(input("Number of votes on party \""+name+"\"?"))
#     parties.append({'name':name,'votes':votes})
#     temp.append({'name':name,'votes':votes,'seats':0})

# if i == 1:
#     append = 'st'
# elif i == 2:
#     append = 'nd'
# elif i == 3:
#     append = 'rd'
# else:
#     append = 'th'

# append = 'th' if i > 3 else ('rd' if i == 3 else ('nd' if i == 2 else 'st'))









# # Begin loop to calculate seat distribution
# for i in range(1, nSeats+1):
#     # For each seat, find the party with more votes
#     maxVotes = 0
#     maxParty = 0
#     partyIndex = 0
#     twoOrMoreEqual = False;
#     # For each party, find how many votes should be accounted for, when assigning the ith seat
#     for j in temp:
#         if (j['votes'] > maxVotes):
#             # This is the party with the most votes, until now
#             maxVotes = j['votes']
#             maxParty = partyIndex
#             twoOrMoreEqual = False
#         elif (j['votes'] == maxVotes and maxVotes != 0):
#             # The current party has the same ammount of votes has the one with more votes
#             twoOrMoreEqual = True
#         partyIndex += 1
#     if (twoOrMoreEqual):
#         # There are two or more parties with the same ammount of votes for this seat
#         # Assign the seat to the party with the least total votes
#         minVotes = 0
#         minParty = 0
#         n = 0
#         for j in temp:
#             if j['votes'] == maxVotes:
#                 if minVotes == 0: # first iteration, this is automatically the party with less votes
#                     minVotes = parties[n]['votes']
#                     minParty = n
#                 elif minVotes > parties[n]['votes']:
#                     # This is the list with less votes until now
#                     minVotes = parties[n]['votes']
#                     minParty = n
#             n+=1
#         # A lista com menos votos totais e a que elege o mandato (o indice e igual)
#         maxParty = minParty
#         twoOrMoreEqual = False
#     # Increment the number of seats taken by the party with more votes in this iteration
#     temp[maxParty]['seats'] += 1
#     # Finds the number of votes that will be taken into account for this party, in the nex iteration
#     # by dividing th total ammount of votes it had, by the number of seats it has won +1
#     temp[maxParty]['votes'] = parties[maxParty]['votes']/(temp[maxParty]['seats']+1)
#     print(temp[maxParty]['name'] + ' - ' + str(maxVotes))

# for j in temp:
#     if (j['votes'] > maxVotes):
#     	temp[maxParty]['name']

# print("============ TOTALS ============")
# for j in temp:
# 	print(j['name'] + ' => ' + str(j['seats']))
