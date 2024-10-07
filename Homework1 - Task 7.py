#Task 7 - Create a program that checks whether a given number is even or odd. Prompt the user to enter a number and then print out whether it's even or odd.

num = int (input("Enter any number to test if it is even or odd: "))

if (num % 2) == 0:
    print("The number is even.")
else:
    print("The number is odd.")
