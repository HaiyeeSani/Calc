#It is important to use function when there are many tasks 
#function to add
#function to subtract
#function to multiply
#function to divition
#variable delaration

number1=int(input("Put first the number"))
number2=int(input("Put the second number"))
operator=input("Select the operator: ")
#validate number1
#function to check number1
def validate_num(n):
    try:
        number1=int(input("Put the number"))
    except:
        print("must be the number")
#validate number2

#intiazing values for variables
try:
    number1=int(input("Put first the number"))
except:
    print("This is not number")
try:
    number2=int(input("Put the second number"))
except:
    print("This is not number")
operator=input("Select the operator: ")
try:
    if operator =="+":
        result=number1+number2
        print("{}+{}=".format(number1+number2),result)
    elif operator =="-":
        result=number1+number2
        print("{}-{}=".format(number1+number2),result)
    elif operator =="*":
        result=number1+number2
        print("{}*{}=".format(number1+number2),result)
    elif operator =="/":
        result=number1+number2
        print("{}/{}=".format(number1+number2),result)
except:
    print("something is wrong")


 
