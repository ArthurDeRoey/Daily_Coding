import sys

dna = sys.stdin.read()

alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

def reverse_complement(dna):    
    for k,v in alt_map.items():
        dna = dna.replace(k,v)
    bases = list(dna) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases
print(reverse_complement(dna))