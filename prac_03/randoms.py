import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
#What did you see on line 1?
# I see it generate random integer between 5 and 20.

#What was the smallest number you could have seen, what was the largest?
# 5 is smallest number and 20 is larget number



#What did you see on line 2?
#It generates a number  starting from 3 and increasing by 2 until (but not including) 10.

#What was the smallest number you could have seen, what was the largest?
#3 is smallest number and 9 is largest number

#Could line 2 have produced a 4?
#No,because step=2. 3+2=5>4



#What did you see on line 3?
#It returns a random floating-point number x, which lies between 2.5 and 5.5.

#What was the smallest number you could have seen, what was the largest?
#2.5 is smallest number and 5.5 is largest number



#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
random_number=random.randint(1,100)
print(f"Generated random number between 1 and 100: {random_number}")