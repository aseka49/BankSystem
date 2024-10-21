import os

pin_file = "pin_code.txt"

def load_pin():
    if os.path.exists(pin_file):
        with open(pin_file, 'r') as file:
            pin = file.read().strip()
            return pin
    return '0000'

def login():

    current_pin = load_pin()
    attempts = 3
    while attempts > 0:
        print("Enter PIN code")
        pin = input().strip()
        if current_pin == pin:
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN code. You have {attempts} attempts")
    return False

def main():
    if not login():
        return

    while True:
        print("Choose operation")
        print("1. Bank statement")
        print("2. Balance replenishment")
        print("3. Cash withdrawal")
        print("4. Change PIN code")
        print("5. Exit")

        choose = int(input())

        if choose == 1:
            bank_statement()
        elif choose == 2:
            balance_replenishment()
        elif choose == 3:
            cash_withdrawal()
        elif choose == 4:
            change_pin()
        elif choose == 5:
            print("Goodbye")
            break


balance = 0

def bank_statement():
    global balance
    print(f'Your balance is {balance} dollars')

def balance_replenishment():
    global balance
    amount = int(input("The amount to top up: "))
    if amount > 0:
        balance = balance + amount
        print(f"Now, your balance is {balance} dollars")
    else:
        print('U cant enter negative number')

def cash_withdrawal():
    global balance
    amount = int(input("The amount to top up: "))
    if amount > 0 and balance > amount:
        balance = balance - amount
        print(f"Now, your balance is {balance} dollars")
    elif amount > 0 and amount > balance:
        print("U cant enter sum higher than your balance")
    else:
        print('U cant enter negative number')

def save_pin(new_pin):
    with open(pin_file, 'w') as file:
        file.write(new_pin)

def change_pin():
    new_pin = input("Your new PIN?").strip()
    if len(new_pin) == 4 and new_pin.isdigit():
        save_pin(new_pin)
        print("Your PIN code saved")
    else:
        print("Error")


main()


