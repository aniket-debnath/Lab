"""
Algorithm Name: Program to Implement Queue
Author: Aniket Debnath
Date: 23-08-2024
"""

#Define a class Queue to perform operations on queue
class Queue:
    
    #Initializing an empty list to store the queue values
    def __init__(self):
        self.values = []

    #Add a value to the queue
    def enqueue(self, item):
        self.values.append(item)

    #Check if the queue is empty or not
    def is_empty(self):
        return len(self.values) == 0
    
    #Remove and return the first item of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
            return None
        return self.values.pop(0)
    
    #Display all the elements in the queue
    def display(self):
        if self.is_empty() == False:
            print("Queue: ",self.values)

#Creating an instance of Queue class
queue = Queue()

#To get the number of elements to enqueue
num = int(input("Enter the number of elements in the queue:\n"))
print(f"Enter {num} elements of the queue:")

#Input the elements to enqueue
for idx in range(num):
    ele = int(input(f"Element[{idx+1}]: "))
    queue.enqueue(ele)

#Display all elements in queue after enqueue
queue.display()

#Get the number of elements to dequeue
n = int(input("How many elements you want to remove:\n"))

#Dequeue of elements
while(n>0):
    deque = queue.dequeue()
    if deque is not None:
        print(f"Element dequeued: {deque}")
        n = n-1
    else:
        break

#Display queue after dequeue
queue.display()
