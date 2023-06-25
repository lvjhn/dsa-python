from .structs.dll import DLL 

dll = DLL() 

dll.prepend(30) 
dll.prepend(20)
dll.prepend(10) 

dll.append(60)
dll.append(80)
dll.append(90)

dll.insert(3, 50) 
dll.insert(4, 60)
dll.insert(5, 70)

dll.traverse_backwards(lambda n, i: print(n.value))
