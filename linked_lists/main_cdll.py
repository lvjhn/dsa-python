from .structs.cdll import CDLL 

cdll = CDLL() 

cdll.prepend(30) 
cdll.prepend(20)
cdll.prepend(10) 

cdll.append(70)
cdll.append(80)
cdll.append(90)

cdll.insert(3, 40) 
cdll.insert(4, 50)
cdll.insert(5, 60)

cdll.traverse_range(36, 3, lambda n, i: print(n.value))
