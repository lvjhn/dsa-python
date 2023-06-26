''' 
    HEAP IMPLEMENTATION (PYTHON)

    Notes: 
		* isolated
			- does not depend on third-party packages or other files 
			- can be used as is
        
        * printable / narrow width

        * reference (slightly modified implementation)
            - https://www.programiz.com/dsa/fibonacci-heap
            - https://www.programiz.com/dsa/decrease-key-and-delete-node-from-a-fibonacci-heap

		* implements common operations
            - value(x) 
            - comparator(a, b) 
            - swap_key_map(i, j)
            - insert(key, value)
            - delete() 
            - update(key, new_value)
            - update_a(key, value)
            - update_b(key, value)  
            - keys()
            - values()
            - top()
            - size()
''' 

class FibonacciTree: 
    def __init__(self, key, value, data = None): 
        self.key = key 
        self.value = value 
        self.data = data
        self.children = [] 
        self.order = 0

    def add_at_end(self, tree): 
        self.children.append(tree)
        self.order = self.order + 1 

class FibonacciHeap: 
    def __init__(self, type_ = "min"): 
        self.trees = [] 
        self.least = None 
        self.count = 0 
        self.type_ = type_
        self.key_no = 0 
        self.key_map = {} 

    def value(self, x): 
        return x.value

    def comparator(self, a, b): 
        if self.type == "min": 
            return self.value(a) < self.value(b)
        elif self.type == "max":
            return self.value(a) > self.value(b)
        return None

    def swap_key_map(i, j):
        arr = self.items
        self.key_map[arr[i].key] = j
        self.key_map[arr[j].key] = i

    def insert(key, value):
        pass 

    def delete():
        pass 

    def update(key, new_value):
        pass 
        
    def update_a(key, value):
        pass 

    def update_b(key, value):
        pass 

    def keys(self):
        pass 

    def values(self)
        pass 

    def top(self):
        pass 

    def size(self):
        pass 
