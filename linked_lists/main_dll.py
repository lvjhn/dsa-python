from .structs.dll import DLL 

dll = DLL() 

dll.prepend(3)
dll.prepend(2)
dll.prepend(1) 

dll.append(8)
dll.append(9)
dll.append(10)

dll.insert(3, 4)
dll.insert(4, 5)
dll.insert(5, 6)
dll.insert(6, 7)


dll.traverse(lambda n, i: print(n.value))
print("---")
dll.traverse_backwards(lambda n, i: print(n.value))
