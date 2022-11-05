import minesweeper
import create_profile
import login_to_profile


def Handler():
    print("".center(40, '*'))
    print("WELCOME TO MINESWEEPER".center(40))
    print("".center(40, '*'))
    print()

    bool_true = False
    choice = input("Is this your first time playing with us? Y/n: ")
        
    if choice.lower() == 'y':
        create_profile.create_details()

    while  not bool_true:
        bool_true = login_to_profile.login()

    minesweeper.Game()


if __name__ == '__main__':
    Handler()
        

    