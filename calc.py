"""
Program: Simple Calculator 

Simple calcuatro help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""
import sys
number1= number2= result= 0
operator=''

def addition():
        result=number1+number2
        print(f"The sumation for the two values is equal to: ,{result}")
def subtraction():
        result=number1-number2
        print(f"The sumation for the two values is equal to: ,{result}")
def multiply():
        result=number1*number2
        print(f"The sumation for the two values is equal to: ,{result}")
def divide():
        result=number1/number2
        print(f"The sumation for the two values is equal to: ,{result}")
def again():
        calc_again = input('''
        Do you want to calculate again?
        Please type Y for YES or N for NO.
        ''')
        if calc_again.upper() == 'Y':
                main()

<<<<<<< Updated upstream
        elif calc_again.upper() == 'N':
                sys.exit('See you later.')
        else:
                again()
def validate_input():
    try:
        number1=float(input("Insert the first value\n"))
    except:
        print("Your first input is not a number\n")
        validate_input()
def validate_second_input():
    try:
        number2=float(input("Insert the second value\n"))
    except:
        print("Your first second is not a number\n")
        validate_input()
def validate_operator():
    operator = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    if operator =='+':
        addition()
    if operator =='-':
        subtraction()
    if operator =='*':
        multiply() 
    if operator =='/':
        divide()
    else:
        print("Invalid operator\n")
        validate_operator()
def main():
        validate_input()
        validate_second_input()
        validate_operator()
        again()
        
                
main()
=======
addition=number1+number2
print(f"The addition for the two values is equal to: ,{addition}")

subtraction=number1-number2
print(f"The subtraction for the two values is equal to: ,{subtraction}")

multiplication=number1*number2
print(f"The multiplication for the two values is equal to: ,{multiplication}")

division=number1/number2
print(f"The division for the two values is equal to: ,{division}")

umber1=int(input("Insert the first value"))
number2=int(input("Insert the second value"))

select = int(input("Select operations form 1, 2, 3, 4 :"))

addition=number1+number2
subtraction=number1-number2
multiplication=number1*number2
division=number1/number2


if select == 1:
       print(f"The addition for the two values is equal to: ,{addition}")

elif select == 2:
       print(f"The subraction for the two values is equal to: ,{subtraction}")

elif select == 3:
       print(f"The multiplication for the two values is equal to: ,{multiplication}")

elif select == 4:
       print(f"The division for the two values is equal to: ,{division}")
else:
        print("invalid input")
>>>>>>> Stashed changes
