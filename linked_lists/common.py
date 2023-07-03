from .structs.csll import CSLL 
from .structs.cdll import CDLL

def display_list(llist): 
    print("> List Items: ", end="")
    for item in llist.iterate():
        print(item.value, end=" -> ")
    print("None")

def value_fn(node): 
    if node: 
        return node.value 
    else: 
        return None

def as_array(llist): 
    arr = [] 
    for item in llist.iterate(): 
        arr.append(item.value)
    return arr

def linked_list_demo(llist):

    print(f"# DEMO OF {llist.__class__} #")

    # display initial size 
    print(f"> List Size: {llist.size()}")

    # prepend items 
    print(f"> Prepending items 3, 2, and 1 ...") 
    llist.prepend(3)
    llist.prepend(2) 
    llist.prepend(1) 

    # display list 
    display_list(llist)
    assert(as_array(llist) == [1, 2, 3])

    # append items 
    print(f"> Appending items 7, 8, and, 9 ...")
    llist.append(7)
    llist.append(8)
    llist.append(9)

    # display list 
    display_list(llist)
    assert(as_array(llist) == [1, 2, 3, 7, 8, 9])

    # insert items 
    print(f"> Inserting items 4, 5, and 6 ...")
    llist.insert(3, 4)
    llist.insert(4, 5)
    llist.insert(5, 6) 

    # display list 
    display_list(llist)
    print()
    assert(as_array(llist) == [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # search for 5 
    print(f"> Searching for element with value 5 ...")
    at5 = llist.search(5) 
    print(f"> Element with value 5: (value: {at5.value}) -> {at5}")
    print() 
    assert(at5.value == 5)

    # get head and tail element  
    print(f"> Head: (value: {llist.head.value}) -> {llist.head}")
    print(f"> Tail: (value: {llist.tail.value}) -> {llist.tail}")
    print() 
    assert(llist.head.value == 1) 
    assert(llist.tail.value == 9)

    # get element at certain 
    print(f"> Getting element at position 4 and -5 ...")
    at4 = llist.at(4)
    atn5 = llist.at(-5)
    print(f"> Node at position 4: (value: {at4.value}) -> {at4}")
    print(f"> Node at position -5: (value: {atn5.value}) -> {atn5}")
    print()
    assert(at4.value == 5)
    assert(atn5.value == 5)

    # searching for element with value 
    print(f"> Searching for element with value 5...")
    s5 = llist.search(5)
    print(f"> Element with value 5: (value: {s5.value}) -> {s5}")
    print() 
    assert(s5.value == 5)

    # getting the index of node with value 5 
    print(f"> Getting the index of node 5") 
    print(f"> Index of node with value 5: {llist.index(5)}")
    print() 
    assert(llist.index(5) == 4)

    # getting the index of node with value  5 
    print(f"> Getting the index of 5th node") 
    print(f"> Index of 5th node: {llist.node_index(llist.at(5))}")
    print() 
    assert(llist.node_index(llist.at(5)) == 5)

    # search for node 
    print(f"> Researching for node at pos. 5 ...")
    at5 = llist.at(5)
    rs5 = llist.search_node(at5)
    print(f"> Node at position 5: (value: {at5.value}) -> {at5}")
    print(f"> Researched node: (value: {rs5.value}) -> {rs5}")
    print() 
    assert(at5.value == 6) 
    assert(rs5.value == 6)

    # insert items before and and after 
    print(f"> Inserting items 5.25 and 5.75 after 5 and before 6...") 
    llist.insert_before(llist.search(6), 5.75) 
    llist.insert_after(llist.search(5), 5.25)
    display_list(llist) 
    print()
    assert(llist.predecessor(llist.search(6)).value == 5.75)
    assert(llist.successor(llist.search(5)).value == 5.25)

    # delete items before and and after 
    print(f"> Deleting items before 6 and after 5") 
    llist.delete_before(llist.search(6)) 
    llist.delete_after(llist.search(5))
    display_list(llist) 
    print()
    assert(llist.successor(llist.search(5)).value == 6) 
    assert(llist.predecessor(llist.search(6)).value == 5)

    # delete specific node 
    print(f"> Deleting node at index 4 ...") 
    llist.delete(4)
    display_list(llist)
    assert(llist.at(4).value == 6)

    print(f"> Deleting node with value 6 ...")
    llist.delete_node(llist.search(6))
    display_list(llist)
    assert(llist.search(6) == None)

    print(f"> Reinserting nodes...") 
    llist.insert(4, 5)
    llist.insert(5, 6)
    display_list(llist)
    print() 
    assert(as_array(llist) == [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # getting predecessor and successor of head
    node = llist.head
    print("> Predecessor and Successor of Head: ")
    print(f"> Predecessor: {value_fn(llist.predecessor(node))}")
    print(f"> Successor: {value_fn(llist.successor(node))}")
    print() 
    
    if llist.__class__ is CDLL: 
        assert(value_fn(llist.predecessor(node)) == 9) 
    else: 
        assert(value_fn(llist.predecessor(node)) == None) 

    assert(value_fn(llist.successor(node)) == 2)

    # getting predecessor and successor of tail
    node = llist.tail
    print("> Predecessor and Successor of Tail: ")
    print(f"> Predecessor: {value_fn(llist.predecessor(node))}")
    print(f"> Successor: {value_fn(llist.successor(node))}")
    print()

    assert(value_fn(llist.predecessor(node)) == 8) 
        
    if llist.__class__ is CSLL or llist.__class__ is CDLL: 
        assert(value_fn(llist.successor(node)) == 1) 
    else: 
        assert(value_fn(llist.successor(node)) == None) 

    # getting predecessor and successor of element with value 5
    print("> Predecessor and Successor of Element with Value 5: ")
    node = llist.search(5)
    print(f"> Predecessor: {value_fn(llist.predecessor(node))}")
    print(f"> Successor: {value_fn(llist.successor(node))}")
    print()
    assert(value_fn(llist.predecessor(node)) == 4) 
    assert(value_fn(llist.successor(node)) == 6)

