#1.
name=input("Enter your name: ")
with open("name.txt","w")as file:
    file.write(name)

#2.
with open("name.txt","r")as file:
    name=file.read()
    print(f"Hi,{name}!")

#3.
with open("numbers.txt", "r") as file:
    number1=int(file.readline())
    number2=int(file.readline())
print(number1+number2)

#4.
total = 0
with open("numbers.txt","r") as file:
    for line in file:
        number=int(line.strip())
        total += number
print(total)