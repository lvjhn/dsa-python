from .structs.stack import Stack 

print("--- STACK DEMONSTRATION ---")

stack = Stack()

print("Pushing item 1.")
stack.push(1)

print("Pushing item 2.") 
stack.push(2) 

print("Pushing item 3.") 
stack.push(3)

print("Stack Items: " + str(stack.items())) 

print("Top of Stack: " + str(stack.top()))

print("Popping Top of Stack") 
stack.pop() 

print("New Stack Items: " + str(stack.items()))

	  