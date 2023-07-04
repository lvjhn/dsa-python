from .structs.deque import Deque 

def display_list(queue): 
    print("> Queue Items: ", end="")
    for item in queue.items.iterate(): 
        print(item.value, end = " <- ")
    print("None")

def value_fn(node): 
    if node: 
        return node.value 
    else: 
        return None 

def as_array(queue): 
    items = [] 
    for item in queue.items.iterate(): 
        items.append(item.value)
    return items

print(f"# DEMO OF STACK ADT #")

queue = Deque() 

# display initial size 
print(f"> Queue Size: {queue.size()}")
print()
assert(queue.size() == 0)

# enqueue items at the back 
print(f"> Enqueuing 4, 5, and 6 and the back of queue...")
queue.enqueue_back(4) 
queue.enqueue_back(5) 
queue.enqueue_back(6)
display_list(queue)
print()
assert(as_array(queue) == [4, 5, 6])

# enqueue items in front  
print(f"> Enqueuing 3, 2, and 1 in front of the queue...")
queue.enqueue_front(3) 
queue.enqueue_front(2)
queue.enqueue_front(1) 
display_list(queue) 
print()
assert(as_array(queue) == [1, 2, 3, 4, 5, 6])

# display front and back of the queue
print(f"> Front of Queue: {queue.front().value}") 
print(f"> Back of Queue: {queue.back().value}")
print() 
assert(queue.front().value == 1) 
assert(queue.back().value == 6) 

# dequeue first three items of the list 
print("> Dequeuing first three items in front of the list...") 
expected = [1, 2, 3, 4, 5, 6]
for i in range(3): 
    front = queue.front() 
    print(f"> Dequeuing {front.value}...")
    assert(front.value == expected[0])
    expected = expected[1:]
    queue.dequeue_front()  
    print(f"> Current Items: {as_array(queue)}")
    print(f"> Expected: {expected}")
    assert(as_array(queue) == expected)
    print("---------------------------------------------")
print() 

# dequeue last three items of the list 
print("> Dequeuing last three items in front of the list...") 
expected = [4, 5, 6]
for i in range(3): 
    back = queue.back() 
    print(f"> Dequeuing {back.value}...")
    assert(back.value == expected[-1])
    expected = expected[:-1]
    queue.dequeue_back()  
    print(f"> Current Items: {as_array(queue)}")
    print(f"> Expected: {expected}")
    assert(as_array(queue) == expected)
    print("---------------------------------------------")
print()

# display queue size 
print(f"> Queue Size: {queue.size()}")
assert(queue.size() == 0)