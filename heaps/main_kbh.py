from .structs.kbh import KBH 

def values(items): 
    return [item.value for item in items]

def min_heap_demo():
    heap = KBH("min")

    print(f"# DEMO OF KEYED BINARY-HEAP ADT (MIN-HEAP) #")

    # display heap size
    print(f"> Heap Size: {heap.size()}") 
    print()
    assert(heap.size() == 0)

    # heapify items 
    heap.heapify_up([13, 15, 11, 12, 14, 19, 17, 18, 16, 15])
    assert(heap.size() == 10) 
    heap.heapify_down([13, 15, 11, 12, 14, 19, 17, 18, 16, 15])
    assert(heap.size() == 10) 
    
    # clear heap 
    print(f"> Clearing heap...")
    heap.clear() 
    assert(heap.size() == 0)
    assert(heap.items == [])

    # insert items in heap 
    heap.insert("a", 5)
    heap.insert("b", 1)
    heap.insert("c", 3)
    heap.insert("d", 4)
    heap.insert("e", 2)
    heap.insert("f", 9)
    heap.insert("g", 7)
    heap.insert("h", 6)
    heap.insert("i", 8)
    heap.insert("j", 10) 

    # display heap size 
    print(f"> Items: {values(heap.items)}")
    print(f"> Heap Size: {heap.size()}")
    print()
    assert(heap.size() == 10)

    # print keys and values
    print(f"> Keys: {list(heap.keys())}") 
    print(f"> Values: {list(heap.values())}")
    assert(len(list(heap.keys())) == 10) 
    assert(len(list(heap.values())) == 10)

    # delete three keys from heap 
    print(f"> Deleting 3, 5, and 7 from heap...") 
    heap.delete("c") 
    heap.delete("a") 
    heap.delete("g") 
    print()
    assert(heap.size() == 7) 
    assert("c" not in heap.keys())
    assert("a" not in heap.keys())
    assert("g" not in heap.keys())
    assert(3 not in heap.values())
    assert(5 not in heap.values())
    assert(7 not in heap.values())


    # test accessor and mutators 
    print(f"> Heap Top: {heap.top().key} -> {heap.top().value}")
    assert(heap.top().value == 1) 
    print(f"> Accessing Heap Top as 'b' : {heap.get_item('b')}") 
    assert(heap.get_item('b') == heap.top())
    print(f"> Data of 'j': {heap.get_data('j')}")
    assert(heap.get_data('j') == None)
    print(f"> Updating data of 'j' as 12...")
    heap.set_data('j', 12) 
    print(f"> Data of 'j': {heap.get_data('j')}")
    assert(heap.get_data('j') == 12)
    print(f"> Updating value of 'b' (top) as -5...")
    heap.set_value('b', -5) 
    print(f"> Value of 'b': {heap.get_value('b')}")
    assert(heap.get_value('b') == -5)
    print(f"> New Top: {heap.top().key} -> {heap.top().value}")
    assert(heap.top().key == "b") 
    assert(heap.top().value == -5)
    print(f"> Min: {heap.min()}")
    assert(heap.top() == heap.min())
    print(f"> Min Key: {heap.min_key()}")
    assert(heap.top().key == heap.min_key())
    print(f"> Min Value: {heap.min_value()}")
    assert(heap.top().value == heap.min_value())
    print() 

    # test pop 
    print(f"> Popping Top of Heap...")
    heap.pop() 
    print(f"> New Top Value: {heap.top().key} -> {heap.top().value}")
    print() 
    assert(heap.top().key == "e")
    assert(heap.top().value == 2)

    # unload heap 
    print(f"> Unloading Heap...")
    while heap.size() > 0: 
        heap.pop() 
    print(f"> Heap Size: {heap.size()}")
    assert(heap.size() == 0)

    # reinsert some data 
    print(f"> Reinserting some data...")
    heap.insert("a", 1)
    heap.insert("b", 2) 
    heap.insert("c", 3) 
    print()
    assert(heap.size() == 3)

    # test clear 
    print(f"> Clearing Heap...")
    heap.clear() 
    print(f"> Heap Size: {heap.size()}")
    assert(heap.size() == 0)

    print("==========================================================")


