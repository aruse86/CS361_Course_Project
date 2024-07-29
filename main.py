import sqlite3


def login(cursor):
    print('Welcome to the login screen\n')
    user_name = input('Enter user name: ')
    password = input('Enter password: ')

    # Code here to send to microservice to get checked

    personal_home_page(user_name, cursor)
    return 0


def register(cursor):
    print('Welcome to the registration screen\n')
    user_name = input('Create a user name: ')
    password = input('Create a password: ')

    # Code here to send to microservice to get checked

    create_profile(user_name, password, cursor)
    return 0


def create_profile(user_name, password, cursor):
    print('Create a Personal Profile!\n\n')

    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    phone = input('Enter your phone number: ')
    e_mail = input('Enter your e-mail address: ')

    discovery = input('Please tell us how you found us (Enter 1 for Social Media, 2 for Search Engine, 3 for Mail,'
                      '4 for Other: ')
    while 1 > int(discovery) > 4:
        discovery = input('Please enter a valid option (1 for Social Media, 2 for Search Engine, 3 for Mail,'
                          '4 for Other: ')
    if discovery == '1':
        discovery = 'Social Media'
    elif discovery == '4':
        discovery = 'Search Engine'
    elif discovery == '3':
        discovery = 'Mail'
    else:
        discovery = 'Other'

    journal = f'{user_name}.db'

    # creates a table called user_data if it does not exist
    cursor.execute("CREATE TABLE IF NOT EXISTS user_data (user_name TEXT, password TEXT, first_name TEXT,"
                   "last_name TEXT, phone INTEGER, e_mail TEXT, discovery TEXT, journal TEXT)")

    cursor.execute("INSERT INTO user_data (user_name, password, first_name, last_name, phone, e_mail, discovery,"
                   "journal) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (user_name, password, first_name, last_name, phone,
                                                               e_mail, discovery, journal))
    connection.commit()

    go_home = input('\nThank you for registering with us. Your profile is now complete!\n\nEnter 0 to go to your '
                    'home page or any other key to exit: ')

    if go_home == '0':
        personal_home_page(user_name, cursor)
    else:
        return 0


def edit_profile(user_name, cursor):
    edit = input('Edit your Personal Profile!\nEnter 1 to edit your first name, 2 to edit your last name, '
                 '3 to edit your phone number, 4 to edit your email address, or any other key to return '
                 'to your home page: ')

    if edit == '1':
        first_name = input('Enter your first name: ')
        query = f'UPDATE user_data SET first_name = {first_name} WHERE user_name = {user_name}'
        cursor.execute(query)
    elif edit == '2':
        last_name = input('Enter your last name: ')
        query = f'UPDATE user_data SET last_name = {last_name} WHERE user_name = {user_name}'
        cursor.execute(query)
    elif edit == '3':
        phone = input('Enter your phone number: ')
        query = f'UPDATE user_data SET phone = {phone} WHERE user_name = {user_name}'
        cursor.execute(query)
    elif edit == '4':
        e_mail = input('Enter your e-mail address: ')
        query = f'UPDATE user_data SET e_mail = {e_mail} WHERE user_name = {user_name}'
        cursor.execute(query)
    else:
        personal_home_page(user_name, cursor)

    go_home = input('\n. Your profile edits are now complete!\n\nEnter 1 to edit again, 2 to go to your '
                    'home page or any other key to exit: ')

    if go_home == '1':
        edit_profile(user_name, cursor)
    elif go_home == '2':
        personal_home_page(user_name, cursor)
    else:
        return 0


def personal_home_page(user_name, cursor):
    print(f'Welcome {user_name}! This is your profile, where you can view your wine journal, and edit your personal '
          f'profile information!\n')

    action = input('Enter 1 to view your journal, 2 to edit your profile, or 3 to exit the program: ')

    if action == '1':
        wine_journal()
    elif action == '2':
        edit_profile()
    else:
        return 0


def main():
    print('\nWelcome to your Wine Journal!\n')
    print('This is a place where you can log and keep track of your favorite wines for that special occasion\n'
          'or when you feel like cozying up on the couch watching a movie with a glass of wine in hand!\n')

    login_input = input('Enter ‘1’ to login to your account, 2 to register a new account, or any other key to exit '
                        'the program: ')

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    if login_input == '1':
        login(cursor)
    elif login_input.lower() == '2':
        register(cursor)
    else:
        return 0

    connection.commit()

    print(connection.total_changes)

    connection.close()

    return 0


if __name__ != '__main__':
    pass
else:
    main()
