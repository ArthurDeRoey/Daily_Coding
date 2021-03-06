from itu.algs4.sorting.max_pq import MaxPQ

from itu.algs4.stdlib.stdio import readString, readInt

import sys


from sys import stdin



data = stdin.read().strip().split('\n')


n, m = map(int, data[0].split())

class Party:
    
    def __init__(self, party, votes, seats=0):
        self.party = party 
        self.seats = seats 
        self.votes = votes 

        
    def __dhondt(self):
        return self.votes/(self.seats+1)

    
    def __lt__(self, other):
        if self.__dhondt() < other.__dhondt():
            return True 
        else: 
            return False

    def __str__(self):
        return str(self.seats)

PQ = MaxPQ()

for i in range(len(data[1:])):
    party = Party(i, int(data[1:][i]))
    PQ.insert(party)

for i in range(m):
    winner = PQ.del_max()
    winner.seats += 1
    PQ.insert(winner)

P = []

for p in PQ.__iter__(): 
    P.append([p.party, p.seats])

P = sorted(P, key=lambda tup: tup[0])

for p in P:
    print(p[1])
