import databaseHandler

def enter_details():
    username = input('Username: ')
    password = input("Password: ")

    print("".center(40, '*'))
    print()

    if databaseHandler.Handler(username, password, 'login'):
        print("You have logged in successfuly")
        print(f"Welcome back, {username}")
        return True

    print("Either your username or password is incorrect.")
    choice = input("Do you want to try again (try) or create a new profile (new): ")

    if choice.lower() ==  'new':
        return False
    return enter_details()


def login():
    print(''.center(40, '*'))
    print("ENTER YOU LOGIN INFORMATION".center(40))
    print(''.center(40, '*'))
    print()

    return enter_details()


if __name__ == '__main__':
    login()