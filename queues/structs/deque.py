""" 
    DOUBLE-ENDED QUEUE IMPLEMENTATION 
    (Uses Doubly-Linked List) 
""" 
from linked_lists.structs.dll import DLL

class Deque: 
    def __init__(self): 
        self.items = DLL()  

    def front(self): 
        return self.items.head 

    def back(self): 
        return self.items.tail

    def enqueue_front(self, item): 
        self.items.prepend(item) 

    def enqueue_back(self, item): 
        self.items.append(item) 

    def dequeue_front(self): 
        front = self.front() 
        self.items.delete_head() 
        return front 

    def dequeue_back(self): 
        back = self.back() 
        self.items.delete_tail() 
        return back     

    def length(self): 
        return self.items.size 
