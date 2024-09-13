"""
Algorithm Name: Program to find Euclidean Distance
Author: Aniket Debnath
Date: 13-09-2024
"""
#Importing math library
import math

#Defining a class Point3D to find Euclidean distance for 3D points
class Point3D:

    #Initializing the Point3D class with parameters x, y and z coordinates of 3D space
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    #Returns a string representation of the points
    def __repr__(self):
        return f"Point({self.x},{self.y},{self.z})"
    
    #Calculation of the Euclidean Distance between the points
    def euclidean_distance(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)

#Taking input for the first point's coordinates
coords1 = input("Enter the x, y, z coordinates for the 1st point, separated by spaces: ").split()
x1, y1, z1 = map(int, coords1)

# Taking input for the second point's coordinates
coords2 = input("Enter the x, y, z coordinates for the 2nd point, separated by spaces: ").split()
x2, y2, z2 = map(int, coords2)

#Creating Point3D instances
point1 = Point3D(x1,y1,z1)
point2 = Point3D(x2,y2,z2)

#Calculating the distance
distance = point1.euclidean_distance(point2)

#Printing the final result
print(f"The Euclidean distance between {point1} and {point2} is {distance:.2f}")