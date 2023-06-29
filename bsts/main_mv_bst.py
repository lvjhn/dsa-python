from .structs.mv_bst import MV_BST
from .structs.rbt import RBT
from .structs.avlt import AVLT
import random

bst = MV_BST(driver=AVLT) 

for i in range(100000//3):
    for j in range(3): 
        bst.insert(i, i + j) 

# bst.tree.display()

print(bst.tree.size())

value = bst.tree.find(30).value 

print(value.size)
print("------")
for item in value.iterate(): 
    print(item.value)

print("------")

print(bst.get_current_value(30))
bst.delete(30)
print(bst.get_current_value(30))
bst.delete(30)
print(bst.get_current_value(30))
bst.delete(30)
print(bst.get_current_value(30))

print