from .structs.avlt import AVLT 

N_ITEMS = 100_000

avlt = AVLT() 

for i in range(N_ITEMS): 
    avlt.insert(i, i)

# avlt.display()