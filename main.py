import sqlite3


def login(cursor, connection):
    print('\nWelcome to the login screen')
    user_name = input('Enter user name: ')
    password = input('Enter password: ')

    # Code here to send to microservice to get checked

    personal_home_page(user_name)


def register(cursor, connection):
    print('\nWelcome to the registration screen')
    user_name = input('Create a user name: ')
    password = input('Create a password: ')

    # Code here to send to microservice to get checked

    create_profile(user_name, password, cursor, connection)


def create_profile(user_name, password, cursor, connection):
    print('\nCreate a Personal Profile!')

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
    elif discovery == '2':
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
        personal_home_page(user_name)
    else:
        return 0


def edit_profile(user_name, cursor, connection):
    edit = input('\nEdit your Personal Profile!\nEnter 1 to edit your password, 2 to edit your first name, '
                 '3 to edit your last name, 4 to edit your phone number, 5 to edit your email address, '
                 'or any other key to return to your home page: ')

    if edit == '1':
        password = input('Enter your new_password: ')
        query = f'UPDATE user_data SET password = ? WHERE user_name = ?'
        cursor.execute(query, (password, user_name))
    elif edit == '2':
        first_name = input('Enter your new first name: ')
        query = f'UPDATE user_data SET first_name = ? WHERE user_name = ?'
        cursor.execute(query, (first_name, user_name))
    elif edit == '3':
        last_name = input('Enter your new last name: ')
        query = f'UPDATE user_data SET last_name = ? WHERE user_name = ?'
        cursor.execute(query, (last_name, user_name))
    elif edit == '4':
        phone = input('Enter your new phone number: ')
        query = f'UPDATE user_data SET phone = ? WHERE user_name = ?'
        cursor.execute(query, (phone, user_name))
    elif edit == '5':
        e_mail = input('Enter your new e-mail address: ')
        query = f'UPDATE user_data SET e_mail = ? WHERE user_name = ?'
        cursor.execute(query, (e_mail, user_name))
    else:
        personal_home_page(user_name)

    connection.commit()

    go_home = input('\nYour profile edits are now complete!\nEnter 1 to edit again, 2 to go to your '
                    'home page or any other key to exit: ')

    if go_home == '1':
        edit_profile(user_name, cursor, connection)
    elif go_home == '2':
        personal_home_page(user_name)
    else:
        return 0


def wine_journal_home(user_name):
    print(f'\nWelcome to your wine journal page!')
    entry = input('Enter 1 to view your journal, 2 to add a journal entry, 3 to edit an entry in your journal, '
                  '4 to delete an entry from your journal, any other key to return to your profile: ')

    journal_connect = sqlite3.connect(f'{user_name}.db')
    journal_cursor = journal_connect.cursor()

    journal_cursor.execute("CREATE TABLE IF NOT EXISTS wine_data (brand TEXT, type TEXT, region TEXT, "
                           "year INTEGER, varietal TEXT, comments TEXT)")
    journal_connect.commit()

    if entry == '1':
        print('\nBelow is your journal.')

        query = 'SELECT * FROM wine_data'
        journal_cursor.execute(query)
        output = journal_cursor.fetchall()
        if not output:
            print("There are no entries in your journal")
        else:
            for row in output:
                print(row)
    elif entry == '2':
        wine_brand = input('Enter the wine brand: ')
        wine_type = input('Enter the wine type: ')
        wine_region = input('Enter the wine region: ')
        wine_year = int(input('Enter the wine year: '))
        wine_varietal = input('Enter the wine varietal: ')
        wine_comments = input('Enter any other comments about the wine: ')

        journal_cursor.execute("INSERT INTO wine_data (brand, type, region, year, varietal, comments) "
                               "VALUES(?, ?, ?, ?, ?, ?)", (wine_brand, wine_type, wine_region, wine_year,
                                                            wine_varietal, wine_comments))
    elif entry == '3':
        entry = input('Which brand would you like to edit? ')
        edit_wine_journal(user_name, entry, journal_cursor, journal_connect)
    elif entry == '4':
        warning = input('Warning, this will permanently delete the entry. Enter 1 to continue or any other key to '
                        'exit.')
        if warning == '1':
            entry = input('Which brand would you like to delete? ')
            journal_cursor.execute("DELETE FROM wine_data WHERE brand = ?", (entry,))
    else:
        personal_home_page(user_name)

    journal_connect.commit()
    wine_journal_home(user_name)


def edit_wine_journal(user_name, entry, journal_cursor, journal_connect):
    edit = input(f'\nEdit {entry}\nEnter 1 to edit the wine type, 2 to edit the wine region, '
                 '3 to edit the wine year, 4 to edit the wine varietal, 5 to edit your comments, '
                 'or any other key to return to your wine journal page: ')

    if edit == '1':
        wine_type = input('Enter the new wine type: ')
        query = f'UPDATE wine_data SET type = ? WHERE brand = ?'
        journal_cursor.execute(query, (wine_type, entry))
    elif edit == '2':
        wine_region = input('Enter the new wine region: ')
        query = f'UPDATE wine_data SET region = ? WHERE brand = ?'
        journal_cursor.execute(query, (wine_region, entry))
    elif edit == '3':
        wine_year = input('Enter the new wine year: ')
        query = f'UPDATE wine_data SET year = ? WHERE brand = ?'
        journal_cursor.execute(query, (wine_year, entry))
    elif edit == '4':
        wine_varietal = input('Enter the new wine varietal: ')
        query = f'UPDATE wine_data SET varietal = ? WHERE brand = ?'
        journal_cursor.execute(query, (wine_varietal, entry))
    elif edit == '5':
        wine_comments = input('Enter your new comments: ')
        query = f'UPDATE wine_data SET comments = ? WHERE brand = ?'
        journal_cursor.execute(query, (wine_comments, entry))
    else:
        wine_journal_home(user_name)

    journal_connect.commit()

    go_home = input('\nYour journal entry edits are now complete!\nEnter 1 to edit again, 2 to go to your '
                    'wine journal page or any other key to exit: ')

    if go_home == '1':
        edit_wine_journal(user_name, entry, journal_cursor, journal_connect)
    elif go_home == '2':
        wine_journal_home(user_name)
    else:
        return 0


def personal_home_page(user_name):
    print(f'\nWelcome {user_name}! This is your profile, where you can view your wine journal, and edit your personal '
          f'profile information!')

    action = input('Enter 1 to view your journal, 2 to edit your profile, or 3 to exit the program: ')

    if action == '1':
        wine_journal_home(user_name)
    elif action == '2':
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        edit_profile(user_name, cursor, connection)
    else:
        quit()


def main():
    print('\nWelcome to your Wine Journal!')
    print('This is a place where you can log and keep track of your favorite wines for that special occasion\n'
          'or when you feel like cozying up on the couch watching a movie with a glass of wine in hand!\n')

    login_input = input('Enter ‘1’ to login to your account, 2 to register a new account, or any other key to exit '
                        'the program: ')

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    if login_input == '1':
        login(cursor, connection)
    elif login_input.lower() == '2':
        register(cursor, connection)

    connection.commit()

    print(connection.total_changes)

    connection.close()


if __name__ != '__main__':
    pass
else:
    main()
