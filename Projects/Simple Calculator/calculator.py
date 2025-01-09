import os
exit_flag = False
operations = ["add", "sub", "mul", "div", "+", "-", "*" , "/", "addition", "substraction", "division", "multiplication", "options", "option"]

def getNumbers(operation):
    list1 = []
    count = 1
    getnumber_flag = False
    if operation == "division":
        value1 = int(input(f"Enter your 1st value = "))
        value2 = int(input(f"Enter your 2nd value = "))
        return [value1, value2]
    else:
        while getnumber_flag == False:
            getnumber_input = str(input(f"Enter your {count} value = ")).lower().strip()
            if getnumber_input == "done":
                getnumber_flag = True
                return list1
            else:
                u_input_flag = False
                try:
                    getnumber_input = int(getnumber_input)
                except ValueError:
                    u_input_flag = True
                if u_input_flag:
                    print("Invalid Value")
                else:
                    list1.append(int(getnumber_input))
                    count += 1
            
def addition():
    sum = 0
    print("Addition")
    a = getNumbers("addition")
    for i in a:
        sum += i
    print(f"Sum = {sum}")

def substraction():
    print("Substraction")
    a = getNumbers("substraction")
    diff = a[0]
    for i in range(1,len(a)):
        diff -= a[i]
    print(f"Difference = {diff}")

def division():
    print("Division")
    a = getNumbers("division")
    print(f"Quotient = {a[0] / a[1]}")

def multiplication():
    product = 1
    print("Multiplication")
    a = getNumbers("multiplication")
    for i in a:
        diff *= i
    print(f"Product = {product}")

def redirect(operation):
    if operation == "add" or operation == "addition" or operation == "+":
        os.system('cls')
        addition()
    elif operation == "mul" or operation == "multiplication" or operation == "*":
        os.system('cls')
        multiplication()
    elif operation == "div" or operation == "division" or operation == "/":
        os.system('cls')
        division()
    elif operation == "sub" or operation == "substraction" or operation == "-":
        os.system('cls')
        substraction()
    elif operation == "option" or operation == "options":
        os.system('cls')
        options()
         
def operationValidation(operation):
    if operation in operations:
        redirect(operation)
    else:
        print("Operation not found!")
        
def startingFunction():
    print('          Simple Calculator')
    print('Type "options/option" to see instructions\n')
    operation = str(input("What operation do wish to perform = ")).lower().strip()
    return operation

def options():
    os.system('cls')
    instructions = """We have 4 operations that you can perform
Addition (+) - Can pass n number of values
Substraction (-) - Can pass n number of values
Division (/) - Can pass only two values
Multiplication (*) - Can pass n number of values 

Type the operation according to your need.
"""
    print()
    print(instructions)

while exit_flag == False:
    a = operationValidation(startingFunction())
    loop_in = str(input('Press "Enter" to go back or type "exit" to close = ')).lower().strip()
    if loop_in == "exit":
        exit_flag = True
    else:
        os.system('cls')