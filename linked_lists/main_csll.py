from .structs.csll import CSLL 

csll = CSLL() 

csll.prepend(30) 
csll.prepend(20)
csll.prepend(10) 

csll.append(70)
csll.append(80)
csll.append(90)

csll.insert(3, 40) 
csll.insert(4, 50)
csll.insert(5, 60)

csll.traverse_range(3, 36, lambda n, i: print(n.value))
