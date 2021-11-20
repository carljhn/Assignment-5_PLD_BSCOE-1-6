import math

def get_Grade():
    grade=input("Enter your grade percentage: ")
    if grade=="Inc":
        print("Grade/Mark: Inc")
        print("Description: Incomplete")
    elif grade=="W":
        print("Grade/Mark: W")
        print("Description: Withdraw")
    elif grade=="D":
        print("Grade/Mark: D")
        print("Description: Dropped")