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

#function to show the user's current balance
def balance():
    current_balance = rd.randint(100, 999999)
    return current_balance

#function to check there is enough money in the account to transfer the given amount
def transfer_check(bal,amount):
    new_current_balance = bal - amount
    return new_current_balance

#function to return the new balance after withdrawal
def withdraw(bal, amount):
    with_balance = bal - amount
    return with_balance

#function to return the new balance after deposit
def deposit(bal,amount):
    dep_balance = bal + amount
    return dep_balance

#user login details
user_dict ={'Sarah42':4141,
            'Lillian88':7283,
            'Paul67':9403,
            'Mike77':7262}


print("Welcome to Safe Bank. We are here to keep you and your money safe.")

#usernames and pin numbers stored in a dictionary. Check that user input matches the key value pair
while True:
    user_name = input("Please enter your username : ")
    if user_name in user_dict:
        print(f"Welcome {user_name}")
        break
    else: 
        print("Invalid username. Please try again")
        user_name = input("Please enter your username : ")
        continue

valid_pin = user_dict[user_name]
while True:
    try:
        pin_num = int(input("Please enter your 4 digit pin : "))
    except ValueError:
        print("Please enter 4 digits") 
    if valid_pin == pin_num:
        print("PIN correct")
        break
    else:
        print("Invalid pin. Please try again")
        continue

#menu options given each time the user has completed an action
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
        pin_check = int(input("Please enter your pin to continue : "))
        if valid_pin == pin_check:
            print(f"Your current balance is £{balance()}")
            print(f"{menu}")
            continue
        
        else: 
            print("Please enter a valid pin")
            break

#function to calculate whether there are sufficient funds
    if menu_choice == 2:
        
        try:
            trans_amount = int(input("Please enter the amount you would like to transfer £:"))
        except ValueError:
            print("Error. Please enter digits only.")
            continue
        current_bal = balance()
        print(f"Your current balance is \n £{current_bal}")
        print(f"After this transfer your new balance will be \n £{transfer_check(current_bal,trans_amount)}")
        if transfer_check(current_bal,trans_amount) < 0:
            print("You do not have sufficient funds to make this transfer")
            continue
        recip = input(f"Who would you like to transfer £{trans_amount} to? :")
        sort_code = input("Enter the recipients sort code : ")
    #check if sort code and account number are the correct length
        if len(sort_code) != 6:
            print("Please enter a valid sort code")
            continue
        
        acc_no = input("Enter the recipients account number : ")
        if len(acc_no) != 8:
            print("Please enter a valid account number")
            continue
#gives the user the option to check the details entered before the transfer is complete
        print(f'''You would like to transfer £{trans_amount} to {recip}
sort code {sort_code} account number {acc_no}''')
        correct = int(input("Is this information correct? 1. yes  0. no : "))
        if correct == 1:
            print("Transfer successful")
            print(f"{menu}")
            continue
        else:
            print("Please try again")
            continue

#function to check there are sufficient funds to withdraw
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
        
#function to inform the user of their new balance after a deposit  
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
        













