import os
global_flag = True
print("PERSONAL TO DO LIST")

# Landing Selector
def landing():
    print("""
    1) Login
    2) Sign Up
    3) Exit""")
    landing_input = input("Enter your input: ")
    return landing_input

# Selector Validation
def landingValidation(landingReturnValue):
    flag = True
    while flag:
        if str(landingReturnValue).lower().strip() == '1':
            flag = False
            return 'login'
        elif str(landingReturnValue).lower().strip() == '2':
            flag = False
            return 'signup'
        elif str(landingReturnValue).lower().strip() == '3':
            flag = False
            pass
        else:
            os.system('cls')
            print("Invalid Input. Please try again!")
            landingReturnValue = landing()

# Login
def login():
    print("Login")
    input()

# Signup
def signUp():
    print("Signup")
    input()

# Global Functional Looping
while global_flag:
    landingReturn = landingValidation(landing())
    if landingReturn == 'login':
        global_flag = False
        os.system('cls')
        login()
    elif landingReturn == 'signup':
        global_flag = False
        os.system('cls')
        signUp()
    else:
        global_flag = False