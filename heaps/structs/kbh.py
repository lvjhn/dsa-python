''' 
    KEYED BINARY-HEAP IMPLEMENTATION (PYTHON)
    (Modified Binary Heap with Custom Keys)

   * implements common operations
            - comparator(a, b) 
            - bubble_up(arr, i)
            - bubble_down(arr, i)
            - keyfy(items) 
            - swap_key_map(i, j)
            - heapify_up(items, keyfy) 
            - heapify_down(items, keyfy) 
            - insert(key, value, data)
            - insert_node(node)
            - delete() 
            - update(key, new_value)
            - update_a(key, value)
            - update_b(key, value)  
            - keys()
            - values()
            - top()
            - size()
            - get_data(key)
            - set_data(key, data) 
            - get_value(key) 
            - set_value(key, value)
            - get_item(key) 
            - set_item(key, data) 
            - display()
            - min() 
            - max() 

''' 
class KBH_Item: 
    def __init__(self, key, value, data = None):
        self.key = key 
        self.value = value 
        self.data = data

class KBH: 
    def __init__(self, type_ = "min"): 
        self.items = [] 
        self.type = type_
        self.key_no = 0  
        self.key_map = {}

    def comparator(self, a, b): 
        if self.type == "min": 
            return a.value < b.value
        elif self.type == "max":
            return a.value > b.value
        return None

    def bubble_down(self, arr, i):
        n = len(arr)

        while 2 * i + 1 < n: 
            l = 2 * i + 1 
            r = 2 * i + 2
            m = i

            if l < n and self.comparator(arr[l], arr[m]): 
                m = l 
            if r < n and self.comparator(arr[r], arr[m]):                 
                m = r
            
            if m == i: 
                break
            else: 
                self.swap_key_map(m, i)
                arr[m], arr[i] = arr[i], arr[m]
                i = m

        return arr  

    def bubble_up(self, arr, i):  
        while i > 0:
            if self.comparator(arr[i], arr[i // 2]): 
                self.swap_key_map(i // 2, i)
                arr[i // 2], arr[i] = arr[i], arr[i // 2]
                i = i // 2  
            else:
                break   
        return arr

    def keyfy(self, items): 
        if type(items) is list: 
            for i in range(len(items)): 
                items[i] = KBH_Item(self.key_no, items[i])
                self.key_map[items[i].key] = i
                self.key_no += 1 
            return items
        elif type(items) is dict: 
            i = 0
            new_items = []
            for key in items: 
                value = items[key]
                new_items.append(KBH_Item(key, value))
                self.key_map[key] = i
                self.key_no += 1 
                i += 1
            return new_items

    def swap_key_map(self, i, j): 
        arr = self.items
        self.key_map[arr[i].key] = j
        self.key_map[arr[j].key] = i

    def heapify_up(self, arr, keyfy = True): 
        self.items = arr
        if keyfy: 
            arr = self.keyfy(self.items)
            self.items = arr
        n = len(arr)

        for i in range(n): 
            j = i 
            self.bubble_up(arr, j)
    
    def heapify_down(self, arr, keyfy = True):
        self.items = arr
        if keyfy:
            arr = self.keyfy(self.items)
            self.items = arr
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1): 
            j = i 
            self.bubble_down(arr, j)
    
    def insert(self, key, value, data = None): 
        item = KBH_Item(key, value, data)
        
        # add element to heap
        arr = self.items
        arr.append(item)
        i = len(arr) - 1 
        self.key_map[key] = i  

        # bubble up from last element 
        self.bubble_up(arr, i)

    def pop(self):

        # remove element from heap if the heap only has one element
        if len(self.items) == 1: 
            self.items = [] 
            return

        # find last element
        arr = self.items
        n = len(arr)
        l = n - 1 
        
        # move last element from heap
        item = arr[0]
        arr[0] = arr[l]

        # delete previous min and end of array
        del self.key_map[arr[0].key]

        # update key map of end of array
        self.key_map[arr[l].key] = 0
        arr.pop(l)

        n = len(arr)
        
        # bubble down from root
        self.bubble_down(arr, 0)

        return item

    def delete(self, key):
        rem_val = float('-inf') if self.type == "min" else float("inf")
        self.update(key, rem_val) 
        self.pop()

    def update(self, key, new_value): 
        arr = self.items 
        if key not in self.key_map: 
            raise Exception(f"{key} is not in list.")
        i = self.key_map[key] 

        aux = KBH_Item(key, new_value, None)
        item = arr[i] 
    
        if self.type == "min": 
            if self.comparator(aux, item):
                self.update_a(key, new_value)
            else:   
                self.update_b(key, new_value)

        elif self.type == "max": 
            if self.comparator(aux, item): 
                self.update_b(key, new_value)
            else: 
                self.update_a(key, new_value)

    def update_a(self, key, value): 
        arr = self.items 
        i = self.key_map[key] 
        arr[i].value = value
        self.bubble_up(arr, i) 

    def update_b(self, key, value): 
        arr = self.items
        i = self.key_map[key] 
        arr[i].value = value
        n = len(arr)
        self.bubble_down(arr, i)

    def items(self): 
        for item in self.items: 
            yield item
            
    def keys(self): 
        for item in self.items: 
            yield item.key
    
    def values(self): 
        for item in self.items: 
            yield item.value

    def top(self): 
        return self.items[0]

    def size(self): 
        return len(self.items)

    def get_data(self, key): 
        return self.key_map[key].data

    def set_data(self, key, data): 
        self.key_map[key].data = data

    def get_value(self, key): 
        return self.get_item(key).value 

    def set_value(self, key, value): 
        self.key_map[key].value = value

    def get_item(self, key): 
        return self.key_map[key] 

    def set_item(self, key, item): 
        self.key_map[key] = item

    def display(self): 
        text = [] 
        for item in self.items: 
            text.append(f"({item.key}, {item.value}, {item.data})")
        print(", ".join(text))

    def min(self): 
        if self.type != "min":
            raise Exception("Not a minimum heap.") 
        return self.top().value 

    def max(self): 
        if self.type != "max": 
            raise Exception("Not a maximum heap.") 
        return self.top().value 
