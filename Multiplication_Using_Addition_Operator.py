"""
Algorithm Name: Program to find multpication using addition operator
Author: Aniket Debnath
Date: 13-09-2024
"""

#Define a class Multiplier to perform multiplication operation
class Multiplier:

    #Initializing the Multiplier class with two variables x and y to store values
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #Multiplies x and y using repeated addition
    def multiply(self):
        result = 0
        for idx in range(abs(self.y)):
            result += abs(self.x)
        if (self.x < 0 and self.y > 0) or (self.x > 0 and self.y < 0):
            result *= -1
        return result

#Getting numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Creating an instance of Multiplier class
multiplier = Multiplier(num1,num2)

#Calling multiply method
product = multiplier.multiply()

#Printing the final product result
print(f"Product of {num1} and {num2} is {product}")
