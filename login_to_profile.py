import databaseHandler
import getpass

def enter_details():
    """
    * This function askes the user for their profile login details.
    * If the details are correct they will then play the game
    * If not, they will be asked if they want to try again or
    would prefer making a new profle
    """

    username = input('Username: ')
    password = getpass.getpass(prompt="Password: ", stream=None)

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