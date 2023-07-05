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

print("> Printing at values...")
items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(items)): 
    print(f"> bst.at({i}) = {bst.at(i).key} -> {bst.at(i).value}")
    assert(bst.at(i).key == items[i])
print()

print(f"Printing previous and next...")
prev_ = [] 
next_ = [] 
for item in bst.iterate(): 
    key = item.key
    prev__ = bst.prev(key)
    next__ = bst.next(key)
    
    print(f"@ item-{key} : ".ljust(20) + \
          f"prev ({prev__.key if prev__ else None}), " + \
          f"next ({next__.key if next__ else None})")
    
    prev_.append(prev__.key if prev__ else None)
    next_.append(next__.key if next__ else None)
assert(prev_ == [None, 10, 20, 30, 40, 50, 60, 70, 80, 90])
assert(next_ == [20, 30, 40, 50, 60, 70, 80, 90, 100, None])
print()

# printing keys and values 
print(f"> Displaying keys and values...")
print(f"> Keys: {list(bst.keys())}")
print(f"> Values: {list(bst.values())}")
print()

# search items from the tree 
print(f"Finding 50: {bst.find(50)}")
print(f"Finding -1: {bst.find(-1)}")
print()
assert(type(bst.find(50)) is AVLT_Node) 
assert(bst.find(-1) is None)

# delete items 
print(f"Deleting items 20, 50, 70 from the tree..") 
bst.delete(20)
bst.delete(30) 
bst.delete(50) 
bst.display()
print() 

print(f"> Displaying keys and values...")
print(f"> Keys: {list(bst.keys())}")
print(f"> Values: {list(bst.values())}")
print()
assert(20 not in bst.keys()) 
assert(30 not in bst.keys()) 
assert(50 not in bst.keys())

print(f"> Update value of 70 to 'z'...")
print(f"> Current Value of '70': {bst.find(70).value}")
bst.update(70, "z") 
print(f"> New Value of '70': {bst.find(70).value}")
assert(bst.find(70).value == "z")