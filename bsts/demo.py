from .structs.avlt import AVLT, AVLT_Node
from .structs.rbt import RBT, RBT_Node

def main(): 

    # create stack
    bst = RBT() 

    print(bst)

    # display initial Tree size 
    print(f"> Tree Size: {bst.size()}")
    print()
    assert(bst.size() == 0)



    # insert keys to the tree
    print(f"> Inserting keys to the tree...")
    for i in range(100000): 
        # print(f"> Inserting ({i * 10}, None)")
        bst.insert(i * 10, None)
        # bst.display() 
        # print("=====================================")
    print()

    # delete items from the tree
    print(f"Deleting keys 20, 50, 70 from the tree..") 
    to_delete = [20, 50, 70] 
    for item in to_delete:
        # print(f"> Deleting {item}")
        bst.delete(item)
        # bst.display() 
        # print("=====================================")
    print() 

    # iterate over elements 
    for item in bst.iterate(): 
        print(item.key)

    bst.display()

def bench(): 
    for i in range(10000): 
        bst.insert(i) 

main()