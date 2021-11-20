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
        
        elif 85<=round(grade)<=87:
            print("Grade/Mark: 2.00")
            print("Description: Good")
            
        elif 82<=round(grade)<=84:
            print("Grade/Mark: 2.25")
            print("Description: Good")
        
        elif 79<=round(grade)<=81:
            print("Grade/Mark: 2.50")
            print("Description: Satisfactory")
            
        elif 76<=round(grade)<=78:
            print("Grade/Mark: 2.75")
            print("Description: Satisfactory")
            
        elif round(grade)==75:
            print("Grade/Mark: 3.00")
            print("Description: Passing")
            
        elif 65<=round(grade)<=74:
            print("Grade/Mark: 5.00")
            print("Description: Failure")

        return grade

grade_=get_Grade()
print("Thank you for using this program!")        