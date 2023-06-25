'''
	STACK IMPLEMENTATION (PYTHON) 
	
	Notes: 
		* isolated
			- does not depend on third-party packages or other files 
			- can be used as is
		
		* printable / narrow width

		* implements common operations 
			- push(value)
			- top() 
			- pop()
			- size() 

''' 

class Stack: 
	def __init__(self): 
		self.items = [] 
	
	def size(self):
		return len(self.items) 
	
	def top(self): 
		return self.items[-1] 
	
	def push(self, value): 
		self.items.append(value)
	
	def pop(self): 
		return self.items.pop(self.size() - 1) 
