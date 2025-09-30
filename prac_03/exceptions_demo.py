"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If we enter a string or float
2. When will a ZeroDivisionError occur?
if denominator is equal to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("The denominator cannot be zero.")
        numerator = int(input("Enter the numerator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#except ZeroDivisionError:
    #print("Cannot divide by zero!")
print("Finished.")