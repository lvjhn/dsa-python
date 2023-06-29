""" 
    AVL TREE IMPLEMENTATION (PYTHON)

    NOTES: 
        * reference (slightly modified)
            https://www.programiz.com/dsa/avl-tree
""" 
from linked_lists.structs.sll import SLL 
from linked_lists.structs.dll import DLL 

class AVLT_Node(): 
    def __init__(self, key, **kwargs):
        self.key = key 
        self.values = SLL()
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
        print(f"root: {root.key}")
        if root.left is None and root.right is None: 
            print("c1")
            return root 
        elif root.left is not None and root.right is None: 
            print("c2")
            return root 
        return self.find_max(root.right)

    def left_rotate(self, a): 
        al = None 
        b = None 
        bl = None 
        br = None 
        p = None 

        if a.left: 
            al = a.left 
        if a.right: 
            b = a.right 
        if b.left:
            bl = b.left 
        if b and b.right:
            br = b.right 
        if a.parent: 
            p = a.parent 

        b.left = a 
        if a:
            a.parent = b 
        
        a.left = al
        if al: 
            al.parent = a 

        a.right = bl  
        if bl: 
            bl.parent = a 


        if a is self.root: 
            self.root = b
            b.parent = None

        if p: 
            if p.left is a: 
                p.left = b 
            else: 
                p.right = b 
            b.parent = p
        
        a.height = 1 + max(self.get_height(al), self.get_height(bl)) 
        b.height = 1 + max(self.get_height(a), self.get_height(br))

        return b 

    def right_rotate(self, a): 
        ar = None 
        b = None 
        bl = None 
        br = None 
        p = None 

        if a.right: 
            ar = a.right  
        if a.left: 
            b = a.left 
        if b.left: 
            bl = b.left 
        if b.right: 
            br = b.right
        if a.parent:
            p = a.parent

        b.right = a 
        if a:
            a.parent = b

        a.left = br 
        if br: 
            br.parent = a 

        a.right = ar 
        if ar: 
            ar.parent = a

        if a is self.root: 
            self.root = b
            b.parent = None 
        if p:
            if p.left is a: 
                p.left = b 
            else: 
                p.right = b 
            b.parent = p
        
        a.height = 1 + max(self.get_height(br), self.get_height(ar)) 
        b.height = 1 + max(self.get_height(a), self.get_height(bl))

        return b 

    def left_right_rotate(self, A):
        B = A.left 
        self.left_rotate(B) 
        rr = self.right_rotate(A) 
        return rr
    
    def right_left_rotate(self, A): 
        B = A.right 
        self.right_rotate(B) 
        lr = self.left_rotate(A) 
        return lr 

    def update_height(self, node): 
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))

    def insert(self, key, value): 
        node = AVLT_Node(key) 
        self.insert_node(node, value)

    def insert_node(self, node, value): 
        if self.root is None: 
            self.root = node 
            self.count = 1 
        else: 
            current = self.root 

            while True: 
                if node.key < current.key:
                    if current.left is None:
                        current.left = node 
                        node.values.append(value)
                        node.parent = current 
                        break
                    else: 
                        current = current.left
                 
                elif node.key > current.key: 
                    if current.right is None: 
                        current.right = node 
                        node.values.append(value)
                        node.parent = current 
                        break
                    else:
                        current = current.right

                elif node.key == current.key:
                    current.values.append(value)
                    break

            self.count += 1 
            self.rebalance_insert(node, current)

    def rebalance_insert(self, new_node, current): 
        while current is not None: 
            # update height 
            self.update_height(current) 

            # get balance factor 
            bf = self.get_balance_factor(current) 

            # apply rotation rules
            if bf > 1:
                if new_node.key < current.left.key: 
                    current = self.right_rotate(current)
                else: 
                    current = self.left_right_rotate(current) 
            if bf < -1:
                if new_node.key > current.right.key: 
                    current = self.left_rotate(current) 
                else: 
                    current = self.right_left_rotate(current)

            # continue until root is reached
            current = current.parent 

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

    def delete(self, key, root = None): 
        current = self.find(key, root)

        if current is None: 
            raise Exception(f"{key} is not in tree.")

        self.delete_node(current, root)

    def delete_node(self, node, root = None):
        if root == None: 
            root = self.root

        temp = None 

        if node.left is None: 
            temp = node.right 
        elif node.right is None: 
            temp = node.left 
        else: 
            temp = self.find_min(node.right) 
            temp.left = node.left 
            temp.right = self.delete(temp.key, node.right) 
        
        if node is self.root: 
            self.root = temp
        else: 
            parent = node.parent 
            if parent.left is node: 
                parent.left = temp 
            else: 
                parent.right = temp

        self.rebalance_delete(temp)

    def rebalance_delete(self, current):
        while current is None:
            # update height 
            self.update_height(current) 

            # get balance factor 
            bf = self.get_balance_factor(current) 

            # apply rotation rules
            if bf > 1:
                if self.get_balance_factor(current.left) >= 0:
                    current = self.right_rotate(current)
                else: 
                    current = self.left_right_rotate(current) 
            if bf < -1:
                if self.get_balance_factor(current.right) <= 0: 
                    current = self.left_rotate(current) 
                else: 
                    current = self.right_left_rotate(current)

            # continue unless top is reached
            current = current.parent 

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
            f"|v|: {len(root.values)}" 
        )
        
        self.display_node(root.left, indent + 1, "left")
        self.display_node(root.right, indent + 1, "right")
