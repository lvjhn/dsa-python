""" 
    RED-BLACK TREE IMPLEMENTATION (PYTHON)

    NOTES: 
        * reference (slightly modified)
            https://www.programiz.com/dsa/red-black-tree

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

    def size(self): 
        return self.count 

    def find_min(self, root): 
        if root.left is self.TNULL and root.right is self.TNULL: 
            return root 
        elif root.left is self.TNULL and root.right is not self.TNULL: 
            return root 
        return self.find_min(root.left)

    def find_max(self, root): 
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

    def insert(self, key, value):
        node = RBT_Node(key, value)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        self.count += 1

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
            return

        if node.parent.parent == None:
            return

        self.rebalance_insert(node)
        

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

    def delete(self, key): 
        self.delete_node(self.root, key)
        self.count -= 1

    def delete_node(self, node, key):
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
            f"v: {root.value}" 
        )
        
        self.display_node(root.left, indent + 1, "left")
        self.display_node(root.right, indent + 1, "right")
