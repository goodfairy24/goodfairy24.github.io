'''
 Start
 1. Create functions for different packages for gym memberships including renewals
 2. Create higher order functions to allow and calculate discounts
 3. Create a dictionary to schedule gym classes
 4. Creat a function to find out what time a class is on
 End
'''
#dictionary to show if members qualify for a discount
gym_user_dict = {'Peter Full':{'months remaining':3},
                 'Diane Stop':{'months remaining':7},
                 'Larry Johnson':{'months remaining':4},
                 'Paula Potts':{'months remaining':11},
                 'David Short':{'months remaining':1},
                 'Ella Pine':{'months remaining':10}
                 }

#dictionaries to show class days and times
keep_fit_dict = {'Monday':['11:00','19:00'],
                 'Tuesday':['10:30','19:30'],
                 'Wednesday':['11:00','19:30'],
                 'Sunday':['10:00', '15:00']
                 }

spin_dict = {'Monday':['06:00','17:00'],
                 'Wednesday':['06:30','17:30'],
                 'Friday':['06:00','17:30'],
                 'Saturday':['09:00', '13:00']
                 }

aqua_dict = {'Tuesday':['12:00','20:00'],
                 'Thursday':['11:30','20:30'],
                 'Saturday':['12:00','18:30'],
                 'Sunday':['12:00', '18:00']
                 }


#function to find the cost of a package based on duration
def membership(package):
    base_cost = 50
    if package == 'monthly':
        print(f'Your membership will be £{base_cost} per month')
    elif package == 'quartely':
        quart = (base_cost * 12)/4
        print(f'Your membership will be £{quart} per month')
    elif package == 'annual':
        year = base_cost * 12
        print(f'Your membership will be £{year} per month')
    
#function to find out how many months are remaining on current membership
#this will inform staff if the member qualifies for a discount
def months_remain(name):
    name_memb = gym_user_dict[name]['months remaining']
    print(f'You have {name_memb} months remaining')

#functions to apply either 
#a percentage discount or a fixed discount based on user input
def apply_discount(original_price, discount_function):
    discounted_price = discount_function(original_price)
    print(f"The price with the discount applied is £{discounted_price}")

def percent(original_price):
    return original_price * 0.85
    
def fixed(original_price):
    return original_price - 30

#function to find out the class times on days input by the user
def class_times(name,day):
    if name == 'keep fit':
        print(keep_fit_dict[day])
    if name == 'spin':
        print(spin_dict[day])
    if name == 'aqua':
        print(aqua_dict[day])

#menu for staff member to use 
while True:
    menu = '''What would you like to do?
        1. Find out months remaining on current membership
        2. Find out the price of a package
        3. Add a discount to the price of a package
        4. Find out times and days of classes
        5. Exit the menu'''
    print(menu)
    try:
        menu_choice = int(input("Please enter a number between 1 and 5 : "))
    except ValueError:
        print("Please enter a number between 1 and 5")

    #menu 1 and 2 have a printed statement so staff know when to apply a discount 
    if menu_choice == 1:
        print('''If the member would like to renew with 2 or more months remaining
              please apply the percentage discount''')
        member = input("Please enter the member's name :")
        months_remain(member)

    if menu_choice == 2:
        print('''If the member would like to renew with 2 or more months remaining
              please apply the percentage discount.
              If the member is new, please apply the fixed discount''')
        memb_pack = input('Which package would you like?\nmonthly\nquartely\nannual? :')
        membership(memb_pack)

    if menu_choice == 3:
        price = float(input("Enter the price of membership £"))
        discount = input('''Which discount does the member qualify for?
                         p = percentage discount  f = fixed discount : ''')
        if discount == 'p':
            percentage_disc = apply_discount(price,percent)
        elif discount == 'f':
            fixed_disc = apply_discount(price,fixed)

    if menu_choice == 4:
        class_name = input("Please enter the name of the class: ")
        class_day = input("Please enter the day of the class : ")
        class_times(class_name,class_day)

    if menu_choice == 5:
        print('You have exited the menu')
        break









