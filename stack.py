# Samina Ahmed | 220023354 | 04/2023
# IN0007 Lab 2 Assessment | Q4

class Stack:
    # __init__ is a method that initialises the object's attributes when it is created.
    def __init__(self):
        self.stack = []
    
    # Defining the push method
    def push(self, item):
        self.stack.append(item)
    
    # Defining the pop method
    def pop(self):
        return self.stack.pop()
    
    # Defining the peek method
    def peek(self):
        return self.stack[-1] if self.stack else None

print("\n")  
# Creating an instance of the Stack class
s = Stack()

# # 1. Print the empty stack.
print(s.stack)

# 2. Push the number 1 into the stack and print.
s.push(1)
print(s.stack)

# 3. Push number 3, 5, and 7 into the stack respectively and print.
s.push(3)
s.push(5)
s.push(7)
print(s.stack)

# 4. Pop the number 7 from the stack and print
popped_item = s.pop()
print("pop:", popped_item)
print(s.stack)

# # 5. Peek the top number from the stack and print. 
peeked_item = s.peek()
print("peek:", peeked_item)
print(s.stack)





