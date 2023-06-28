''' 
    KEYED FIBONACCI-HEAP IMPLEMENTATION (PYTHON)
    (Modified Fibonacci-Heap with Custom Keys)

    Notes: 
		* isolated
			- does not depend on third-party packages or other files 
			- can be used as is
        
        * printable / narrow width

        * reference (slightly modified implementation)
            - https://www.programiz.com/dsa/fibonacci-heap
            - https://www.programiz.com/dsa/decrease-key-and-delete-node-from-a-fibonacci-heap

		* implements common operations
            - comparator(a, b) 
            - swap_key_map(i, j)
            - insert(key, value)
            - delete() 
            - consolidate()
            - update(key, new_value)
            - update_a(key, value)
            - update_b(key, value)  
            - keys()
            - values()
            - top()
            - size()
''' 
import math 

class KFH_Item: 
    def __init__(self, key, value, data = None): 
        self.key = key 
        self.value = value 
        self.data = data
        self.order = 0
        self.mark = False

        self.parent = None 
        self.left = None 
        self.right = None
        self.child = None

    def add_at_end(self, tree): 
        self.children.append(tree)
        self.order = self.order + 1 

class KFH: 
    def __init__(self, type_ = "min"): 
        self.trees = [] 
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
        new_node = KFH_Item(key, value, data)
        self.insert_node(new_node)

    def insert_node(self, node):
        self.key_map[node.key] = node

        min_node = self.min_node

        if min_node is None:
            self.min_node = node
            min_node = self.min_node
            min_node.left = min_node 
            min_node.right = min_node 
        else: 
            node.right = min_node 
            node.left = min_node.left 
            min_node.left.right = node 
            min_node.left = node

            if self.comparator(node, min_node): 
                self.min_node = node  

        self.count += 1 

    def pop(self):
        smallest = self.min_node 

        del self.key_map[smallest.key]

        if smallest is not None: 
            child = smallest.child 
            start = child
            right = None 

            # transfer children of smallest element 
            if child is not None:
                while True:
                    right = child.right 
                    self.insert_node(child)
                    self.count -= 1 
                    child.parent = None 
                    child = right 
                    if child is None and child is start: 
                        break 
            
            # remove smallest element 
            smallest.left.right = smallest.right 
            smallest.right.left = smallest.left 
            smallest.child = None 

            # if heap is to be emptied
            if smallest is smallest.right: 
                self.min_node = None 
            else: 
                self.min_node = smallest.right 
                self.consolidate() 
            
            self.count -= 1 
            return smallest 
        else:
            raise Exception("Heap is empty.")

        return None

    def delete(self, key): 
        pass

    def consolidate(self): 
        aux = (int(math.log2(self.count)) + 1) * [None]
        node = self.min_node 
        
    
    def link(self, y, x): 
        y.left.right = y.right 
        y.right.left = y.left 

        child = x.child 

        # add y to x's children
        if child is None: 
            y.right = y 
            y.left = y  
        
        else: 
            y.right = child 
            y.left = child.left              
            child.left.right = y 
            child.left = y 

        # attach and y and x together
        y.parent = x 
        x.child = y 
        x.order += 1 
        y.mark = False 
        
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
        item = self.key_map[key] 
        item.value = value 
        parent = item.parent  
        
        if parent is not None and self.comparator(item, parent): 
            self.cut(item, parent) 
            self.cascading_cut(parent)

        if self.comparator(item, self.min_node): 
            self.min_node = item 

    def update_b(self, key, value): 
        pass 

    def cut(self, x, y): 
        x.right.left = x.left 
        x.left.right = x.right 
        y.order = y.order - 1 
        
        x.right = None 
        x.left = None 
        self.insert_node(x)
        self.count -=1  
        x.parent = none 
        x.mark = False 

    def cascading_cut(self, y): 
        z = y.parent 
        if z is not None: 
            if y.mark == False: 
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
        self.display_tree(self.min_node) 
    
    def display_tree(self, root, level = 0):
        if root is None: 
            return 

        current = root 

        while True:     
            print(f"{'    ' * level} {current.value} {current.order}")
            self.display_tree(current.child, level + 1)
            current = current.right
            if current is root: 
                break  
            