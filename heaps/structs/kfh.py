''' 
    KEYED FIBONACCI-HEAP IMPLEMENTATION (PYTHON)
    (Modified Fibonacci-Heap with Custom Keys)

    Notes: 
		* isolated
			- does not depend on third-party packages or other files 
			- can be used as is
        
        * printable / narrow width

        * reference (slightly modified implementation)
            - https://rosettacode.org/wiki/Fibonacci_heap

		* implements common operations
            - comparator(a, b) 
            - swap_key_map(i, j)
            - insert(key, value, data)
            - insert_node(node)
            - pop() 
            - consolidate() 
            - update(key, new_value)
            - update_a(key, value)
            - update_b(key, value)  
            - keys()
            - values()
            - top()
            - size()
            - get_data(key)
            - set_data(key, data) 
            - get_value(key) 
            - set_value(key, value)
            - get_item(key) 
            - set_item(key, data) 
            - display()
            - min() 
            - max() 
''' 
import math 

class KFH_Item: 
    def __init__(self, key, value, data = None): 
        self.key = key 
        self.value = value 
        self.data = data
        self.order = 0
        self.mark = False
        self.children = []
        self.parent = None

    def add_at_end(self, tree): 
        self.children.append(tree)
        self.order = self.order + 1 

class KFH: 
    def __init__(self, type_ = "min"): 
        self.children = [] 
        self.min_node = None 
        self.count = 0 
        self.type = type_
        self.key_no = 0 
        self.key_map = {} 
    
    def comparator(self, a, b): 
        if self.type == "min": 
            return a.value < b.value
        elif self.type == "max":
            return a.value > b.value
        return None

    def swap_key_map(self, i, j):
        arr = self.items
        self.key_map[arr[i].key] = j
        self.key_map[arr[j].key] = i

    def insert(self, key, value, data = None):
        node = KFH_Item(key, value, data)
        self.insert_node(node)  

    def insert_node(self, node):
        self.children.append(node)
        self.key_map[node.key] = node 
        if self.min_node is None or self.comparator(node, self.min_node): 
            self.min_node = node 

        self.count += 1 

    def pop(self):
        smallest = self.min_node 
        del self.key_map[smallest.key]

        if smallest is not None: 
            for child in smallest.children: 
                self.children.append(child) 
            self.children.remove(smallest) 
            if self.children == []:
                self.min_node = None 
            else: 
                self.min_node = self.children[0]
                self.consolidate() 
            self.count -= 1
            return smallest.key 
        return None 

    def consolidate(self): 
        aux = math.floor(math.log2(self.count) + 1) * [None] 

        while self.children != []: 
            x = self.children[0] 
            order = x.order 
            self.children.remove(x) 
            while aux[order] is not None: 
                y = aux[order] 
                if not self.comparator(x, y): 
                    x, y = y, x 
                x.add_at_end(y) 
                y.parent = x
                aux[order] = None 
                order += 1  
            aux[order] = x 
        
        self.min_node = None 

        for k in aux: 
            if k is not None: 
                self.children.append(k) 
                if self.min_node is None or self.comparator(k, self.min_node): 
                    self.min_node = k 

    def update(self, key, new_value): 
        if key not in self.key_map: 
            raise Exception(f"{key} is not in list.")
        item = self.key_map[key] 
        
        aux = KFH_Item(key, new_value, None)
        item = self.key_map[key]

        if self.comparator(aux, item): 
            self.update_a(key, new_value)
        else:   
            self.update_b(key, new_value)

    def update_a(self, key, value): 
        x = self.get_item(key)
        x.value = value 
        y = x.parent  
        if y is not None and self.comparator(x, y): 
            self.cut(x, y)
            self.cascading_cut(y) 
        if self.comparator(x, self.min_node): 
            self.min_node = x
 
    def update_b(self, key, value): 
        x = self.get_item(key)  

        # delete key 
        self.delete(key)

        # reinsert item with new value to the heap 
        self.insert(key, value, x.data)

    def delete(self, key): 
        del_val = None
        
        if self.type == "min": 
            del_val = float("-inf") 
        elif self.type == "max":  
            del_val = float("inf") 

        self.update_a(key, del_val)
        self.pop()   

    def cut(self, x, y): 
        y.children.remove(x) 
        y.order -= 1
        self.children.append(x)
        x.parent = None 
        x.mark = False

    def cascading_cut(self, y): 
        z = y.parent 
        if z is not None: 
            if y.mark is False: 
                y.mark = True 
            else: 
                self.cut(y, z) 
                self.cascading_cut(z)

    def items(self):
        for key in self.key_map: 
            yield self.key_map[key]

    def keys(self): 
        for key in self.key_map: 
            yield key 

    def values(self): 
        for item in self.items():
            yield item.value

    def top(self): 
        return self.min_node 

    def size(self): 
        return self.count

    def get_data(self, key): 
        return self.key_map[key].data

    def set_data(self, key, data): 
        self.key_map[key].data = data

    def get_value(self, key): 
        return self.get_item(key).value 

    def set_value(self, key, value): 
        self.key_map[key].value = value

    def get_item(self, key): 
        return self.key_map[key] 

    def set_item(self, key, item): 
        self.key_map[key] = item
    
    def display(self):
        self.display_tree(self) 
    
    def display_tree(self, root, level = 0):
        if root is None: 
            return 

        for current in root.children: 
            print(f"{'    ' * level} {current.key} -> {current.value} {current.order}")
            self.display_tree(current, level + 1)  

    def min(self): 
        if self.type != "min":
            raise Exception("Not a minimum heap.") 
        return self.top().value 

    def max(self): 
        if self.type != "max": 
            raise Exception("Not a maximum heap.") 
        return self.top().value 

    def size(self): 
        return self.count