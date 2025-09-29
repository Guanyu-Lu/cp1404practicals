MIN_SCORE=0
MAX_SCORE=100
EXCELLENT_THRESHOLD=90
PASSABLE_THRESHOLD=50
MENU="(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
def main():
    """Run the program based on user's choice"""
    score = -1 #-1 represent no score yet

    print(MENU)
    choice=input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score ==-1:
                print("You must enter a score.")
            else:
                result=get_result(score)
                print(f"Your Score: {score}-{result}")
        elif choice == "S":
            if score ==-1:
                print("You must enter a score.")
            else:
                print("*" * int(score))
        else:
            print("Invalid choice. Please enter again.")
        print(MENU)
        choice = input(">>>").upper()
    print("Farewell")

def get_valid_score():
    """Get valid score input from user."""
    score = float(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Score must be 0-100 inclusive. Please enter again.")
        score = float(input("Enter score: "))
    return score
def get_result(score):
    """Determine result category based on score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()