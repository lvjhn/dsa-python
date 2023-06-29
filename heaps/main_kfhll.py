from .structs.kfhll import KFHLL
import random 
import time 

heap = KFHLL("max") 

# heap.insert("a", 10)
# heap.insert("b", 20)
# heap.insert("c", 30)
# heap.insert("d", 40)
# heap.insert("e", 50)
# heap.insert("f", 60)
# heap.insert("g", 70)
# heap.insert("h", 80)

# heap.update("f", -100)

# heap.display()

# print("heap.max()", heap.max())

# print("No. of items before popping:", heap.count)
# heap.pop()
# print("No. of items after popping:", heap.count)


# print("heap.max():", heap.max())

# heap.display()

N_ITEMS = 100000

for i in range(N_ITEMS): 
    heap.insert(i, i)

a = time.time() 
for i in range(N_ITEMS):
    heap.pop()
    # heap.update(i, random.uniform(0, 100))
b = time.time() 

print("Time:", b - a)

# heap.display() 