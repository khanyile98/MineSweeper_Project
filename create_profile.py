import databaseHandler


def details():
    username = input('Enter a username: ')
    
    while True:
        password = input('Enter password: ')
        password_again = input("Re-enter the password: ")

        if password == password_again:
            return username, password

        print("The password is not the same")


def create_details():
    print("".center(40, '*'))
    print("LET'S CREATE A PROFILE FOR YOU".center(40))
    print("".center(40, '*'))
    print()

    username, password = details()
    databaseHandler.Handler(username, password, 'create')

    print("your profile was successfully created.")
    

if __name__ == '__main__':
    create_details()

    



