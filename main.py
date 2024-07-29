def login():
    print('Welcome to the login screen\n')
    user_name = input('Enter user name: ')
    password = input('Enter password: ')

def register():
    print('Welcome to the registration screen\n')
    user_name = input('Create a user name: ')
    password = input('Create a password: ')


def main():
    print('\nWelcome to your Wine Journal!\n')
    print('This is a place where you can log and keep track of your favorite wines for that special occasion\n'
          'or when you feel like cozying up on the couch watching a movie with a glass of wine in hand!\n')

    login_input = input('Enter ‘L’ to login to your profile or ‘R’ to register: ')

    if login_input.lower() == 'l':
        login()
    elif login_input.lower() == 'r':
        register()



if __name__ != '__main__':
    pass
else:
    main()
