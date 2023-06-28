'''
    CIRCULAR SINGLY LINKED-LIST IMPLEMENTATION (PYTHON)

    Notes: 
		* isolated
			- does not depend on third-party packages or other files 
			- can be used as is
        
        * printable / narrow width

		* implements common operations 
			
            Location Operations
            - at(index)
            - search(value) 
            - search_node(node) 
            - index(value)
            - node_index(node) 
            
            Insertion Operations
            - insert(pos, value) 
            - insert_node(pos, node) 
            - prepend(value) 
            - prepend_node(node) 
            - append(value) 
            - append_node(value) 
            - insert_after(node, value) 
            - insert_node_after(node, new_node) 
            - insert_before(node, value) 
            - insert_node_before(node, new_node) 
            
            Deletion Operations 
            - delete(pos) 
            - delete_node(node)
            - delete_head() 
            - delete_tail() 
            - delete_after(node) 
            - delete_before(node)

            Utility Functions 
            - predecessor(node) 
            - successor(node)

            Traversal Operations 
            - traverse(cb) 
            - traverse_backwards(cb) 
            - traverse_range(i, j, cb)

''' 

class CSLL_Node: 
    def __init__(self, value): 
        self.value = value 
        self.next  = None 
         
class CSLL: 
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
        node = CSLL_Node(value) 
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
        node = CSLL_Node(value)
        self.prepend_node(node) 

    def prepend_node(self, node): 
        # if list is initially empty 
        if self.head == None: 
            self.head = node 
            self.tail = node 
        else: 
            node.next = self.head 
            self.head = node   

            # reattach head to tail 
            self.tail.next = self.head

        # increase size of list 
        self.size += 1 

    def append(self, value): 
        node = CSLL_Node(value) 
        self.append_node(node)

    def append_node(self, node):
        # if list is initially empty 
        if self.head == None: 
            self.head = node 
            self.tail = node 
        else: 
            self.tail.next = node 
            self.tail = node 

            # reattach head to tail 
            self.tail.next = self.head

        # increase size of list 
        self.size += 1

    def insert_after(self, node, value):
        new_node = CSLL_Node(value)
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
        new_node = CSLL_Node(value) 
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

            # reattach head to tail  
            self.tail.next = self.head

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

            # reattach head to tail 
            self.tail.next = self.head

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
    def iterate(self):
        current = self.head 
        while True: 
            yield current 
            current = current.next
            if current is self.head: 
                break

    def traverse(self, cb): 
        current = self.head 
        i = 0 
        while True: 
            res = cb(current, i)
            if res: return res  
            i += 1
            current = current.next
            if current is self.head: 
                break 
        return None 

    def traverse_backwards(self, cb):
        current = self.head 
        stack = []  
        while True: 
            stack.append(current)
            current = current.next
            if current is self.head: 
                break  
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
        while True: 
            if idx >= i and idx < j:  
                res = cb(current, idx)
                if res: return res 
            idx += 1 
            current = current.next 
            if idx >= j: 
                break
        return None 

