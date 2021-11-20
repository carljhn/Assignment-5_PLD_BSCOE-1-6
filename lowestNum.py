num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

def get_lowestNum(num1, num2, num3):
    if num1<num2 and num1<num3:
        return num1
    elif num2<num1 and num2<num3:
        return num2
    else:
        return num3
def display(lowest_):
    print(f"The lowest number is {lowest_}")

lowest=get_lowestNum(num1, num2, num3)
display(lowest)