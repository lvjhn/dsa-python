from .structs.csll import CSLL 

csll = CSLL() 

csll.prepend(3)
csll.prepend(2)
csll.prepend(1) 

csll.append(8)
csll.append(9)
csll.append(10)

csll.insert(3, 4)
csll.insert(4, 5)
csll.insert(5, 6)
csll.insert(6, 7)


csll.traverse_to(15, lambda n, i: print(n.value))
