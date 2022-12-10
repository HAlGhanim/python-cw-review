# Variables

# Create a variable called length and assign a value to it
length = 10
# Create a variable called width and assign a value to it
width = 5
# Create a variable called area and assign to it the multiplication of length and width
area = length * width
# Print area in the following: "The result is " followed by the area variable BONUS: Print the area in the following syntax: "If the length of a rectangle is 5, and width is 3 then the area is: 15". Keep in mind that you should replace the numbers with their respective variables.
print(f"If the length of a rectangle is {length}, and width is {width} then the area is: {area} ")

# Lists

# Create a list named 'favorite_animals' that has four items: dog, cat, monkey, rabbit
favorite_animals = ['dog', 'cat', 'monkey', 'rabbit']
# After creating the list, replace the item that currently holds the value "rabbit" with another animal. It can be any animal you like.
favorite_animals[3] = 'chimpanzee'
# Then using the 'remove' method, remove 'cat' from the list.
favorite_animals.remove('cat')
# Using 'append', add an animal that you like.
favorite_animals.append('lion')
# Print the list to test your code
print(favorite_animals)

# Functions

# Create a function called cube
# It takes an argument called number
# It returns the cube of that number (the number to the power of 3)
# Call function to test it out

def cube(number):
    cubednumber = number ** 3
    return print(f"The number {number} cubed is: {cubednumber}")
cube(3)

# Create a function called by_three
# It takes an argument called number
# If number is divisible by 3, by_three should call `cube(number) and return its result
# Otherwise, by_three should return False.

def by_three(number):
    if number%3 == 0:
       result = cube(number)
       return result
    else:
        return False
number = eval(input("Enter a number: ")) 
by_three(number)

# Functions Extra

# Define a function called padel_court_cost. This function has two arguments, hours and court_type
# If the court_type is indoors, the padel court costs 30 KWD per hour.
# If the court_type is outdoors, the padel court costs 20 KWD per hour.
# The function calculates the padel court cost and returns it. BONUS: If the number of hours is three or more, the cost will be reduced by 20%.
def padel_court_cost(hours, court_type):
    if court_type == "indoor":
        pcc = 30
    elif court_type == "outdoor":
        pcc = 20
    if hours >= 3:
        pcc = pcc * 0.8    
    print(f"Hours: {hours}")
    print(f"Padel court cost: {pcc}")

h = int(input("Enter the number of hours reserved: "))
ct = input("Enter the court type: ")
padel_court_cost(h,ct)

# Functions & Loops

# Create a function printer(elements)
# Accepts a list of temperature degrees
# Prints every element of the list followed by "C" for celsius
def printer(elements):
    tempdegrees = [0, 17, 52, 41, 105]
    for temp in tempdegrees:
        print(f"{temp}C")
printer("elements")

# Create a function to_celsius(temperatures)
# Accepts a list of temperatures in degrees Fahrenheit
# Returns a list of temperatures in degrees Celsius The conversion is: C = (F - 32) * (5/9)

def to_celsius(tempratures):
    tdf = [32, 68, 142, 45, 98]
    tdc = []
    for t in tdf:
        cel = (t-32)*(5/9)
        tdc.append(cel)
    for t in tdc:
        return print(f"Fahrenheit: {tdf}\nConverted \nCelsius: {tdc}")
to_celsius("temp")

# Functions Advanced

# Write a function that will convert seconds into minutes and returns the minutes

def sec_to_min():
    secInput = int(input("Enter the number of seconds: "))
    min = secInput / 60
    secInput %= 60
    return print("%02d:%02d" % (min, secInput))
sec_to_min()

# Write a function is_odd that receives number as an argument, and returns True if it's odd, False otherwise HINT: To check if a number is odd, if a number % 2 is 0 then it's even

def is_odd(numCheck = int(input("Please enter a number: "))):
    if numCheck%2 == 0:
        return print(False)
    else:
        return print(True)
is_odd()

# Write a function that returns the sum of the first and the last elements of a list. If you can, use lambda

# Without lambda

def fl_sum():
    sumList = [12,23,34,45,56,67,78,89,90,100]     
    return print(sumList[0] + sumList[len(sumList)-1])
fl_sum()

# With lambda

def fl_sumL():
    sumList = [12,23,34,45,56,67,78,89,90,100]
    return print((lambda x,y : x+y)(sumList[0], sumList[len(sumList)-1]))
fl_sumL()

# Write a function is_array_length_even that receives an array of numbers as an argument, and returns True if the array has an even number of elements, otherwise it returns False

def is_array_length_even(num):   
    if len(numbers)%2 == 0:
        return print(True)
    else:
        return print(False)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
is_array_length_even(numbers)

# 6 students had taken CODED’s assessment. The results of the assessments were stored in a list. Write a function that returns the greatest score without using any built-in functions

# I found two ways to find the max hunmber without using any built in function

def greatest_score1():
    assessment_grade = [100, 98, 93, 95, 87, 99]
    maxNum = assessment_grade[0]

    for num in assessment_grade:
        if num > maxNum:
            maxNum = num
    return print(maxNum)
greatest_score1()

def greatest_score2():
    assessment_grade = [78, 98, 93, 95, 87, 100]
    maxNum = None

    for num in assessment_grade:
        if maxNum is None or maxNum < num:
            maxNum = num
    return print(maxNum)
greatest_score2()

# In a sorted list that includes the numbers 1-10, one number is missing. How do you find it using a function?

def missing_number():
    num_list = [3,9,2,8,1,7,6,10,4]
    missingNum = []
    sort = sorted(num_list)
    for miss in range(1, sort[-1]):
        if miss not in sort:
            missingNum.append(miss)
    return print(f"The missing number is: {missingNum}")
missing_number()