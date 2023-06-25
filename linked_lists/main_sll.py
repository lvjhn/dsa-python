from .structs.sll import SLL 

sll = SLL() 

sll.prepend(30) 
sll.prepend(20)
sll.prepend(10) 

sll.append(70)
sll.append(80)
sll.append(90)

sll.insert(3, 40) 
sll.insert(4, 50)
sll.insert(5, 60)

sll.traverse(lambda n, i: print(n.value))
