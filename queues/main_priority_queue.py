from .structs.priority_queue import PriorityQueue

queue = PriorityQueue() 

queue.enqueue("a", 5, None)
queue.enqueue("b", 5, None)
queue.enqueue("c", 10, None)
queue.enqueue("d", 10, None)

while queue.length() > 0: 
    print(
        f"{queue.front().key} -> {queue.front().value} : " +
        f"{queue.front().data}"
    )
    queue.dequeue_front() 


