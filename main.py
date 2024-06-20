#Defining a Function To Be Called to Execute a Block of Code
def deposit():
    while True: #To get the user to continually enter a value until given a deposit amount
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #String method to determine if a valid number is input