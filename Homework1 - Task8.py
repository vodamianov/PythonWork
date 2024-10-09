#Task 8 - Write a program that prompts the user to enter their age and then determines and prints out whether they are eligible to vote (i.e., if they are 18 or older).
age = int(input("Enter age : "))

if age >= 18:
    print("Eligible for Voting!")
else:
    print("Not Eligible for Voting!")