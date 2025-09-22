"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MINIMUM_SCORE=0
MAXIMUM_SCORE=100
EXCELLENT_THRESHOLD=90
PASSABLE_THRESHOLD=50
score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    message="Invalid score"
elif score >= EXCELLENT_THRESHOLD:
    message="Excellent"
elif score >= PASSABLE_THRESHOLD:
    message="Passable"
else:
    message="Bad"
print(message)