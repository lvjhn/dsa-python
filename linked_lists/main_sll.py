from .structs.sll import SLL 

sll = SLL() 


sll.prepend(3)
sll.prepend(2)
sll.prepend(1) 

sll.append(8)
sll.append(9)
sll.append(10)

sll.insert(3, 4)
sll.insert(4, 5)
sll.insert(5, 6)
sll.insert(6, 7)


sll.traverse(lambda n, i: print(n.value))
