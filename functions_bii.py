#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    output = []
    for i in range(num, -1,-1):
        output.append(i) 
    return output 

print(countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_return (list):
    print([0])
    return([1])

print(print_return([0,1]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstpluslength(list):
    return list[0] + len(list)
print(firstpluslength([3,4,4,5,5]))



# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output



# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(9,8))
print(length_and_value(9,9))