age=int(input("Enter your age: "))

if age>=-1 and age<=12:
    print("You are a Kid.")
elif age>=13 and age<=17:
    print("you are a Teen.")
elif age==18:
    print("Debut")
else: 
    print("You are an Adult.")

print("Thank you for using the program!")