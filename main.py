MAX_LINES = 3   #Convention in Python in all capitals to show it won't change, Can reference "MAX_LINES" anywhere in code to get the standard 3 lines

#Defining a Function To Be Called to Execute a Block of Code
def deposit():
    while True: #To get the user to continually enter a value until given a deposit amount
        amount = input("What would you like to deposit? $") #User input
        if amount.isdigit(): #String method to determine if a valid number is input
            amount = int(amount)
            if amount > 0:
                break #If amount input is greater than 0, then we will end or "Break" out of this
            else:
                print("Amount must be greater than 0.") #covering the less than 0 inputs
        else:
            print("Please enter a number.") 

    return amount

#Collect the bet from the user
def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") 
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break 
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.") 

    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print("You have deposited: $", balance)
    print(balance, lines)

main()