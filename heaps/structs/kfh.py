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
        self.degree = 0
        self.mark = False

        self.parent = None 
        self.left = None 
        self.right = None
        self.child = None

    def add_at_end(self, tree): 
        self.children.append(tree)
        self.degree = self.degree + 1 

class KFH: 
    def __init__(self, type_ = "min"): 
        self.trees = [] 
        self.min_node = None 
        self.root_list = None
        self.count = 0 
        self.type = type_
        self.key_no = 0 
        self.key_map = {} 

    def iterate(self, head): 
        node = stop = head 
        flag = False 
        while True: 
            if node == stop and flag is True: 
                break 
            elif node == stop: 
               flag = True 
            yield node 
            node = node.right 
    
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

    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node
            
    def merge_with_child_list(self, parent, node): 
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node
    
    def remove_from_root_list(self, node): 
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left
        
    def remove_from_child_list(self, parent, node): 
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left

    def insert(self, key, value, data = None):
        n = KFH_Item(key, value, data)
        self.insert_node(n)  

    def insert_node(self, node):
        n = node 
        n.left = n.right = n 
        self.key_map[n.key] = n 

        self.merge_with_root_list(n)
        if self.min_node is None or self.comparator(n, self.min_node): 
            self.min_node = n 
        self.count += 1 

    def pop(self):
        z = self.min_node 
        del self.key_map[z.key]
        
        if z is not None: 
            if z.child is not None: 
                # attach child nodes to root list 
                children = [ x for x in self.iterate(z.child) ]
                for i in range(0, len(children)): 
                    self.merge_with_root_list(children[i]) 
                    children[i].parent = None  
            self.remove_from_root_list(z) 
            
            # set new min node in heap 
            if z == z.right: 
                self.min_node = self.root_list = None 
            else: 
                self.min_node = z.right 
                self.consolidate() 
            self.count -= 1
        return z 

    def consolidate(self): 
        A = [None] * self.count 
        nodes = [w for w in self.iterate(self.root_list)]  
        for w in range(0, len(nodes)): 
            x = nodes[w] 
            d = x.degree 
            while A[d] != None: 
                y = A[d]
                if not self.comparator(x, y): 
                    x, y = y, x 
                self.heap_link(y, x) 
                A[d] = None   
                d += 1 
            A[d] = x 
        
        # find new min node - no need to reconstruct 
        # new root list below because root list was iteratively 
        # chaining as we were moving around in the above loop 
        for i in range(0, len(A)): 
            if A[i] is not None: 
                if self.comparator(A[i], self.min_node): 
                    self.min_node = A[i]

    def heap_link(self, y, x): 
        self.remove_from_root_list(y) 
        y.left = y.right = y 
        self.merge_with_child_list(x, y) 
        x.degree += 1 
        y.parent = x 
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
        x = self.get_item(key)
        x.value = value 
        y = x.parent  
        if y is not None and self.comparatro(x, y): 
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
        self.remove_from_child_list(y, x) 
        y.degree -= 1
        self.merge_with_root_list(x) 
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
        self.display_tree(self.root_list) 
    
    def display_tree(self, root, level = 0):
        if root is None: 
            return 

        for current in self.iterate(root): 
            print(f"{'    ' * level} {current.value} {current.degree}")
            self.display_tree(current.child, level + 1)
            current = current.right
            if current is root: 
                break  

    def min(self): 
        if self.type != "min":
            raise Exception("Not a minimum heap.") 
        return self.top().value 

    def max(self): 
        if self.type != "max": 
            raise Exception("Not a maximum heap.") 
        return self.top().value 