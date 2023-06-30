from .structs.kmmh import KMMH 

heap = KMMH() 

# heap.build_heap([1, 2, 3, 4, 5, 6, 7, 8])

items = [
    ("a", 1), 
    ("b", 2), 
    ("c", 3), 
    ("d", 4), 
    ("e", 5), 
    ("f", 6), 
    ("g", 7), 
    ("h", 8)
]

for item in items: 
    heap.insert(*item)

heap.update("c", -100)
heap.update("b", 200) 

print("Min:", heap.min_value()) 
print("Max:", heap.max_value())

heap.display()
