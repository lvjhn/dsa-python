'''
    SINGLY LINKED-LIST IMPLEMENTATION (PYTHON) 

    Notes: 
        * isolated
			- does not depend on third-party packages or other files 
			- can be used as is

        * reference: 
            * Singly Linked List (programiz.com) - slightly modified
                https://www.programiz.com/dsa/linked-list
                https://www.programiz.com/dsa/linked-list-operations

        * implements common operations 
			- search(value)
            - at(pos)
            - insert(pos, value)
            - prepend(value)
            - append(value)
            - traverse(cb)

        * printable / narrow width
''' 

class SLL_Node: 
    def __init__(self, value): 
        self.value = value 
        self.next  = None 

class SLL: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.size = 0 

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

    def at(self, pos):
        i = 0 
        current = self.head
        
        while i < pos: 
            i += 1 
            current = current.next 
        
        return current 

    def insert(self, pos, value): 
        if pos == 0: 
            self.prepend(value) 
        elif pos == self.size: 
            self.append(value) 
        else: 
            new_node = SLL_Node(value) 

            if pos > self.size: 
                raise Exception("Out of bounds.") 

            predecessor = self.at(pos - 1)

            new_node.next = predecessor.next
            predecessor.next = new_node 

            self.size += 1

    def prepend(self, value): 
        new_node = SLL_Node(value) 
        new_node.next = self.head

        if self.head is None: 
            self.tail = new_node 
        
        self.head = new_node
        
        self.size += 1

    def append(self, value): 
        new_node = SLL_Node(value) 
        
        if self.head is None: 
            self.head = new_node 
        else: 
            self.tail.next = new_node 
        
        self.tail = new_node     
        self.size += 1 

    def traverse(self, cb): 
        current = self.head
        i = 0 
        while current is not None: 
            res = cb(current, i)
            if res: return 
            i += 1
            current = current.next 
        
