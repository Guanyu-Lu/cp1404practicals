#1.
name=input("Enter your name: ")
with open("name.txt","w")as file:
    file.write(name)

#2.
with open("name.txt","r")as file:
    name=file.read().strip()
print(f"Hi,{name}!")

#3.
with open("numbers.txt", "r") as file:
    first_number=int(file.readline())
    second_number=int(file.readline())
print(first_number + second_number)

#4.

with open("numbers.txt","r") as file:
    total=0
    for line in file:
        number=int(line.strip())
        total += number
print(total)