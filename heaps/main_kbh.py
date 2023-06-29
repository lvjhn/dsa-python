from .structs.kbh import KBH

def main_a():
    heap = KBH("min") 

    # Custom Comparator Demo 
    def comparator(a, b): 
        if heap.type == "min": 
            if a.value == b.value: 
                return a.key < b.key 
            else: 
                return a.value < b.value  
        elif heap.type == "max": 
            if a.value == b.value: 
                return a.key > b.key 
            else: 
                return a.value < b.value  

    heap.comparator = comparator

    heap.insert("a", 10)
    heap.insert("b", 20)
    heap.insert("c", 30)
    heap.insert("d", 40)
    heap.insert("e", 50)
    heap.insert("f", 60)
    heap.insert("g", 60)
    heap.insert("h", 60)
    heap.insert("i", 70)
    heap.insert("j", 80)

    heap.display()

    # Update and Pop

    heap.update("i", -100)

    print("heap.min()", heap.min())

    print("No. of items before popping:", heap.size)
    heap.pop()
    print("No. of items after popping:", heap.size)

    print("heap.min():", heap.min())

    heap.display()

    # Unload heap 
    while heap.size() > 0: 
        top = heap.top() 
        print(top.value, top.key) 
        heap.pop()
        
def main_b():
    heap = KBH("min") 
    N_ITEMS = 100_000

    for i in range(N_ITEMS): 
        heap.insert(i, i) 
    
    for i in range(N_ITEMS): 
        heap.pop()

main_b()