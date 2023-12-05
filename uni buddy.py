'''
Start
1. Ask user to input name, age and favourite food
2. Print a personalised greeting based on user input name
3. Print activities based on user age
4. Print places to eat based on favourite food
5. Ask user to enter a question
6. Answer the question using personalised language
End'''

user_name = input("Hello, my name is Uni Buddy. What is your name? : ")

while True: 
    user_age = int(input("How old are you? : "))

    if user_age > 35:
        print(f"Hello {user_name}. It is lovely to meet you.")
        print("There are some great activities onsite for people of your age. Check these out;")
        print('''
    1. Local bookstores are holding bookclubs @ 6:30 across the week
    2. Join in with our yoga classes on a Tuesday and Thuursday @ 7:30
    3. Meet up with other mature students in the cafeteria on Sunday @ 2pm)
    4. Join our wellbeing webinars everyday @ 4 pm''')
        break
    
    elif user_age >= 25:
        print(f"Hello {user_name}. It is lovely to meet you.")
        print("There are some great activities onsite for people of your age. Check these out;")
        print('''
    1. Local tour run by the social comittee @ 4pm on Wednesday
    2. Sign up to our onsite gym and swimming pool anytime this week for a 10% discount
    3. Housing support will be available @10am every day to answer questions about renting in the area.
    4. Come and join our pool, darts or skittles teams in the student union @ 7pm every Thursday''')
        break

    elif user_age >= 18:
        print(f"Hello {user_name}. It is lovely to meet you.")
        print("There are some great activities onsite for people of your age. Check these out;")
        print('''
    1. Cooking classes on a Tuesday @ 5pm for those away from home for the first time
    2. Sports taster events everyday this week @ 2pm on the field
    3. Social events every evening @ the student union after 9pm
    4. Tours of the library @ 11 on Monday and Thursday''')
        break
    
    else:
        print("Please enter an age over 17")
        continue

fav_food = input("What type of food do you like to eat? : ").lower()

if fav_food == "chinese":
    print(f"If your favourite food is {fav_food}, we have a noodle bar at weekends in the cafeteria")

elif fav_food == "indian":
    print(f"If your favourite food is {fav_food}, there are over 50 indian restaurants and take aways within 5 miles of the university! ")

elif fav_food == "mexican":
    print(f"If your favourite food is {fav_food}, our weekly cooking classes often teach simple mexican inpired meals. Why not join!")

else:
    print('''There are a wide range of restaurants, take aways, international shops in the area
as well as our wonderful cafeteria. You are sure to find something delicious to eat!''')

question = input("If you have a question for me, please enter it here : ")
print(f"Thank you for your question {user_name}")
print('''
Here are some our our frequently asked questions.
If you can't find your answer here please contact our friendly student support team.
- Where is the student union? 
      You will find a map of the site in your welcome pack. The student union is the meet up point for all activities.
- How do I access student services?
      All students services can be accessed on the university website under the tab student services.
- When will I get my lecture schedule?
      When you have your student login details, your schedule will be on your student dashboard.
- What are the cafeteria opening times?
      The cafeteria is open from 6:30am - 6:30pm every weekday. Outside of these times there are self service options available.''')

print(f"It has been great chatting with you today {user_name}")