from .structs.avlt import AVLT, AVLT_Node

print(f"# DEMO OF AVL TREE ADT #")

# create stack
bst = AVLT() 

# display initial Tree size 
print(f"> Tree Size: {bst.size()}")
print()
assert(bst.size() == 0)

keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
values = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# insert keys to the tree
print(f"> Inserting keys to the tree...")
for i in range(len(keys)): 
    print(f"> Inserting ({keys[i]}, {values[i]})")
    bst.insert(keys[i], values[i])
    bst.display() 
    print("=====================================")