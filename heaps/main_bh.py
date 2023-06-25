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
        "h" : 8, 
        "i" : 9, 
        "j" : 10, 
        "k" : 11, 
        "l" : 12
    }

    heap.heapify_up(arr)

    print(list(heap.keys()))
    print(list(heap.values()))
    print(heap.key_map)

    print("Updating 4 to value -10")
    heap.update("i", -10)

    print(list(heap.keys()))
    print(list(heap.values()))
    print(heap.key_map)

    print(heap.top().key)

main_b()