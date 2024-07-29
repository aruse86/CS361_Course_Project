import sqlite3


def login():
    print('Welcome to the login screen\n')
    user_name = input('Enter user name: ')
    password = input('Enter password: ')

    # Code here to send to microservice to get checked


def register(user_data_dictionary, cursor):
    print('Welcome to the registration screen\n')
    user_name = input('Create a user name: ')
    password = input('Create a password: ')

    # Code here to send to microservice to get checked

    # code here to add to user_name_password dictionary

    create_profile(user_name, user_data_dictionary, cursor)


def create_profile(user_name, user_data_dictionary, cursor):
    print('Create a Personal Profile!\n\n')

    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    phone = input('Enter your phone number: ')
    e_mail = input('Enter your e-mail address: ')
    discovery = input('Please tell us how you found us: ')

    # creates a table called user_data if it does not exist
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (user_name TEXT, first_name TEXT, last_name TEXT, "
                   "phone INTEGER, e_mail TEXT, discovery TEXT)")

    cursor.execute("INSERT INTO user_data (user_name, first_name, last_name, phone, e_mail, discovery) VALUES(?, ?, ?, ?, ?, ?)", (user_name, first_name, last_name, phone, e_mail, discovery))

    user_data_list = [first_name, last_name, phone, e_mail, discovery]

    # code here to add this info to a database for this username
    user_data_dictionary[user_name] = user_data_list

    print('\nThank you for registering with us. Your profile is now complete!')


def main():
    print('\nWelcome to your Wine Journal!\n')
    print('This is a place where you can log and keep track of your favorite wines for that special occasion\n'
          'or when you feel like cozying up on the couch watching a movie with a glass of wine in hand!\n')

    login_input = input('Enter ‘L’ to login to your profile or ‘R’ to register: ')

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    user_data_dictionary = {}

    if login_input.lower() == 'l':
        login()
    elif login_input.lower() == 'r':
        register(user_data_dictionary, cursor)

    connection.commit()

    print(connection.total_changes)


if __name__ != '__main__':
    pass
else:
    main()
