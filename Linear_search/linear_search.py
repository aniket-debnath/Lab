"""
Algorithm Name: Linear Search
Author: Aniket Debnath
Date: 09-08-2024
"""
def linear_search(list: int,element):
    """
    Program of linear search to find the element in the list.
    List: int: List with the integer elements to search
    Element: Value to search in the list
    """

    #Going through each index in the list
    for idx in range(len(list)):
       
       #Using if condition to check whether the element found is in recent index
       if(element==list[idx]):
           
           #Returns if the element is found in the list
           return f"{element} was found at index {idx}"
    
    #Return when the element is not found
    return f"{element} is not found in the given list"

#Defining a list
list = [9,18,27,36,45,54,63,72,81,90,99]

#User input for the element to search
element = int(input("Enter element to be searched: "))

#Calling the function
final_result=linear_search(list,element)

#Printing the final result
print(final_result)