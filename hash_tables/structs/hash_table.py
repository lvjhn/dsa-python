'''
    DOUBLY LINKED-LIST IMPLEMENTATION (PYTHON)

    Notes: 
		* isolated
			- does not depend on third-party packages or other files 
			- can be used as is
        
        * printable / narrow width

        * references: 
            - slightly modified from:
              https://www.programiz.com/dsa/hash-table

		* implements common operations
            Public Methods
            - set_item(key, val) 
            - insert_item(key, val)
            - update_item(key, val)
            - remove_item(key, val) 
            - has_item(key)
            - get_item(key) 
            - clear(key, val) 

            Internal Methods 
            - rehash() 
            - expand()
            - shrink()  
''' 
import math 

#############
# CONSTANTS #
#############

# --- COLLISION RESOLUTION --- # 
CHAINING_RESOLUTION = 1 
LINEAR_PROBING_RESOLUTION = 2 
QUADRATIC_PROBING_RESOLUTION = 3 
DOUBLE_HASHING_RESOLUTION = 4 

OPEN_ADDRESSING_MODES = [
    LINEAR_PROBING_RESOLUTION,
    QUADRATIC_PROBING_RESOLUTION, 
    DOUBLE_HASHING_RESOLUTION
]

# --- HASH FUNCTIONS --- # 
DIVISION_METHOD = 4
MULTIPLICATION_METHOD = 5  

#####################
# UTILITY FUNCTIONS #
##################### 

def log2(x):
    return x.bit_length() + 2



