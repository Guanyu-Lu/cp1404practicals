#Part1
NUMBER_COUNT=5
numbers=[]
for number in range(NUMBER_COUNT):
    is_integer=False
    while not is_integer:
        try:
            number=int(input("Number:"))
            numbers.append(number)
            is_integer=True
        except ValueError:
            print("Please enter an integer.")
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/NUMBER_COUNT}")

#Part2
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username=input("Username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")