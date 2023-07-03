from .structs.stack import Stack 

print(f"# DEMO OF STACK ADT #")

# create stack
stack = Stack() 

# display initial stack size 
print(f"> Stack Size: {stack.size()}")
assert(stack.size() == 0)

# insert items to the stack 
print(f"> Inserting 1, 2, and 3 to the stack...")
stack.push(1)
stack.push(2)
stack.push(3)

# display stack items 
print(f"> Stack Items: {stack.items}") 
assert(stack.items == [1, 2, 3])


# display top of stack 
print(f"> Top of Stack: {stack.top()}") 
assert(stack.top() == 3)

# pop top of stack 
print("> Popping top of stack...") 
pop = stack.pop() 
assert(pop == 3)

# display top of stack 
print(f"> New Top of Stack: {stack.top()}") 
assert(stack.top() == 2)

# pop remaining items in the stack
print(f"> Popping remaining items in the stack...") 
while stack.size(): 
    print(f"> Popping top = {stack.top()}...")
    stack.pop() 

print(f"> Stack Size: {stack.size()}")
assert(stack.size() == 0)
assert(stack.items == [])