class HashTable: 
    def __init__(self, init_cap = 2, **kwargs):
        
        # meta config
        self.size = 0
        self.resolution_mode = \
            kwargs.get("resolution_mode", CHAINING_RESOLUTION) 

        #
        # Source: https://en.wikipedia.org/wiki/Quadratic_probing
        #    * 1/2 is a good c1 and c2 val for 2^n
        #
        self.quadratic_probe_c1 = 1/2
        self.quadratic_probe_c2 = 1/2 

        #
        # Source: https://www.programiz.com/dsa/hash-table
        #    * (sqrt(5) - 1) / 2 is a good val for A
        # 
        self.multiplication_hash_a = ((5 ** 1/2) - 1) / 2
         
        # 
        # Hash Function Configuration
        # 

        self.hash_function_a = \
            kwargs.get("hash_fn_a", DIVISION_METHOD) 
        self.hash_function_b = \
            kwargs.get("hash_fn_b", MULTIPLICATION_METHOD)

        self.hash_fn_a = None 
        self.hash_fn_b = None 
        
        self.setup_hash_fns()

        #
        # Threshold Configuration (for Chaining)
        # 
        self.threshold_mode = "constant"
        self.threshold_factor = 10

        #
        # Load Factor Configuration (for Open Addressing)
        # 
        self.load_factor = 0.8

        # main table 
        self.table = [self.make_container() for i in range(init_cap)]

    def init_cap(n): 
        x = math.ceil(log2(n))
        return 2 ** (x + 2)

    def map_hash_fn(self, idx): 
        if idx == DIVISION_METHOD: 
            return self.division_hash
        elif idx == MULTIPLICATION_METHOD:
            return self.multiplication_hash 
        
    def setup_hash_fns(self):      
        self.hash_fn_a = self.map_hash_fn(self.hash_function_a)
        self.hash_fn_b = self.map_hash_fn(self.hash_function_b)

    def threshold(self):
        tf = self.threshold_factor  
        tm = self.threshold_mode 
        if tm == "log":
            return int(tf * log2(self.capacity()))
        elif tm == "constant": 
            return tf

    def capacity(self):
        return len(self.table)

    def make_container(self): 
        if self.resolution_mode == CHAINING_RESOLUTION: 
            return SLL() 
        elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
            return None
 
    def make_table(self, capacity): 
        table = [] 
        for i in range(capacity): 
            table.append(self.make_container())
        return table

    def rehash(self, aux): 
        # handle chaining resolution mode
        if self.resolution_mode == CHAINING_RESOLUTION:     
            for container in self.table: 
                current = container.head 
                while current is not None: 
                    aux.set_item(current.value[0], current.value[1])
                    current = current.next 

        # handle open addressing mode
        elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
            for container in self.table:
                if container is not None:
                    aux.set_item(container[0], container[1])

        self.table = aux.table

    def expand(self): 
        # make an auxiliary hash table 
        aux = HashTable(
            self.capacity() * 2, 
            resolution_mode = self.resolution_mode,
            hash_fn_a=self.hash_function_a, 
            hash_fn_b=self.hash_function_b
        )

        self.rehash(aux)

    def shrink(self): 
        print(f"Should shrink from {self.capacity()}")
        # make an auxiliary hash table 
        aux = HashTable(
            self.capacity() // 2, 
            resolution_mode=self.resolution_mode,
            hash_fn_a=self.hash_function_a, 
            hash_fn_b=self.hash_function_b
        )

        self.rehash(aux)

    def resolver(self): 
        if self.resolution_mode == LINEAR_PROBING_RESOLUTION: 
            return self.linear_probe 
        elif self.resolution_mode == QUADRATIC_PROBING_RESOLUTION:
            return self.quadratic_probe 
        elif self.resolution_mode == DOUBLE_HASHING_RESOLUTION: 
            return self.double_hashing 
        
    # --- Open Addressing Functions --- # 
    def linear_probe(self, k, i): 
        m = self.capacity()
        hf = self.hash_fn_a
        return int((hf(k) + i) % m)

    def quadratic_probe(self, k, i): 
        m = self.capacity()
        hf = self.hash_fn_a
        c1 = self.quadratic_probe_c1 
        c2 = self.quadratic_probe_c2
        return int((hf(k) + (c1 * i) + (c2 * (i << 1))) % m)

    def double_hashing(self, k, i):
        m = self.capacity()  
        hf1 = self.hash_fn_a 
        hf2 = self.hash_fn_b 
        return int((hf1(k) + i * hf2(k)) % m)

    # --- Hash Functions --- # 
    def division_hash(self, k):
        k = int(k)
        m = self.capacity()
        return k % m

    def multiplication_hash(self, k):
        k = int(k)
        m = self.capacity()
        A = self.multiplication_hash_a  
        return int(m * ((k * A) % 1))

    # 
    # MAIN OPERATIONS 
    # 
    def set_item(self, key, val):   
        if self.has_item(key): 
            self.update_item(key, val)
        else: 
            self.insert_item(key, val)

    def insert_item(self, key, val):
        if self.resolution_mode == CHAINING_RESOLUTION: 
            index = self.hash_fn_a(key)  
            container = self.table[index] 
            container.append([key, val])

            self.size += 1

            # expand when container size reach threshold
            if container.size >= self.threshold(): 
                self.expand()

        elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
            i = 0 

            resolver = self.resolver()
            index = None 
            
            while True: 
                index = resolver(key, i)
                if self.table[index] is None: 
                    break 
                i += 1

            self.table[index] = (key, val) 
            self.size += 1 

            # expand when list reaches maximum capacity
            if self.size >= self.capacity() * self.load_factor:
                self.expand()  

        else: 
            error = "Unknown resolution mode when inserting item."
            raise Exception(error)
    
    def update_item(self, key, val): 
        if not self.has_item(key):
            raise Exception("Item not in hash table.") 
        else: 
            search = self.search(key) 
            if self.resolution_mode == CHAINING_RESOLUTION: 
                self.table[search[1]].at(search[2]).value[1] = val
            elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
                self.table[search[1]][1] = val 

    def remove_item(self, key):
        if not self.has_item(key): 
            raise Exception("Item not in hash table.") 
        else: 
            # remove item from hash table
            search = self.search(key)
            
            if self.resolution_mode == CHAINING_RESOLUTION: 
                self.table[search[1]].delete(search[2])
            elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
                self.table[search[1]] = None
            
            
            self.size -= 1

            # attempt to shrink  hash table
            threshold = None

            if self.resolution_mode == CHAINING_RESOLUTION: 
                threshold = (self.capacity() * self.threshold()) // 2
            elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
                threshold = self.capacity() * self.load_factor() 

            if self.size < self.threshold(): 
                self.shrink()


    def has_item(self, key): 
        if self.search(key): 
            return True 
        else: 
            return False 

    def search(self, key): 
        if self.resolution_mode == CHAINING_RESOLUTION: 
            index = self.hash_fn_a(key)  
            container = self.table[index] 
            current = container.head 
            i = 0 
            while current is not None: 
                if current.value[0] == key: 
                    return current.value, index, i
                current = current.next
                i += 1
            return None  

        elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
            i = 0 

            resolver = self.resolver()
            index = None 

            while i < self.capacity(): 
                index = resolver(key, i)
                
                if self.table[index] is not None and \
                   self.table[index][0] == key: 
                    return self.table[index], index 

                i += 1

            return None 

    def clear(self):
        self.table = self.make_table(self.capacity()) 
        self.size = 0

    def traverse(self, cb): 
        if self.resolution_mode == CHAINING_RESOLUTION: 
            i = 0 
            idx = 0
            for container in self.table: 
                current = container.head
                j = 0
                while current is not None: 
                    res = cb(current.value, i, j, idx)
                    if res: return res
                    current = current.next 
                    j += 1
                    idx += 1 
                i += 1
            return None

        elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
            i = 0
            idx = 0
            j = None
            for item in self.table: 
                if item != None:
                    cb(item, i, j, idx)
                    idx += 1
                i += 1

  
    def report_container_frequencies(self): 
        containers = [None] * self.capacity()   
        for i in range(len(self.table)): 
            containers[i] = self.table[i].size
        return containers

    def report_container_items(self): 
        for item in self.table: 
            print(item)

    def display(self): 
        self.traverse(
            lambda item, i, j, idx: 
                print(str(item).ljust(20), i, j, idx)
        )

    # --- KEY/VALUE/ITEM ACCESSORS --- # 

    def items(self): 
        if self.resolution_mode == CHAINING_RESOLUTION: 
            for container in self.table: 
                current = container.head
                while current is not None: 
                    item = current.value
                    yield item
                    current = current.next
            return None

        elif self.resolution_mode in OPEN_ADDRESSING_MODES: 
            for item in self.table: 
                if item != None:
                    yield item

    def keys(self): 
        for item in self.items(): 
            yield item[0]

    def values(self):
        for item in self.items(): 
            yield item[1]
        
