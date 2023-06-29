""" 
    MULTI-VALUED BINARY-SEARCH TREE MODIFICATION FOR 
    BALANCED BINARY SEARCH TREES
""" 
from .avlt import AVLT 
from .rbt import RBT
from linked_lists.structs.sll import SLL

class MV_BST():
    def __init__(self, **kwargs):
        self.FIFO = 1 
        self.LIFO = 2

        self.driver = kwargs.get("driver", RBT) 
        self.mode = kwargs.get("mode", self.FIFO)
        self.tree = self.driver() 
        
    def insert(self, key, value): 
        item = self.tree.find(key)
        if item is not None: 
            item.value.append(value) 
            return item
        else:
            sll = SLL() 
            sll.append(value)
            return self.tree.insert(key, sll) 

    def delete(self, key): 
        item = self.tree.find(key) 
        if item is not None:
            if item.value.size > 1: 
                if self.mode == self.FIFO: 
                    item.value.delete_head() 
                elif self.mode == self.LIFO: 
                    item.value.delete_tail()
            else:
                self.tree.delete(key) 
            return 1 
        else: 
            return None 

    
    def delete_node(self, node): 
        item = node
        if item is not None:
            if item.value.size > 1: 
                if self.mode == self.FIFO: 
                    item.value.delete_head() 
                elif self.mode == self.LIFO: 
                    item.value.delete_tail()
            else:
                self.tree.delete_node(node) 
            return 1 
        else: 
            return None 

    def get_current_value(self, key): 
        node = self.tree.find(key)
        return self.get_current_node_value(node)
        
    def get_current_node_value(self, node): 
        if node is None: 
            return None

        if self.mode == self.FIFO: 
            return node.value.head.value 
        elif self.mode == self.LIFO: 
            return node.value.tail.value
