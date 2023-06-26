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
            - value() 
            - comparator() 
            - keyfy(self, items) 
            - swap_key_map(i, j)
            - heapify_up(items, keyfy) 
            - heapify_down(items, keyfy) 
            - insert(key, value)
            - delete() 
            - update(key, new_value)
            - update_a(key, value)
            - update_b(key, value)  
            - keys(self)
            - values(self)
            - top(self)
            - size(self)
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

    def comparator(self, a, b):
        if self.type == "min": 
            return a < b 
        elif self.type == "max":
            return a > b 
        return None

    def insert(self, key, value, data = None): 
        new_tree = FibonacciTree(key, value, data)
        self.trees.append(new_tree) 

        if self.least is None or self.comparator(self.value())