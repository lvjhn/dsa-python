from .structs.binary_heap import BinaryHeap  

def main_a():
    heap = BinaryHeap() 

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
    heap = BinaryHeap() 

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

    print("Updating f to value 10")
    heap.update("f", 10)
    heap.insert("i", 9)

    print(list(heap.keys()))
    print(list(heap.values()))
    print(heap.key_map)


    print("--- Heap Sort Demo ---")

    n = heap.size()
    for i in range(n): 
        print(heap.top().value)
        heap.delete()

main_b()