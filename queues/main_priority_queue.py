from .structs.priority_queue import PriorityQueue

queue = PriorityQueue("max") 

N = 100
G = 10 

k = 0
for i in range(N//G):
    for j in range(G): 
        queue.enqueue(k, i, (i + 1) + (j + 1))
        k += 1

queue.items.display()
print(queue.items.max_key)

while queue.length() > 0: 
    print(queue.front())
    queue.dequeue_front() 

