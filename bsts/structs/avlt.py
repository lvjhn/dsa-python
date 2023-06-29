""" 
    AVL TREE IMPLEMENTATION (PYTHON)

    NOTES: 
        * reference (slightly modified)
            https://www.programiz.com/dsa/avl-tree
""" 

class AVLT_Node(): 
    def __init__(self, key, value):
        self.key = key 
        self.value = value

        self.height = 1

        self.parent = None 
        self.left = None 
        self.right = None 
    
class AVLT: 
    def __init__(self): 
        self.count = 0 
        self.root = None 

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

    def find_min(self, root): 
        if root.left is None and root.right is None: 
            return root 
        elif root.left is None and root.right is not None: 
            return root 
        return self.find_min(root.left)

    def find_max(self, root): 
        if root.left is None and root.right is None: 
            return root 
        elif root.left is not None and root.right is None: 
            return root 
        return self.find_max(root.right)

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

        return y

    def right_rotate(self, a): 
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

        return y

    def left_right_rotate(self, A):
        B = A.left 
        self.left_rotate(B) 
        return self.right_rotate(A)

    def right_left_rotate(self, A): 
        B = A.right 
        self.right_rotate(B) 
        return self.left_rotate(A)

    def update_height(self, node): 
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))


    def find(self, key, root = None): 
        if root == None: 
            current = self.root 
        else: 
            current = root 

        while current is not None: 
            if key < current.key:
                current = current.left
            elif key > current.key: 
                current = current.right
            else: 
                return current 
        return None

    def insert(self, key, value): 
        node = AVLT_Node(key, value) 
        self.insert_node(self.root, node, None)
        self.count += 1

    def insert_node(self, root, node, parent): 
        # find the correct location and insert the node
        if self.root is None: 
            self.root = node
            return node
        elif not root:
            node.parent = parent
            return node
        elif node.key < root.key:
            root.left = self.insert_node(root.left, node, root)
        else:
            root.right = self.insert_node(root.right, node, root)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

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
        self.delete_node(self.root, key)
        self.count -= 1

    def delete_node(self, root, key):
        # find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
           
            else:
                temp = self.find_min(root.right)
                temp.left = root.left
                temp.right = self.delete_node(root.right,temp.key)

            if root is self.root: 
                self.root = temp
            else: 
                if root.parent.left is root: 
                    root.parent.left = temp 
                else: 
                    root.parent.right = temp
        
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

    def display(self): 
        self.display_node(self.root, 0, "root")

    def display_node(self, root, indent, orient):
        if root is None:
            return 

        print(
            "    " * indent + \
            f"{orient} : {root.key} -> " +
            f"h: {self.get_height(root)}, " + 
            f"bf: {self.get_balance_factor(root)}, " + 
            f"v: {root.value}" 
        )
        
        self.display_node(root.left, indent + 1, "left")
        self.display_node(root.right, indent + 1, "right")
