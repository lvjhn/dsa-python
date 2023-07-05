""" 
    ####################################
    # AVL TREE IMPLEMENTATION (PYTHON) #
    ####################################

    NOTES 
        * main source: programiz.com (modified implementation)
        * does not require other files
		* printable / narrow width 

    API 
        AVLT_Node 
            - key 
            - value 
            - height 
            - parent 
            - left 
            - right 
            - n_desc

        AVLT 
            Properties 
                - count 
                - root 

            Utility Methods
                - at(index)
                - index(key)

                - size() 
                - get_height(root) 
                - get_balance_factor(root) 
                - get_n_desc(root)

                - find(key, root)
                - find_min(root)  
                - find_max(root) 
                
                - update_height(node)

                - display() 
                - display_node(root, indent, orient)
                
                - iterate()
                - keys()
                - values()
                
                - key_prev(key)
                - prev(node)
                - key_next(next)
                - next(node)
             
            Rotation Methods
                - left_rotate(x) 
                - right_rotate(x)
                - left_right_rotate(A) 
                - right_left_rotate(A) 

            Threaded Binary Tree Methods 
                - set_prev(node, prev)
                - set_next(node, next)
            
            Main Operations 
                - insert(key, value) 
                - insert_node(root, node, parent) 
                
                - update(key, value)

                - delete(key) 
                - delete_node(root, key)
                
                - clear()

""" 

class AVLT_Node(): 
    def __init__(self, key, value, **kwargs):
        self.key = key 
        self.value = value

        self.height = 1
        self.n_desc = 1

        self.parent = None 
        
        self.left = None 
        self.right = None

        self.prev = None
        self.next = None 

