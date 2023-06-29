from .structs.rbt import RBT 
from binarytree import Node 


def extract_tree(tree): 
    root = Node(tree.root.key) 

    def extract_subtree(root, parent, orient): 
        if root is tree.TNULL or root is None: 
            return

        if orient == "left": 
            _node = Node(root.key)
            parent.left = _node
        elif orient == "right": 
            _node = Node(root.key) 
            parent.right = _node

        extract_subtree(root.left, _node, "left") 
        extract_subtree(root.right, _node, "right")            

    extract_subtree(tree.root.left, root, "left")
    extract_subtree(tree.root.right, root, "right")

    return root 


N_ITEMS = 20

rbt = RBT() 

for i in range(N_ITEMS): 
    rbt.insert(i, i)

print(rbt.size())

rbt.delete(12)

print(rbt.size())

rbt.display()

print(rbt.find_max(rbt.root).key)

print(extract_tree(rbt))

