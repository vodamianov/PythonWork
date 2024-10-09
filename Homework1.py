
#Exercise one - Write a Python script that prints "Hello, World!" to the console.
print ("Hello, World!")

#Exercise two - Create variables to store your name, age, and favorite color. Then, print out a message using these variables (e.g., "My name is [name], I am [age] years old, and my
#favorite color is [color].").

name = 'Vassil'
age = 36
favorite_color = 'purple'

print ("My name is " + name)
print ("I am " , age, " years old, and my favorite color is " + favorite_color)

#Exercise three - Write a program that calculates the area of a rectangle. Prompt the user to enter the length and width, calculate the area, and then print it.

length = input("Enter length: ")
width = input("Enter width: ")

rectangle = (int(length)*int(width))
print ("The are of the rectangle is ", int(rectangle))

#Exercise four - Write a program that converts temperatures from Fahrenheit to Celsius. Prompt the user to enter a temperature in Fahrenheit and then print out the equivalent
#temperature in Celsius.

tempF = input("Enter temperature in F: ")
Celsius = ((float(tempF) - 32) / 1.8)

print ("Converted temperature in Celsius is: ",  float(Celsius))