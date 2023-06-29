from .structs.avlt import AVLT 
from binarytree import Node 

def extract_tree(tree): 
    root = Node(tree.root.key) 

    def extract_subtree(root, parent, orient): 
        if root is None: 
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


N_ITEMS = 20

avlt = AVLT() 

for i in range(N_ITEMS): 
    avlt.insert(i, i)

print(avlt.size())

avlt.delete(12)

print(avlt.size())

avlt.display()

print(extract_tree(avlt))