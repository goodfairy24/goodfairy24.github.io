import math
'''
start
1. Ask use to input either investment or bond using .lower to formalise entries
2. print user input
3.  If user input is equal to investment, ask the user to input the following;
    amount of money investing
    interest rate (%)
    the number of years they plan on investing
    simple or compound interest - user input.lower
    4. Store simple or compound in a variable called interest
    5. Store r as interest rate / 100
     store P as the amount of money investing
    store t as the number of years invested
6. If simple was input
    A = P *(1 + r*t)
7. If compound was input
    A = P * math.pow((1+r),t)
8. Print A
9. If the user inputs bond ask the user to input;
    the present value of the house
    the interest rate (%)
    the number of months they plan to take to repay the bond
10. Calculate the monthly interest rate (interest_rate/100) / 12
11. store;
 P as the present value of the house
 i as the monthly interest rate
 n as the number of months the bond will be repaid
 12. repayment = (i * P)/(1 - (1 + i)**(-n)) 
 13. print repayment
 14. If investment or bond are not entered correctly print an error message
 end
    '''

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

inv_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
new_inv_or_bond = inv_or_bond.lower()
#.lower function is used to change the input to all lowercase to ensure it meets the if criteria.

if new_inv_or_bond == "investment":
    money_invested = input("Enter the amount of money you would like to invest £: ")
    interest_rate = input("Enter the interest rate % : ")
    no_of_years = input("Enter the number of years you would like to invest for: ")
    interest = input("Enter 'simple' or 'compound' for the type of interest you would like: ")
    new_interest = (interest).lower()
    

    #cast input data into float or int to allow equation to calculate output
    interest_rate = float(interest_rate)
    r = interest_rate / 100
    P = float(money_invested)
    t = int(no_of_years)
    

    if new_interest == "simple":
        A = P *(1 + r*t)
        A = round(A,2)
        print(f"Using {new_interest} interest your investment will be worth £ {A}")
        #print an f string to so that the output is clear to the user
    
    if new_interest == "compound":
        A = P *math.pow((1 + r),t)
        A = round(A,2)
        print(f"Using {new_interest} interest your investment will be worth £ {A}")


elif new_inv_or_bond == "bond":
    house_value = input("Enter the current value of your house: ")
    int_rate = input("Enter the interest rate %: ")
    no_months = input("Enter the number of months repayment will be over: ")
    
    int_rate = float(int_rate)
    monthly_int_rate = (int_rate / 100)/12
    
    P = float(house_value)
    i = monthly_int_rate
    n = int(no_months)
    
    repayment = (i * P)/(1 -(1 + i)**(-n))
    repayment = (round(repayment,2))
    print(f"Your monthly repayment would be £{repayment}")

else:
    print("Error. Please enter 'investment' or 'bond'")





     







