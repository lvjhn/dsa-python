from .structs.avlt import AVLT, AVLT_Node

print(f"# DEMO OF AVL TREE ADT #")

# create stack
bst = AVLT() 

# display initial Tree size 
print(f"> Tree Size: {bst.size()}")
print()
assert(bst.size() == 0)

# insert items to the tree
print(f"> Inserting items to the tree...")
bst.insert(10, "a")
bst.insert(20, "b")
bst.insert(30, "c")
bst.insert(40, "d")
bst.insert(50, "e")
bst.insert(60, "f")
bst.insert(70, "g")
bst.insert(80, "h")
bst.insert(90, "i")
bst.insert(100, "j")
bst.display()
print(f"> Tree Size: {bst.size()}")
print()
assert(bst.size() == 10)

# printing keys and values 
print(f"> Displaying keys and values...")
print(f"> Keys: {list(bst.keys())}")
print(f"> Values: {list(bst.values())}")

# search items from the tree 
print(f"Finding 50: {bst.find(50)}")
print(f"Finding -1: {bst.find(-1)}")
print()
assert(type(bst.find(50)) is AVLT_Node) 
assert(bst.find(-1) is None)

# delete items 
print(f"Deleting items 20, 50, 70 from the tree..") 
bst.delete(20)
# bst.delete(30) 
# bst.delete(50) 

bst.display()
