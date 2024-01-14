'''
Start
1. Welcome user and ask for login details.
2. Check that login details are valid.
3. Print a menu for the user to choose what they would like to do.
4. Create a function to check balance.
5. Confirm pin to check balance before calling function.
6. Ask if they would like to choose another option or print thank you message
7. Create a function to transfer money.
8. Confirm the amount and bank account.
9. Create function to withdraw money, confirming the amount.
10. Create a function to deposit money.
End
'''

import random as rd

def balance():
    current_balance = rd.randint(100, 999999)
    return current_balance

def transfer(amount, name, acc1, acc2):
    print(f"You have transferred £{amount} to {name}\nsort code:{acc1} account no:{acc2}")


def withdraw(bal, amount):
    with_balance = bal - amount
    return with_balance

def deposit(bal,amount):
    dep_balance = bal + amount
    return dep_balance


print("Welcome to Safe Bank. We are here to keep you and your money safe.")

user_name = input("Please enter your username : ")
pin_num = input("Please enter your 4 digit pin : ")


valid_login = open("login_details.txt", "r")

for details in valid_login:
    new_details = details.strip().split(" ")

    user = new_details[0]
    passw = new_details[1]
    

    if user_name in user:
        print(f"Welcome {user_name}")
        break
    else: 
        print("Username not recognised")
            
    
    if pin_num in passw:
        print("Pin accepted")
        break
    else:
        print("Please enter a valid pin")
        
menu = ('''What would you like to do today?
    1. Check current balance
    2. Transfer money
    3. Withdraw money
    4. Deposit money
    0. Exit menu''')
print(menu)

while True:
    menu_choice = int(input("Enter a number to make your choice :"))

    if menu_choice == 1:
        pin_check = input("Please enter your pin to continue : ")
        if pin_check in passw:
            print(f"Your current balance is £{balance()}")
            print(f"{menu}")
            continue
        
        else: 
            print("Please enter a valid pin")
            break

    if menu_choice == 2:
        trans_amount = int(input("Please enter the amount you would like to transfer £:"))
        recip = input(f"Who would you like to transfer £{trans_amount} to? :")
        sort_code = (input("Enter the recipients sort code : "))
        if len(sort_code) != 6:
            print("Please enter a valid sort code")
            continue
        acc_no = (input("Enter the recipients account number : "))
        if len(acc_no) != 8:
            print("Please enter a valid account number")
            continue
        print(f'''You would like to transfer £{trans_amount} to {recip}
sort code {sort_code} account number {acc_no}''')
        correct = int(input("Is this information correct? 1. yes  0. no : "))
        if correct == 1:
            print(transfer(trans_amount,recip,sort_code,acc_no))
            print(f"{menu}")
            continue
        else:
            print("Please try again")
            continue

    if menu_choice == 3:
        curr_bal = int(balance())
        print(f"Your current balance is {curr_bal}")
        withd_amount = int(input("Please enter the amount you would like to withdraw £ "))
        print(f'''You would like to withdraw £{withd_amount}
After withdrawal your account balance will be £{withdraw(curr_bal,withd_amount)}''')
        if withdraw(curr_bal,withd_amount) < 0:
            print("You do not have sufficient funds to withdraw this amount")
            break
        else:
            correctw = int(input("Is this information correct? 1. yes  0. no : "))
        if correctw == 1:
            print(f"You have withdrawn £{withd_amount} successfully.")
            print(f"{menu}")
            continue
        else:
            print("Please try again")
            continue
        
    
    if menu_choice == 4:
        curr_bal = int(balance())
        print(f"Your current balance is {curr_bal}")
        dep_amount = int(input("Please enter the amount you would like to deposit £ "))
        print(f"You would like to deposit £{dep_amount}")
        correctd = int(input("Is this information correct? 1. yes  0. no : "))
        if correctd == 1:
            print(f'''You have deposited £{dep_amount} successfully.
Your new account balance is £{deposit(curr_bal,dep_amount)}''')
            print(f"{menu}")
            continue
        else:
            print("Please try again")
            break

    if menu_choice == 0:
        print("Thank you for visiting Safe Bank today")
        break
        













