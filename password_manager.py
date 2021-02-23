#password_manager.py
#create and display passwords for users
#josephine.wong, Feb 22

#initialise variables and lists
name = ''
age = ''

#create an empty list to store usernames and passwords for web/apps
password_list = []

#create a list with existing members and sstore new member details
member_list = []

#the menu() function prints out the menu for user to coose an option and returns user option to main routine
def menu(name,age):
  print('Hello,',name)
  if age > 13:
    print('Sorry, you do not qualify to open an account.')
  else:
    mode = input('''Choose a mode by entering the number:1. Add passwords 2. View passwords 3. Exit  :''').strip()
    return mode

#main routine - run main progrm in a loop
print('Welcome to Password Manager!')

name = input('What is your name:')

for name in range(member_list):
  log_in = input('Enter password: ')
  if
while True:
  try:
    age = float(input('What is your age:'))
    chosen_option = menu(name,age)
  except ValueError:
    print('please enter an intergers')

#while true
while True:
  chosen_option = menu(name,age)
  if chosen_option == '1':
  #call add_tasks function if user chooses 1
    print('Successful')
    print('Add Password')
    add_details = input(':').append(password_list)

  #add_details()
#call add_tasks function if the user chooses 2
  elif chosen_option == '2':
    print('Successful')
    print(view_list)
  #view_list()
  elif chosen_option == '3':
    break
#say goodbye and end programme
  else:
  #invaild option
    print('That was not a vaild option, please try again')







print('Goodbye, thanks for using password manager')