"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

MIN_SCORE=0
MAX_SCORE=100
EXCELLENT_THRESHOLD=90
PASSABLE_THRESHOLD=50

def main():
    """Get score from user and random value, then print results."""
    user_score= float(input("Enter score: "))
    print_score_result(user_score, "Your Score")
    random_score=random.randint(MIN_SCORE,MAX_SCORE)
    print_score_result(random_score, "Random Score")

def get_result(score):
    """Determine result category based on score."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

def print_score_result(score, prompt):
    """Print formatted score result with prompt."""
    result = get_result(score)
    print(f"{prompt}: {score} - {result}")

main()