class AVLT: 
    def __init__(self, **kwargs): 
        self.count = 0 
        self.root = None      

    #
    # UTILITY METHODS
    #

    def comparator(self, a, b): 
        return a.key < b.key 

    def equals(self, a, b): 
        return a.key == b.key

    def at(self, index): 
        current = self.root 
        lo = 0
        hi = self.size() - 1

        while current.n_desc > 1: 
            if current.left: 
                mid = lo + current.left.n_desc
            elif current.right: 
                mid = lo
            
            left = (lo, mid)
            right = (mid + 1, hi) 

            if index == mid: 
                return current 
            
            elif index >= left[0] and index <= left[1]: 
                hi = mid - 1
                current = current.left

            elif index >= right[0] and index <= right[1]:
                lo = mid + 1
                current = current.right
 
        return current 

   
    def index(self, key): 
        current = self.root 
        lo = 0
        hi = self.size() - 1

        key_node = AVLT_Node(key, None)

        while current is not None: 
            if current.left: 
                mid = lo + current.left.n_desc
            elif current.right: 
                mid = lo
            
            left = (lo, mid)
            right = (mid + 1, hi) 

            if current.n_desc == 1 and key == current.key: 
                return lo

            elif key == current.key: 
                return mid 
            
            elif self.comparator(key_node, current): 
                hi = mid - 1
                current = current.left

            elif not self.comparator(key_node, current):
                lo = mid + 1
                current = current.right
 
        return None 

    def size(self): 
        return self.count 

    def get_height(self, root): 
        if root is None:
            return 0 
        return root.height 

    def get_balance_factor(self, root): 
        if root is None: 
            return 0    
        return self.get_height(root.left) - self.get_height(root.right)

    def get_n_desc(self, root): 
        if root is None: 
            return 0 
        return root.n_desc 

    def find(self, key, root = None): 
        if self.root is None: 
            return None 
            
        if root is None: 
            current = self.root 
        else: 
            current = root 

        key_node = AVLT_Node(key, None)

        while current is not None: 
            if self.equals(key_node, current): 
                return current
            elif self.comparator(key_node, current):
                current = current.left
            elif not self.comparator(key_node, current): 
                current = current.right
    
        return None

    def find_min(self, root): 
        if root is None: 
            return None 

        if root.left is None and root.right is None: 
            return root 
        elif root.left is None and root.right is not None: 
            return root 

        return self.find_min(root.left)

    def find_max(self, root): 
        if root is None: 
            return None 

        if root.left is None and root.right is None: 
            return root 
        elif root.left is not None and root.right is None: 
            return root 

        return self.find_max(root.right)

    
    def update_height(self, node): 
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))

    def display(self): 
        self.display_node(self.root, 0, "root")

    def display_node(self, root, indent, orient):
        if root is None:
            return 

        print(
            "    " * indent + 
            f"{orient} : {root.key} -> " +
            f"h: {self.get_height(root)}, " + 
            f"bf: {self.get_balance_factor(root)}, " + 
            f"v: {root.value}, " + 
            f"pt: {root.parent.key if root.parent else None}, " + 
            f"nd: {root.n_desc}, " + 
            f"l: {root.left.key if root.left else None}, " + 
            f"r: {root.right.key if root.right else None}, " + 
            f"p: {root.prev.key if root.prev else None}, " +
            f"n: {root.next.key if root.next else None}" 
        )
        
        self.display_node(root.left, indent + 1, "left")
        self.display_node(root.right, indent + 1, "right")
    
    def iterate(self): 
        current = self.find_min(self.root) 
        while current is not None: 
            yield current 
            current = current.next
        return None
        
    def keys(self): 
        for item in self.iterate(): 
            yield item.key

    def values(self): 
        for item in self.iterate(): 
            yield item.value 

    def key_prev(self, key): 
        node = self.find(key)
        return self.prev(node)

    def prev(self, node):   
        if self.size() == 1: 
            return None

        if node.left is not None:  
            return self.find_max(node.left)

        if node.left is None: 
            if node.parent.right is node: 
                return node.parent   
            else: 
                current = node.parent
                while True and current.parent is not None: 
                    if current.parent.right is current: 
                        break
                    current = current.parent
                    if current is self.root: 
                        return None  
                return current.parent 

        return None 

    def key_next(self, key): 
        node = self.find(key)
        return self.next(node)

    def next(self, node): 
        if self.size() == 1: 
            return None

        if node.right is not None:  
            return self.find_min(node.right)

        if node.right is None: 
            if node.parent.left is node: 
                return node.parent   
            else: 
                current = node.parent 
                while True and current.parent is not None: 
                    if current.parent.left is current: 
                        break
                    current = current.parent
                    if current is self.root: 
                        return None  
                return current.parent 

        return None 


    #
    # ROTATION METHODS
    #

    def left_rotate(self, x): 
        y = x.right

        x.right = y.left

        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

        x.height = \
            1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = \
            1 + max(self.get_height(y.left), self.get_height(y.right))
        
        x.n_desc = \
            1 + self.get_n_desc(x.left) + self.get_n_desc(x.right) 
        y.n_desc = \
            1 + self.get_n_desc(y.left) + self.get_n_desc(y.right)

        max_right = self.find_min(x.right)
        
        if max_right: 
            self.set_next(max_right, y) 

        return y

    def right_rotate(self, x): 
        y = x.left
        x.left = y.right

        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        x.height = \
            1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = \
            1 + max(self.get_height(y.left), self.get_height(y.right))
                
        x.n_desc = \
            1 + self.get_n_desc(x.left) + self.get_n_desc(x.right) 
        y.n_desc = \
            1 + self.get_n_desc(y.left) + self.get_n_desc(y.right)
        
        min_left = self.find_min(x.left)
        
        if min_left: 
            self.set_prev(min_left, y)

        return y

    def left_right_rotate(self, A):
        B = A.left 
        self.left_rotate(B) 
        return self.right_rotate(A)

    def right_left_rotate(self, A): 
        B = A.right 
        self.right_rotate(B) 
        return self.left_rotate(A)

    #
    # THREADED BINARY TREE METHODS 
    # 
    
    def set_prev(self, node, prev): 
        node.prev = prev 
        if prev:
            prev.next = node 

    def set_next(self, node, next_): 
        node.next = next_ 
        if next_:
            next_.prev = node 

    #
    # MAIN OPERATIONS 
    # 

    def insert(self, key, value): 
        node = AVLT_Node(key, value) 
        
        self.insert_node(self.root, node, None)
        self.count += 1

        self.set_prev(node, self.prev(node))
        self.set_next(node, self.next(node))

        return node

    def insert_node(self, root, node, parent): 
        # find the correct location and insert the node
        if self.root is None: 
            self.root = node
            return node
        elif not root:
            node.parent = parent
            return node
        elif self.comparator(node, root):
            root.left = self.insert_node(root.left, node, root)
        else:
            root.right = self.insert_node(root.right, node, root)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        root.n_desc = 1 + self.get_n_desc(root.left) + \
                          self.get_n_desc(root.right)

        # update the balance factor and balance the tree
        bf = self.get_balance_factor(root)
        if bf > 1:
            if node.key < root.left.key:
                return self.right_rotate(root)
            else:
                return self.left_right_rotate(root)

        if bf < -1:
            if node.key > root.right.key:
                return self.left_rotate(root)
            else:
                return self.right_left_rotate(root)

        return root

    def delete(self, key): 
        key_node = AVLT_Node(key, None)
        self.delete_node(self.root, key_node)
        self.count -= 1

    def delete_node(self, root, key_node):
        # find the node to be deleted and remove it
        if not root:
            return root

        if self.equals(root, key_node):
            if root.left is None and root.right is not None:
                temp = root.right
                temp.parent = root.parent
                
                self.set_prev(temp, self.prev(temp))
                self.set_next(temp, self.next(temp))
                
                return temp
            
            elif root.right is None and root.left is not None:
                temp = root.left
                temp.parent = root.parent

                self.set_prev(temp, self.prev(temp))
                self.set_next(temp, self.next(temp)) 

                return temp

            elif root.left is None and root.right is None: 
                
                if root.parent.left is root: 
                    root.parent.left = None 
                else: 
                    root.parent.right = None
   
                self.set_prev(root.parent, self.prev(root.parent))
                self.set_next(root.parent, self.next(root.parent))

                return   
            else:
                temp = self.find_min(root.right)
                temp.right = self.delete_node(root.right, temp)
                temp.left = root.left 

                if root.left: 
                    root.left.parent = temp

                if root is self.root: 
                    self.root = temp
                else: 
                    if root.parent.left is root: 
                        root.parent.left = temp 
                    else: 
                        root.parent.right = temp
                    
                    temp.parent = root.parent   

                self.set_prev(temp, self.prev(temp)) 
                self.set_next(temp, self.next(temp))

                root = temp

        elif self.comparator(key_node, root):
            root.left = self.delete_node(root.left, key_node)
        elif not self.comparator(key_node, root):
            root.right = self.delete_node(root.right, key_node)
        
        if root is None:
            return root

        # update the balance factor of nodes
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        
        bf = self.get_balance_factor(root)

        # balance the tree
        if bf > 1:
            if self.get_balance_factor(root.left) >= 0:
                return self.right_rotate(root)
            else:
                return self.left_right_rotate(root)
        if bf < -1:
            if self.get_balance_factor(root.right) <= 0:
                return self.left_rotate(root)
            else:
                return self.right_left_rotate(root)

        return root 

    def clear(self): 
        self.root = None 
        self.count = 0

    def update(self, key, value): 
        if self.find(key) is None:
            raise Exception(f"{key} is not in tree.")
        self.delete(key)
        self.insert(key, value)