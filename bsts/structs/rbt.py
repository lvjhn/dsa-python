""" 
    ##########################################
    # RED-BLACK TREE IMPLEMENTATION [PYTHON] #
    ##########################################

    NOTES 
        * main source: programiz.com (modified implementation)
        * does not require other files
		* printable / narrow width 

    API 
        RBT_Node 
            Properties 
                - key 
                - value 
                - parent 
                - left 
                - right 
                - color 
        
        RBT 
            Properties 
                - TNULL 
                - root 
                - count 
            
            Utility Methods 
                - size() 
                - find_min(root)  
                - find_max(root) 
                - update_height(node)
                - find(key, root)
                - transplant(u, v)
                - rebalance_insert(k)
                - rebalance_delete(k)
                - display() 
                - display_node(root, indent, orient) 
                - prev(root)
                - next(root)

            Rotation Methods
                - left_rotate(x) 
                - right_rotate(x)
                - left_right_rotate(A) 
                - right_left_rotate(A) 
            
            Main Operations 
                - insert(key, value) 
                - insert_node(root, node, parent) 
                - delete(key) 
                - delete_node(root, key)
                - clear()
                - update(key, value)
""" 


class RBT_Node():
    def __init__(self, key, value):
        self.key = key 
        self.value = value

        self.parent = None
        self.left = None
        self.right = None
        
        self.color = 1
    
class RBT():
    def __init__(self):
        self.TNULL = RBT_Node(None, None)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.count = 0

    #
    # UTILITY METHODS
    #

    def size(self): 
        return self.count 

    def find(self, key, root = None): 
        if root is None: 
            current = self.root 
        else: 
            current = root 

        while current is not self.TNULL: 
            if key < current.key:
                current = current.left
            elif key > current.key: 
                current = current.right
            else: 
                return current 
                
        return None

    def find_min(self, root): 
        if root is self.TNULL: 
            return None 

        if root.left is self.TNULL and root.right is self.TNULL: 
            return root 
        elif root.left is self.TNULL and root.right is not self.TNULL: 
            return root 

        return self.find_min(root.left)

    def find_max(self, root): 
        if root is self.TNULL: 
            return None 

        if root.left is self.TNULL and root.right is self.TNULL: 
            return root 
        elif root.left is not self.TNULL and root.right is self.TNULL: 
            return root 

        return self.find_max(root.right)
      
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def rebalance_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    
    def rebalance_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def display(self): 
        self.display_node(self.root, 0, "root")

    def display_node(self, root, indent, orient):
        if root is self.TNULL:
            return 

        print(
            "    " * indent + \
            f"{orient} : {root.key} -> " +
            f"c: {root.color}, " + 
            f"v: {root.value}, " +
            f"p: {root.parent.key if root.parent else None}" 
        )
        
        self.display_node(root.left, indent + 1, "left")
        self.display_node(root.right, indent + 1, "right")
    
    def iterate(self): 
        def inorder(node):
            if node.left is not self.TNULL: 
                yield from inorder(node.left) 
            yield node
            if node.right is not self.TNULL:
                yield from inorder(node.right)             
        return inorder(self.root)

    def keys(self): 
        for item in self.iterate(): 
            yield item.key

    def values(self): 
        for item in self.iterate(): 
            yield item.value 

    def prev(self, key): 
        node = self.find(key) 
        
        if node.left is not self.TNULL:  
            return self.find_max(node.left)

        if node.left is self.TNULL: 
            if node.parent.right is node: 
                return node.parent   
            else: 
                current = node.parent
                while True: 
                    if current.parent.right is current: 
                        break
                    current = current.parent
                    if current is self.root: 
                        return None  
                return current.parent 

        return None 


    def next(self, key): 
        node = self.find(key) 
        
        if node.right is not self.TNULL:  
            return self.find_min(node.right)

        if node.right is self.TNULL: 
            if node.parent.left is node: 
                return node.parent   
            else: 
                current = node.parent 
                while True: 
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
        if y.left != self.TNULL:
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

        return y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
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

        return y

    #
    # MAIN OPERATIONS
    # 

    def insert(self, key, value):
        node = RBT_Node(key, value)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        self.insert_node(node)
        self.count += 1


    def insert_node(self, node): 
        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return node

        if node.parent.parent == None:
            return node

        self.rebalance_insert(node)

        return node
        

    def delete(self, key): 
        self.delete_key(self.root, key)
        self.count -= 1

    def delete_key(self, node, key):
        z = self.TNULL

        while node is not self.TNULL:
            if node.key == key:
                z = node
                break            
            elif node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left

        if z == self.TNULL:
            print(f"{key} is not in the tree")
            return

        return self.delete_node(z)

    def delete_node(self, z): 
        y = z
        y_original_color = y.color

        if z.left is self.TNULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.TNULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.find_min(z.right)
            y_original_color = y.color

            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 0:
            self.rebalance_delete(x)

    def clear(self): 
        self.root = None 
        self.count = 0  

    def update(self, key, value): 
        if self.find(key) is None:
            raise Exception(f"{key} is not in tree.")
        self.delete(key)
        self.insert(key, value)