###############################################################
## --- EMBEDDED LINKED LIST IMPLEMENTATION FOR HASH-TABLE --- # 
###############################################################

class SLL_Node: 
    def __init__(self, value): 
        self.value = value 
        self.next  = None 
         
class SLL: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.size = 0 

    # --- LOCATION OPERATIONS --- #
    
    def at(self, index): 
        i = 0 
        index = index % self.size 
        current = self.head 
        while i < index: 
            current = current.next 
            i += 1   
        return current     
    
    def search(self, value): 
        current = self.head 
        while current is not None: 
            if current.value == value: 
                return current
            current = current.next 
        return None 
    
    def search_node(self, node):
        current = self.head 
        while current is not None: 
            if current is node: 
                return current 
            current = current.next 
        return None 

    def index(self, value):
        i = 0 
        current = self.head 
        while current is not None: 
            if current.value == value: 
                return i 
            current = current.next 
            i += 1 
        return -1   
        
    def node_index(self, node):
        i = 0 
        current = self.head 
        while current is not None: 
            if current is node: 
                return i 
            current = current.next 
            i += 1 
        return -1 
 
    # --- INSERTION OPERATIONS --- # 

    def insert(self, pos, value): 
        node = SLL_Node(value) 
        self.insert_node(pos, node)

    def insert_node(self, pos, node): 
        # insert at beginning of list 
        if pos == 0: 
            self.prepend_node(node)
        # insert at end of the list 
        elif pos == self.size: 
            self.append_node(node)
        # insert at the middle of the list 
        elif pos > 0 and pos < self.size: 
            predecessor = self.at(pos - 1) 
            successor = predecessor.next 
            node.next = successor 
            predecessor.next = node 

            # increase size of list 
            self.size += 1
        # out of bounds 
        else:
            error = f"Out of bounds ({pos})" + \
                    f"when inserting {node.value}"
            raise Exception(error)
        
    def prepend(self, value): 
        node = SLL_Node(value)
        self.prepend_node(node) 

    def prepend_node(self, node): 
        # if list is initially empty 
        if self.head == None: 
            self.head = node 
            self.tail = node 
        else: 
            node.next = self.head 
            self.head = node   

        # increase size of list 
        self.size += 1 

    def append(self, value): 
        node = SLL_Node(value) 
        self.append_node(node)

    def append_node(self, node):
        # if list is initially empty 
        if self.head == None: 
            self.head = node 
            self.tail = node 
        else: 
            self.tail.next = node 
            self.tail = node 

        # increase size of list 
        self.size += 1

    def insert_after(self, node, value):
        new_node = SLL_Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node, new_node): 
        # if node is tail, append 
        if node is self.tail: 
            self.append_node(new_node)
        else: 
            successor = self.successor(node) 
            new_node.next = successor 
            node.next = new_node 
        
        # increase size of list 
        self.size += 1 
    
    def insert_before(self, node, value): 
        new_node = SLL_Node(value) 
        self.insert_node_before(node, new_node) 

    def insert_node_before(self, node, new_node):
        # if node is head, prepend 
        if node is self.head: 
            self.prepend_node(new_node)
        else: 
            predecessor = self.predecessor(node)         
            new_node.next = node 
            predecessor.next = new_node 

        # increase size of list 
        self.size += 1

    # --- DELETION OPERATONS --- # 
    def delete(self, pos):
        # delete at beginning of list 
        if pos == 0: 
            self.delete_head()
        # delete at end of the list 
        elif pos == self.size: 
            self.delete_tail()
        # delete at the middle of the list 
        elif pos > 0 and pos < self.size: 
            self.delete_node(self.at(pos))
        else:
            error = f"Out of bounds ({index})" + \
                    f"when deleting index {node.value}"
            raise Exception(error)

    def delete_node(self, node): 
        if node is self.head: 
            self.delete_head() 
        elif node is self.tail: 
            self.delete_tail() 
        else: 
            predecessor = self.predecessor(node) 
            predecessor.next = predecessor.next.next 

            # decrease size of list
            self.size -= 1  

    def delete_head(self): 
        # move head pointer
        if self.head == self.tail: 
            self.head == None 
            self.tail == None 
        else: 
            self.head = self.head.next  

        # decrease size of list 
        self.size -= 1 

    def delete_tail(self): 
        # move tail pointer 
        if self.head == self.tail: 
            self.head = None 
            self.tail = None 
        else:
            predecessor = self.predecessor(self.tail)
            predecessor.next = None 
            self.tail = predecessor 

        # decrease size of list 
        self.size -= 1 

    def delete_after(self, node):
        if node is self.tail: 
            raise Exception("Out of bounds when deleting node.") 
        else: 
            node.next = node.next.next   


    def delete_before(self, node): 
        if node is self.head:  
            raise Exception("Out of bounds when deleting node.") 
        else: 
            prepredecessor = self.prepredecessor(node) 
            prepredecessor.next = node   

    # --- UTILITY FUNCTIONS --- # 
    def predecessor(self, node):
        if node is self.head: 
            return None 
        else: 
            current = self.head
            while current.next is not node: 
                current = current.next 
            return current  
    
    def successor(self, node): 
        return node.next  

    def prepredecessor(self, node): 
        if node is self.head: 
            return None 
        else: 
            current = self.head
            while current.next is not None and \
                  current.next.next is not node: 
                current = current.next 
            return current  

    def postsucessor(self, node): 
        return node.next.next 
         
    # --- TRAVERSAL OPERATIONS --- # 
    def traverse(self, cb): 
        current = self.head 
        i = 0 
        while current is not None: 
            res = cb(current, i)
            if res: return res  
            i += 1
            current = current.next
        return None 

    def traverse_backwards(self, cb):
        current = self.head 
        stack = []  
        while current is not None: 
            stack.append(current)
            current = current.next 
        i = len(stack) - 1
        while len(stack) > 0 : 
            current = stack[-1]
            res = cb(current, i)
            if res: return res 
            stack.pop(len(stack) - 1)
            i -= 1
        return None

    def traverse_range(self, i, j, cb): 
        current = self.head 
        idx = 0
        while current is not None: 
            if idx >=i and idx < j:  
                res = cb(current, i)
                if res: return res 
            idx += 1 
            current = current.next 
        return None 

