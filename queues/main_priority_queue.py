from .structs.priority_queue import PriorityQueue 

queue = PriorityQueue() 

print(f"# DEMO OF PRIORITY QUEUE ADT #")

queue = PriorityQueue() 

# display initial size 
print(f"> Queue Size: {queue.size()}")
print()
assert(queue.size() == 0)

# enqueue first three items
print(f"> Enqueuing g:6, h:7, and i:8 on the queue...")
queue.enqueue("g", 6) 
queue.enqueue("h", 7) 
queue.enqueue("i", 8)
print(f"> Front of Queue: {queue.front().value}")
print(f"> Back of Queue: {queue.back().value}")
print()
assert(queue.front().value == 6)
assert(queue.back().value == 8)

# enqueue next three items 
print(f"> Enqueuing a:1, b:2, and c:3 on the queue...")
queue.enqueue("a", 1) 
queue.enqueue("b", 2) 
queue.enqueue("c", 3)
print(f"> Front of Queue: {queue.front().value}")
print(f"> Back of Queue: {queue.back().value}")
print()
assert(queue.front().value == 1)
assert(queue.back().value == 8)

# enqueue next three items 
print(f"> Enqueuing d:5, e:d, and f:5 on the queue...")
queue.enqueue("d", 5) 
queue.enqueue("e", 5) 
queue.enqueue("f", 5)
print(f"> Front of Queue: {queue.front().value}")
print(f"> Back of Queue: {queue.back().value}")
print()
assert(queue.front().value == 1)
assert(queue.back().value == 8)

# check data
expected_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
expected_priorities = [1, 2, 3, 5, 5, 5, 6, 7, 8]

# unload queue from front
print(f"> Unloading queue from front...")
i = 0
while queue.size() > 0: 
    key = expected_keys[i]
    priority = expected_priorities[i] 
    print(f"> Dequeuing {queue.front().key}:{queue.front().value}...") 
    assert(queue.front().key == key) 
    assert(queue.front().value == priority)
    queue.dequeue_front() 
    i += 1
print() 
assert(queue.size() == 0)

print(f"> Reloading queue...")
for i in range(len(expected_keys)): 
    key = expected_keys[i] 
    priority = expected_priorities[i] 
    queue.enqueue(key, priority)
print(f"> Front of Queue: {queue.front().value}")
print(f"> Back of Queue: {queue.back().value}")
print()
assert(queue.front().value == 1)
assert(queue.back().value == 8)
assert(queue.size() == 9)

# unload queue from back
print(f"> Unloading queue from back...")
i = queue.size() - 1 
while queue.size() > 0 : 
    key = expected_keys[i] 
    priority = expected_priorities[i]
    print(f"> Dequeuing {queue.back().key}:{queue.back().value}...") 
    assert(queue.back().key == key) 
    assert(queue.back().value == priority)
    queue.dequeue_back()
    i -= 1 
print() 
assert(queue.size() == 0)
