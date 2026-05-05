'''
Cinthya Calderon-Hernandez
CSMC 111
Spring 2026
Debugging
'''
#Used ChatGPT
def multiply(a, b):
    try:
        # Fixed logical error: multiplication instead of subtraction
        return a * b

    except TypeError:
        print("Invalid input: both values must be numbers.")
        return None


result = multiply(5, 2)

if result is not None:
    print(result)