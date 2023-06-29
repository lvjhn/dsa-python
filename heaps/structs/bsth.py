""" 
    CUSTOM HEAP USING BALANCED-BINARY SEARCH TREE (RBT)
"""
from bsts.structs.mv_bst import MV_BST
from bsts.structs.rbt import RBT


class BSTH: 
    def __init__(self, **kwargs):
        self.key_data = {} 
        self.value_tree = kwargs.get("value_tree", MV_BST()) 

        self.min_node_ = None 
        self.max_node_ = None 
        self.min_key = None 
        self.max_key = None


    def min_node(self): 
        return self.min_node_ 
    
    def max_node(self): 
        return self.max_node_ 
    
    def insert(self, key, value, data = None):
        if key in self.key_data:
            raise Exception(f"Key {key} is already in the heap.")

        value_node = self.value_tree.insert(value, key) 
        self.key_data[key] = [value_node, data]
         
        self.update_min()
        self.update_max()
            
    def delete(self, key):
        key_data = self.key_data[key]
        value_node = key_data[0]
        
        del self.key_data[key]

        self.value_tree.delete_node(value_node) 
        
        self.update_min()
        self.update_max()

    def update(self, key, value):
        key_data = self.key_data[key]
        value_node = key_data[0]

        self.delete(key)
        self.insert(key, value, key_data[1]) 

        self.update_min()
        self.update_max()
        
    def get_item(self, key): 
        key_data = self.key_data[key]
        value_node = key_data[0] 
        data = key_data[1]
        return (key, value_node, value_node.key, data)
     
    def update_min(self): 
        self.min_node_ = \
            self.value_tree.tree.find_min(self.value_tree.tree.root)
        
        curr_key = \
            self.value_tree.get_current_node_value(self.min_node_) 

        if curr_key is None: 
            self.min_key = None 
        else: 
            self.min_key = curr_key


    def update_max(self): 
        self.max_node_ = \
            self.value_tree.tree.find_max(self.value_tree.tree.root)

        curr_key = \
            self.value_tree.get_current_node_value(self.max_node_) 

        if curr_key is None: 
            self.max_key = None 
        else: 
            self.max_key = curr_key


    def pop_min(self): 
        self.delete(self.min_key)
    
    def pop_max(self): 
        self.delete(self.max_key)

    def n_values(self): 
        return self.value_tree.tree.size() 
    
    def n_keys(self): 
        return len(self.key_data)

    def min(self): 
        return self.min_node_.key

    def max(self): 
        return self.max_node_.key

    def display(self): 
        for item in self.key_data:
            print(f"{item} -> {self.key_data[item]}")
        self.value_tree.tree.display() 

    def size(self): 
        return self.n_keys()