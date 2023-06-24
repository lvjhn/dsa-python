from .structs.cdll import CDLL 

cdll = CDLL() 

cdll.prepend(3)
cdll.prepend(2)
cdll.prepend(1) 

cdll.append(8)
cdll.append(9)
cdll.append(10)

cdll.insert(3, 4)
cdll.insert(4, 5)
cdll.insert(5, 6)
cdll.insert(6, 7)


cdll.traverse_to(15, lambda n, i: print(n.value))
