from .structs.kfh import KFH

heap = KFH() 

heap.insert("a", 10)
heap.insert("b", 20)
heap.insert("c", 30)
heap.insert("d", 40)
heap.insert("e", 50)
heap.insert("f", 60)
heap.insert("g", 70)
heap.insert("h", 80)

print("No. of items before popping:", heap.count)
heap.pop()
print("No. of items after popping:", heap.count)