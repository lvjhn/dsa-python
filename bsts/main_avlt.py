from .structs.avlt import AVLT 

N_ITEMS = 20

avlt = AVLT() 

for i in range(N_ITEMS): 
    avlt.insert(i, i)

print(avlt.size())

avlt.delete(12)

print(avlt.size())

avlt.display()