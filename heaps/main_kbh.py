from .structs.kbh import KBH

def main_a():
    heap = KBH() 

    arr = []

    for i in range(10, -1, -1): 
        arr.append(i)

    heap.heapify_up(arr)

    print(list(heap.keys()))
    print(list(heap.values()))
    print(heap.key_map)

    print("Updating 4 to value -10")
    heap.update(4, -10)

    print(list(heap.keys()))
    print(list(heap.values()))
    print(heap.key_map)

def main_b(): 
    heap = KBH() 

    arr = {
        "a" : 1,
        "b" : 2, 
        "c" : 3, 
        "d" : 4, 
        "e" : 5, 
        "f" : 6, 
        "g" : 7, 
        "h" : 8
    }

    heap.heapify_up(arr)

    print(list(heap.keys()))
    print(list(heap.values()))
    print(heap.key_map)

    print("Updating values...")
    heap.update("f", 10)
    heap.update("c", -20)

    print("Inserting i with value 9")
    heap.insert("i", 9)

    heap.delete("d")

    print(list(heap.keys()))
    print(list(heap.values()))
    print(heap.key_map)


    print("--- Heap Sort Demo ---")

    heap.display()

    n = heap.size()
    for i in range(n): 
        print(heap.top().key, heap.top().value)
        heap.pop()

def main_c(): 
    heap = KBH() 

    for i in range(20000): 
        heap.insert(i, i) 
    
    for i in range(20000): 
        heap.pop()

main_c()