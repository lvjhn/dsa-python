from .structs.bsth import BSTH 

def main_a():
    heap = BSTH() 

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
    heap.update("j", -200)

    print("heap.min()", heap.min())
    print("heap.max()", heap.max())

    print("No. of items before popping:", heap.size())
    heap.pop_min()
    print("No. of items after popping:", heap.size())

    print("heap.min():", heap.min())
    print("heap.max()", heap.max())

    heap.display()

    # Unload heap 
    while heap.size() > 0: 
        top = heap.min() 
        print(top) 
        heap.pop_min()
        
def main_b():
    heap = BSTH() 
    N_ITEMS = 100_000

    for i in range(N_ITEMS): 
        heap.insert(i, i) 
    
    for i in range(N_ITEMS): 
        heap.pop_min()

main_a()