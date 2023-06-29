from .structs.deque import Deque 

queue = Deque() 

queue.enqueue_back(1)
queue.enqueue_back(2)
queue.enqueue_back(3)
queue.enqueue_back(4) 

while queue.length() > 0: 
    print(queue.front().value)
    queue.dequeue_front() 

