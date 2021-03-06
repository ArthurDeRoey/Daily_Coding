from itu.algs4.sorting.max_pq import MaxPQ
#from itu.algs4.sorting.heap import sort
from itu.algs4.sorting.index_min_pq import IndexMinPQ
from itu.algs4.stdlib.stdio import readString, readInt
import sys

p=readInt()
# parties
s=readInt()
# seats
maxPQ = MaxPQ()
partiesdict = {}
plist = []
tempPartylist = []
qu = 0
votes = 0

def quotient(qu, nextP):
    if nextP > qu:
        return True
    else:
        #rearrange()
        return False

def rearrange():
    tempPartylist.clear()
    for i in range(p):
        maxPQ.insert(plist[i])
        #tempPartylist.append(i)
    vi = maxPQ.max()
    si = partiesdict[maxPQ.max()][0]
    partiesdict[maxPQ.max()][1] = vi / (si + 1)
    qu = partiesdict[maxPQ.max()][1]

def sizeChecker(n):
    if n > 0:
        return True
    else:
        rearrange()
        return False
#party = IndexMinPQ()
for i in range(p):
    v = readInt()
    maxPQ.insert(v)
    plist.append(v)
    partiesdict[v] = [0,0] # seats, quotient
    #partiesdict.append({v:0})

'''for i in range(len(plist)):
    votes+=plist[i]'''

# first guy get a point

i = 0
partiesdict[maxPQ.max()][0]+=1
i+=1
vi = maxPQ.max()
si = partiesdict[maxPQ.max()][0]
partiesdict[maxPQ.max()][1] = vi / (si + 1)
qu = partiesdict[maxPQ.max()][1]
tempPartylist.append(maxPQ.max())
maxPQ.del_max()
#print("i is:",i)
#print("s is:",s)
# we know the quatient

while i < s: #main loop for the seats
    #print("in the first while loop")
    #print("qu is",qu)
    # quatients for prev party, second max
    while quotient(qu,maxPQ.max()) and sizeChecker(maxPQ.size()) > 0 and i < s:
        #print("next seat is:",i)
        partiesdict[maxPQ.max()][0]+=1
        i+=1
        vi = maxPQ.max()
        si = partiesdict[maxPQ.max()][0]
        partiesdict[maxPQ.max()][1] = vi / (si + 1)
        #print("seat was", i)
        tempPartylist.append(maxPQ.max())
        maxPQ.del_max()
        #qu = partiesdict[maxPQ.max()][1]
        #tempPartylist.append(maxPQ.max())
        #maxPQ.del_max()
        if maxPQ.size() == 0:
            rearrange()
        else:
            qu = partiesdict[maxPQ.max()][1]
            print(qu)
    else: 
        rearrange()

for i in plist:
    print("party: ",i, partiesdict[i])

for i in plist:
    print(partiesdict[i][0])
#print(partiesdict)
#print(partiesdict[10][0])
#print(maxPQ.max())
#maxPQ.del_max()
#print(maxPQ.max())
#print(" size,",maxPQ.size())
#maxPQ.del_max()
#print(maxPQ.max())
#print(" size,",maxPQ.size())
#print(partiesdict[maxPQ.max()])
#print(party.min_index())

# own quatient 

#print(sort(maxPQ))
#print(plist)
#print(party)
#for i in range(len(plist)):
 #   print(partiesdict[i+1][plist[i]])
    
    
#print(maxPQ.size())
#print(maxPQ.__len__())
#print(maxPQ.max())
#print(maxPQ._pg())
#print(maxPQ)
#print(partiesdict)
#print(partiesdict[1])
#print(partiesdict[1][10])
#partiesdict[1][10] = 5
#partiesdict[1][10] = partiesdict[1][10]+10
#print(partiesdict[1][10])
#partiesdict[1][10]+=1
#print(partiesdict[1][10])
#print(plist)

# https://zapier.com/apps/airtable/integrations/monkeylearn-legacy

# https://www.integromat.com/en/integration/3783-analyze-airtable-data-with-monkeylearn-machine-learning-models

