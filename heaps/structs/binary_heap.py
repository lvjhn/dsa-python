''' 
    HEAP IMPLEMENTATION (PYTHON)

    Notes: 
		* isolated
			- does not depend on third-party packages or other files 
			- can be used as is
        
        * printable / narrow width

        * reference: 
            https://devashish-iitg.medium.com/heap-sort-heapify-up-or-down-5fd35adfff39
        
		* implements common operations
            - value() 
            - comparator() 
            - keyfy(self, items) 
            - swap_key_map(i, j)
            - heapify_up(items, keyfy) 
            - heapify_down(items, keyfy) 
            - insert(key, value)
            - delete() 
            - update(key, new_value)
            - update_a(key, value)
            - update_b(key, value)  
            - keys(self)
            - values(self)
            - top(self)
            - size(self)

''' 

class BinaryHeap_Item: 
    def __init__(self, key, value, data = None):
        self.key = key
        self.value = value 
        self.data = data

class BinaryHeap: 
    def __init__(self, type_ = "min"): 
        self.items = [] 
        self.type = type_
        self.key_no = 0  
        self.key_map = {} 

    def value(self, x): 
        return x.value

    def comparator(self, a, b): 
        if self.type == "min": 
            return self.value(a) < self.value(b)
        elif self.type == "max":
            return self.value(a) > self.value(b)
        return None

    def keyfy(self, items): 
        if type(items) is list: 
            for i in range(len(items)): 
                items[i] = BinaryHeap_Item(self.key_no, items[i])
                self.key_map[items[i].key] = i
                self.key_no += 1 
            return items
        elif type(items) is dict: 
            i = 0
            new_items = []
            for key in items: 
                value = items[key]
                new_items.append(BinaryHeap_Item(key, value))
                self.key_map[key] = i
                self.key_no += 1 
                i += 1
            return new_items

    def swap_key_map(self, i, j): 
        arr = self.items
        self.key_map[arr[i].key] = j
        self.key_map[arr[j].key] = i

    def heapify_up(self, items, keyfy = True): 
        self.items = items
        if keyfy: 
            items = self.keyfy(self.items)
            self.items = items
        n = len(items)

        for i in range(n): 
            j = i 
            while j > 0 and self.comparator(items[j], items[j // 2]): 
                self.swap_key_map(j // 2, j)
                items[j // 2], items[j] = items[j], items[j // 2] 
                j = j // 2 
    
    
    def heapify_down(self, arr, keyfy = True):
        self.items = arr
        if keyfy:
            items = self.keyfy(self.items)
            self.items = items
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1): 
            j = i 

            while 2 * j + 2 < n: 
                l = 2 * j + 1 
                r = 2 * j + 2 
                
                m = None 

                if self.comparator(items[l], items[j]): 
                    self.swap_key_map(l, j)
                    items[l], items[j] = items[j], items[l]
                    j = l 

                elif self.comparator(arr[r], arr[j]): 
                    self.swap_key_map(r, j)
                    items[r], items[j] = items[j], items[r]
                    j = r 
                
                else: 
                    break
    
    def insert(self, key, value, data = None): 
        item = BinaryHeap_Item(key, value, data)
        arr = self.items
        arr.append(item)
        i = len(arr) - 1 
        while i >= 0: 
            if self.comparator(arr[i], arr[i // 2]): 
                self.swap_key_map(i // 2, i)
                arr[i // 2], arr[i] = arr[i], arr[i // 2]
                i = i // 2       
            else: 
                break     

    def delete(self):
        if len(self.items) == 1: 
            self.items = [] 
            return
        
        arr = self.items
        n = len(arr)
        l = n - 1 
        
        arr[0] = arr[l]
        arr.pop(l)
        n = len(arr)

        i = 0 
        while 2 * i + 2 < n: 
            l = 2 * i + 1 
            r = 2 * i + 2

            m = i

            if self.comparator(arr[l], arr[i]): 
                # self.swap_key_map(l, i)
                arr[l], arr[i] = arr[i], arr[l] 
                m = l 
            if self.comparator(arr[r], arr[i]): 
                # self.swap_key_map(r, i) 
                arr[r], arr[i] = arr[i], arr[r]
                m = r
            
            if m == i: 
                break
            else: 
                l = m

    def update(self, key, new_value): 
        arr = self.items 
        if key not in self.key_map: 
            raise Exception(f"{key} is not in list.")
        i = self.key_map[key] 
        curr_val = arr[i].value 
    
        if self.type == "min": 
            if new_value > curr_val: 
                self.update_b(key, new_value)
            else:   
                self.update_a(key, new_value)

        elif self.type == "max": 
            if new_value > curr_val: 
                self.update_a(key, new_value)
            else: 
                self.update_b(key, new_value)

    def update_a(self, key, value): 
        arr = self.items 
        i = self.key_map[key] 
        arr[i].value = value 
        
        while i > 0:
            if self.comparator(arr[i], arr[i // 2]): 
                self.swap_key_map(i // 2, i)
                arr[i // 2], arr[i] = arr[i], arr[i // 2]
            else:
                break   
            i = i // 2    

    def update_b(self, key, value): 
        arr = self.items
        i = self.key_map[key] 
          
        arr[i].value = value
        n = len(arr)

        while 2 * i + 2 < n: 
            l = 2 * i + 1 
            r = 2 * i + 2
            
            if self.comparator(arr[l], arr[i]): 
                self.swap_key_map(l, i)
                arr[l], arr[i] = arr[i], arr[l] 
                i = l 
            elif self.comparator(arr[r], arr[i]): 
                self.swap_key_map(r, i) 
                arr[r], arr[i] = arr[i], arr[r]
                i = r
            else: 
                break
            
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
        