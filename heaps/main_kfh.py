from .structs.kfh import KFH
import random 
import time 

heap = KFH("min") 

# Custom Comprator Demo 
def comparator(a, b): 
    if heap.type == "min": 
        if a.value == b.value: 
            return a.key < b.key 
        else: 
            return a.value < b.value  
    elif heap.type == "max": 
        if a.value == b.value: 
            return a.key > b.key 
        else: 
            return a.value > b.value  

heap.comparator = comparator 

heap.insert("a", 10)
heap.insert("b", 20)
heap.insert("c", 30)
heap.insert("d", 40)
heap.insert("e", 50)
heap.insert("f", 60)
heap.insert("g", 60)
heap.insert("h", 60)
heap.insert("i", 70)
heap.insert("j", 80)

# Update and Pop 
heap.display()

heap.update("e", -100)

print("heap.min()", heap.min())

print("No. of items before popping:", heap.count)
heap.pop()
print("No. of items after popping:", heap.count)

print("heap.min():", heap.min())

heap.display()

# Unload heap 
while heap.size() > 0: 
    top = heap.top() 
    print(top.value, top.key) 
    heap.pop()
    