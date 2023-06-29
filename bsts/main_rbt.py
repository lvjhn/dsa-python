from .structs.rbt import RBT 

N_ITEMS = 20

rbt = RBT() 

for i in range(N_ITEMS): 
    rbt.insert(i, i)

print(rbt.size())

rbt.delete(12)

print(rbt.size())

rbt.display()

print(rbt.find_max(rbt.root).key)