import random #randomize slot machine

MAX_LINES = 3   #Convention in Python in all capitals to show it won't change, Can reference "MAX_LINES" anywhere in code to get the standard 3 lines
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, #Most valuable win with least available
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { #symbol multiplier for higher output win in the slot machine
    "A": 5, 
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] #we are checking whatever symbol is in the column of the current row
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Add the winning line number

    return winnings, winning_lines  # Return both winnings and winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #symbols.items, you get the keys and values associated with the dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]    
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")   #end tells the print statement what to end the line on INSTEAD of \n which says to go to the next line
            else:
                print(column[row], end="")

        print()

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
                print("Enter a valid number of lines between 1 to 3.")
        else:
            print("Please enter a number.") 

    return lines

def get_bet (): #Repeated code from Deposit
    while True: 
        amount = input("How much would you like to bet on each line? $") 
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break 
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")   #f strings only available in python 3.6 and above - Function here to embed values in my string
        else:
            print("Please enter a number.") 

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}") #embed values with f

    slots =  get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winnings_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play OR Q to quit.")
        if answer == "q":
            break
        balance += spin(balance)  # Pass the balance variable here

    print(f"You left with ${balance}")

main()