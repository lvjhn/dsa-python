from .structs.avlt import AVLT 
import random 

random.seed(1)

N_ITEMS = 1_000_000

avlt = AVLT() 

keys = [random.randint(0, 100) for i in range(N_ITEMS)]
values = [random.uniform(0, 100) for i in range(N_ITEMS)]

for i in range(N_ITEMS):
    avlt.insert(keys[i], values[i]) 

# avlt.display()