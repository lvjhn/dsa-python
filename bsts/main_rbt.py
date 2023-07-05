from .structs.rbt import RBT, RBT_Node

print(f"# DEMO OF RBT TREE ADT #")

# create stack
bst = RBT() 

# display initial Tree size 
print(f"> Tree Size: {bst.size()}")
print()
assert(bst.size() == 0)

keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
values = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# insert keys to the tree
print(f"> Inserting keys to the tree...")
for i in range(len(keys)): 
    bst.insert(keys[i], values[i])
bst.display()
print(f"> Tree Size: {bst.size()}")
print()
assert(bst.size() == 10)


print("> Printing at values...")
for i in range(len(keys)): 
    print(f"> bst.at({i}) = {bst.at(i).key} -> {bst.at(i).value}")
    assert(bst.at(i).key == keys[i])
print()

print("> Index of keys...")
for i in range(len(keys)): 
    print(f"> bst.index({keys[i]}) = {bst.index(keys[i])}")
    assert(bst.index(keys[i]) == i)
print()

print(f"Printing previous and next...")
prev_ = [] 
next_ = [] 
for item in bst.iterate(): 
    key = item.key
    prev__ = bst.key_prev(key)
    next__ = bst.key_next(key)
    
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

# search keys from the tree 
print(f"Finding 50: {bst.find(50)}")
print(f"Finding -1: {bst.find(-1)}")
print()
assert(type(bst.find(50)) is RBT_Node) 
assert(bst.find(-1) is None)

# delete keys 
print(f"Deleting keys 20, 50, 70 from the tree..") 
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