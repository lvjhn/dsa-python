from .structs.avlt import AVLT, AVLT_Node
from .structs.rbt import RBT, RBT_Node
import time

BST = RBT

N_ITEMS = 20

items = [x * 10 for x in range(1, N_ITEMS + 1)]

def main(): 
    for i in range(1, N_ITEMS + 1): 
        for j in range(1, N_ITEMS + 1):
            if i > j: continue
            
            to_delete = items[i:j+1]
            print(f"To Delete: {to_delete}")
            
            # create stack
            bst = BST() 

            print(bst)

            # display initial Tree size 
            print(f"> Tree Size: {bst.size()}")
            print()
            assert(bst.size() == 0)

            # insert keys to the tree
            print(f"> Inserting keys to the tree...")
            for x in items: 
                print(f"> Inserting ({x}, None)")
                bst.insert(x, None)
                bst.display() 
                print("=====================================")
            print()

            # # iterate over elements 
            # for item in bst.iterate(): 
            #     print(item.key)
            # print()

            # # iterate over elements on key range 
            # nodes = bst.interval_nodes(70.5, 20.6)
            # print(nodes[0].key, nodes[1].key)
            # nodes = bst.interval_nodes(20.6, 70.5)
            # print(nodes[0].key, nodes[1].key)
            # print()

            # for item in bst.interval_range(20.6, 70.5): 
            #     print(item.key)
            # print()

            # delete items from the tree
            print(f"Deleting keys from the tree..") 

            for item in to_delete:
                print(f"> Deleting {item}")
                bst.delete(item)
                bst.display() 
                print("=====================================")
            print() 

            # iterate over elements 
            for item in bst.iterate(): 
                print(item.key)
            print()

            bst.display()

            print()
            print("|||||||||||||||||||||||||||||||||||||||")
            print()

def bench(BST): 
    print(BST)
    bst = BST()

    N_ITEMS = 100000

    print("> Benchmarking insertion...")
    a1 = time.time()
    for i in range(N_ITEMS): 
        bst.insert(i, None) 
    b1 = time.time() 

    print("> Benchmarking look-up...")
    a2 = time.time() 
    for i in range(N_ITEMS):
        bst.find(i)
    b2 = time.time() 

    print("> Benchmarking deletion...")
    a3 = time.time()
    for i in range(N_ITEMS): 
        bst.delete(i)
    b3 = time.time() 

    print("Insertion:", str(b1 - a1).format("{:.3f}"))
    print("Look-up:", str(b2 - a2).format("{:.3f}"))
    print("Deletion:", str(b3 - a3).format("{:.3f}"))

# main()
bench(AVLT)
bench(RBT)