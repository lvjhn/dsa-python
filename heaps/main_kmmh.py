from .structs.kmmh import KMMH 

def values(items): 
    return [item.value for item in items]

def kmmh_demo(): 
    print(f"# DEMO OF KEYED MIN-MAX HEAP ADT (MIN-HEAP) #")

    heap = KMMH() 

    # display heap size
    print(f"> Heap Size: {heap.size()}") 
    print()
    assert(heap.size() == 0)

    # build heap 
    heap.build_heap([12, 11, 13, 14, 15, 17, 16, 19, 18, 20])
    assert(heap.size() == 10)
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

    # assert heap size 
    print(f"> Heap Items: {values(heap.items)}")
    assert(heap.size() == 10)
    print()

    # assert min and max
    print(f"> Heap Min: {heap.min().key} -> {heap.min().value}") 
    print(f"> Heap Max: {heap.max().key} -> {heap.max().value}")
    print()
    assert(heap.min().key == "b") 
    assert(heap.min().value == 1)
    assert(heap.max().key == "j") 
    assert(heap.max().value == 10)

    # test accessor and mutators 
    print(f"> Heap Min: {heap.min().key} -> {heap.min().value}")
    assert(heap.min().key == 'b') 
    assert(heap.min().value == 1) 
    print(f"> Accessing Heap Top as 'b' : {heap.get_item('b')}") 
    assert(heap.get_item('b') == heap.min())

    print(f"> Heap Max: {heap.max().key} -> {heap.max().value}")
    assert(heap.max().key == 'j') 
    assert(heap.max().value == 10) 
    print(f"> Accessing Heap Top as 'j' : {heap.get_item('j')}") 
    assert(heap.get_item('j') == heap.max())

    print(f"> Data of 'e': {heap.get_data('e')}")
    assert(heap.get_data('e') == None)
    print(f"> Updating data of 'e' as 12...")
    heap.set_data('e', 12) 
    print(f"> Data of 'e': {heap.get_data('e')}")
    assert(heap.get_data('e') == 12)

    print(f"> Updating 'b' and 'j' values to -5 and 15 respectively")
    heap.set_value("b", -5)
    heap.set_value("j", 15)

    print(f"> New Heap Min: {heap.min().key} -> {heap.min().value}")
    assert(heap.min().key == 'b') 
    assert(heap.min().value == -5)     
    print(f"> New Heap Max: {heap.max().key} -> {heap.max().value}")
    assert(heap.max().key == 'j') 
    assert(heap.max().value == 15) 
    print()

    # pop min and max 
    print(f"> Popping Min and Max...") 
    heap.pop_min() 
    heap.pop_max() 
    print(f"> Heap Min: {heap.min().key} -> {heap.min().value}") 
    print(f"> Heap Max: {heap.max().key} -> {heap.max().value}")
    print()
    assert(heap.min().key == "e") 
    assert(heap.min().value == 2)
    assert(heap.max().key == "f") 
    assert(heap.max().value == 9)

    # unload heap 
    while heap.size() > 0: 
        heap.pop_min() 
        heap.pop_max() 
    print(f"> Heap Size: {heap.size()}")
    assert(heap.size() == 0)

    # reinsert some data
    print(f"> Reinserting some data...")
    heap.insert("a", 1)
    heap.insert("b", 2) 
    heap.insert("c", 3) 
    assert(heap.size() == 3)
    print()

    # test clear 
    print(f"> Clearing Heap...")
    heap.clear() 
    print(f"> Heap Size: {heap.size()}")
    assert(heap.size() == 0)


kmmh_demo()