def max_heap_demo():
    heap = KBH("max")

    print(f"# DEMO OF KEYED BINARY-HEAP ADT (MAX-HEAP) #")

    # display heap size
    print(f"> Heap Size: {heap.size()}") 
    print()
    assert(heap.size() == 0)

    # heapify items 
    heap.heapify_up([13, 15, 11, 12, 14, 19, 17, 18, 16, 15])
    assert(heap.size() == 10) 
    heap.heapify_down([13, 15, 11, 12, 14, 19, 17, 18, 16, 15])
    assert(heap.size() == 10) 
    print()
    
    # clear heap 
    print(f"> Clearing heap...")
    heap.clear() 
    assert(heap.size() == 0)
    assert(heap.items == [])

    # insert items in heap 
    heap.insert("a", 5)
    heap.insert("b", 1)
    heap.insert("c", 3)
    heap.insert("d", 4)
    heap.insert("e", 2)
    heap.insert("f", 9)
    heap.insert("g", 7)
    heap.insert("h", 6)
    heap.insert("i", 8)
    heap.insert("j", 10) 

    # display heap size 
    print(f"> Items: {values(heap.items)}")
    print(f"> Heap Size: {heap.size()}")
    print()
    assert(heap.size() == 10)

    # print keys and values
    print(f"> Keys: {list(heap.keys())}") 
    print(f"> Values: {list(heap.values())}")
    assert(len(list(heap.keys())) == 10) 
    assert(len(list(heap.values())) == 10)

    # delete three keys from heap 
    print(f"> Deleting 3, 5, and 7 from heap...") 
    heap.delete("c") 
    heap.delete("a") 
    heap.delete("g") 
    print()
    assert(heap.size() == 7) 
    assert("c" not in heap.keys())
    assert("a" not in heap.keys())
    assert("g" not in heap.keys())
    assert(3 not in heap.values())
    assert(5 not in heap.values())
    assert(7 not in heap.values())


    # test accessor and mutators 
    print(f"> Heap Top: {heap.top().key} -> {heap.top().value}")
    assert(heap.top().value == 10) 
    print(f"> Accessing Heap Top as 'j' : {heap.get_item('j')}") 
    assert(heap.get_item('j') == heap.top())
    print(f"> Data of 'e': {heap.get_data('e')}")
    assert(heap.get_data('e') == None)
    print(f"> Updating data of 'e' as 12...")
    heap.set_data('e', 12) 
    print(f"> Data of 'j': {heap.get_data('e')}")
    assert(heap.get_data('e') == 12)
    print(f"> Updating value of 'j' (top) as 15...")
    heap.set_value('j', 15) 
    print(f"> Value of 'j': {heap.get_value('j')}")
    assert(heap.get_value('j') == 15)
    print(f"> New Top: {heap.top().key} -> {heap.top().value}")
    assert(heap.top().key == "j") 
    assert(heap.top().value == 15)
    print(f"> Max: {heap.max()}")
    assert(heap.top() == heap.max())
    print(f"> Max Key: {heap.max_key()}")
    assert(heap.top().key == heap.max_key())
    print(f"> Max Value: {heap.max_value()}")
    assert(heap.top().value == heap.max_value()) 
    print() 

    # test pop 
    print(f"> Popping Top of Heap...")
    heap.pop() 
    print(f"> New Top Value: {heap.top().key} -> {heap.top().value}")
    print() 
    assert(heap.top().key == "f")
    assert(heap.top().value == 9)

    # unload heap 
    print(f"> Unloading Heap...")
    while heap.size() > 0: 
        heap.pop() 
    print(f"> Heap Size: {heap.size()}")
    assert(heap.size() == 0)

    # reinsert some data 
    print(f"> Reinserting some data...")
    heap.insert("a", 1)
    heap.insert("b", 2) 
    heap.insert("c", 3) 
    print()
    assert(heap.size() == 3)

    # test clear 
    print(f"> Clearing Heap...")
    heap.clear() 
    print(f"> Heap Size: {heap.size()}")
    assert(heap.size() == 0)

    print("==========================================================")

min_heap_demo()
max_heap_demo()