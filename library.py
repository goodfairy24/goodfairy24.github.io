'''
Start
1. Welcome user to the library with a menu to create an account, borrow a book, return a book or check fines
2. Write dictionaries for books and users
3. Write functions for each menu option
End
'''
#a dictionary of user accounts showing number of books borrowed
#and the total amount of fines
user_account_dict = {
    'Sarah':{'borrowed books':[],'fines':0},
     'Tony':{'borrowed books':[],'fines':0},
    'Ellie':{'borrowed books':[],'fines':0},
}

#a dictionay of books available from the library
#who the book is currently being borrowed by and how many copies available
books_dict = {
    'Harry Potter':{'borrowed by':[],'copies available':5},
    'Horrid Henry':{'borrowed by':[],'copies available':6},
    'The BFG':{'borrowed by':[],'copies available':2},
    'How to Train your Dragon':{'borrowed by':[],'copies available':7},
    'Beauty and the Beast':{'borrowed by':[],'copies available':3},
}

#a function to add a new user to the library
def new_user(name):
    user_account_dict[name] = {'borrowed books':[],'fines':0}
    print(f'Welcome {user_name}. You can now borrow a book.')

'''a function to borrow a book
the function will search through the books dictionary to see if there is a copy available
it will also update the user dictionary and the book dictionary to say who has the book
it will not let the user borrow the book if they already have the maximum number of 
books on loan
it will not accept invalid book titles or usernames'''
def borrow_book(book_title, user):
    if books_dict[book_title]['copies available'] > 0 and len(user_account_dict[user]['borrowed books']) < 5:
        books_dict[book_title]['copies available']-= 1
        books_dict[book_title]['borrowed by'].append(user)
        user_account_dict[user]['borrowed books'].append(book_title)
        print(f'{user} has borrowed {book_title}. You can borrow this book for 3 weeks')
    elif books_dict[book_title]['copies available'] == 0:
        print(f'All copies of {book_title} are out. Please choose a different book')
    elif len(user_account_dict[user]['borrowed books']) == 5:
        print('''You are currently borrowing the maximum of 5 books.
              Please return a book or pay outstanding fines''' )
    else:
        print('Please enter a valid book title or username')
    
'''a function to return a book
it will update the book dictionary to remove the lender and add a copy
it will update the user dictionary by removing the book and adding 1 to the
number of books they are able to borrow
a fine is added if the book is not returned on time and a menu link 
prints to remind the user that they can check their outstanding fines'''
def return_book(book_title, user, fine):
    books_dict[book_title]['copies available']+= 1
    books_dict[book_title]['borrowed by'].remove(user)
    user_account_dict[user]['borrowed books'].remove(book_title)
    if fine == 1:
        user_account_dict[user]['fines'] += 3.00
        print(f'''Thank you for returning {book_title}.
         Please enter option 4 to check your outstanding fines ''')
    elif fine == 0:
        print(f'{book_title}returned on time')
    else:
        print('Please enter a valid book title or username')

#a function to check the amount of outstanding fines
def check_fines(user):
    print(f'Your fine amount is £{user_account_dict[user]}')
    
#user menu on in a while loop so they can choose multiple functions or exit
while True: 
    menu = '''Welcome to the library. What would you like to do today?
         1. Set up a new account
         2. Borrow a book
         3. Return a book 
         4. Check your borrowed books and any outstanding fines
         5. Exit the library'''
    print(menu)
    try:
        menu_choice = int(input('Please enter a number 1-5 to choose an option:'))

    except ValueError:
        print('Please enter a number between 1 and 5')
    

    if menu_choice == 1:
        user_name = input('Please enter a username :')
        new_user(user_name)
        

    if menu_choice == 2:
        new_book = input('Please enter the title of the book you wish to borrow: ')
        print(new_book)
        name = input('Please enter your user name : ')
        borrow_book(new_book,name)

    if menu_choice == 3:
        ret_book = input('Please enter the title of the book you wish to return: ')
        name = input('Please enter your user name : ')
        time = int(input('''Please enter
          0 if the book is returned on time
          1 if the book is returned late. You will incur a fine of £3 :'''))
        return_book(ret_book,name,time)

    if menu_choice == 4:
        name = input('Please enter your user name : ')
        check_fines(name)

    if menu_choice == 5:
        print('Thank you for visiting the library today')
        break
        
    