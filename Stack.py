"""
Algorithm Name: Program to Implement Stack
Author: Aniket Debnath
Date: 23-08-2024
"""

#Define a class Stack to perform operations on stack
class Stack:
    
    #Initializing an empty list to store the stack values
    def __init__(self):
        self.stack = []

    #Add a value to the stack to the top/last of the stack
    def push(self, item):
        self.stack.append(item)

    #Check if the stack is empty or not
    def is_empty(self):
        return len(self.stack) == 0
    
    #Remove and return the last item of the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty!!!")
            return None
        return self.stack.pop()
    
    #Display all the elements in the stack
    def display(self):
        if self.is_empty() == False:
            print("Stack: ",self.stack)

#Creating an instance of Stack class
stack = Stack()

#To get the number of elements to enqueue
num = int(input("Enter the number of elements in the stack:\n"))
print(f"Enter {num} elements of the stack:")

#Input the elements to push/add
for idx in range(num):
    ele = int(input(f"Element[{idx+1}]: "))
    stack.push(ele)

#Display all elements in stack after adding
stack.display()

#Get the number of elements to remove/pop
n = int(input("How many elements you want to remove:\n"))

#Popping of elements
while(n>0):
    pop = stack.pop()
    if pop is not None:
        print(f"Element popped: {pop}")
        n = n-1
    else:
        break

#Display stack after popping
stack.display()
