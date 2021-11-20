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
    else:
        grade=float(grade)
        if 97<=round(grade)<=100:
            print("Grade/Mark: 1.0")
            print("Description: Excellent")
            
        elif 94<=round(grade)<=96:
            print("Grade/Mark: 1.25")
            print("Description: Excellent")

        elif 91<=round(grade)<=93:
            print("Grade/Mark: 1.50")
            print("Description: Very Good")
            
        elif 88<=round(grade)<=90:
            print("Grade/Mark: 1.75")
            print("Description: Very Good")
            
        