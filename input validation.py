'''
Cinthya Calderon-Hernandez
CSMC 111
Spring 2026
Handling Invalid User Input
'''
#Chapt GPT
#try except block to handle invalid number input
try:
    user_input = input("Enter a number: ")

    number = int(user_input)

    print(f"You entered: {number}")
#Input validation output messages and error handling behavior
except ValueError:
    print("Invalid input. Please enter a number.")