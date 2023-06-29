""" 
    DOUBLE-ENDED PRIORITY QUEUE IMPLEMENTATION 
    (Uses BSTH) 
""" 
from heaps.structs.bsth import BSTH

class PriorityQueue: 
    def __init__(self, type_ = "min"): 
        self.items = BSTH()  
        self.type = type_

    def min(self):
        min_node = self.items.min_node()
        return (
            min_node.key,  
            self.items.key_data[self.items.min_key][0],
            self.items.key_data[self.items.min_key][1]
        )
    
    def max(self):
        max_node = self.items.max_node()
        return (
            max_node.key,  
            self.items.key_data[self.items.max_key][0],
            self.items.key_data[self.items.max_key][1],
        )

    def front(self): 
        if self.type == "min":
            return self.min()
        elif self.type == "max": 
            return self.max()

    def back(self): 
        if self.type == "min": 
            return self.max()
        elif self.type == "max": 
            return self.min()

    def enqueue(self, key, priority, data = None): 
        self.items.insert(key, priority, data) 

    def dequeue_front(self):
        if self.type == "min":
            return self.items.pop_min()
        elif self.type == "max": 
            return self.items.pop_max()

    def dequeue_back(self): 
        if self.type == "min":
            return self.items.pop_max()
        elif self.type == "max": 
            return self.items.pop_min()  

    def length(self): 
        return self.items.size()
