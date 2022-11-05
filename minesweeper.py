import random 
import update_display as ud


def generate_grid(size):
    original_grid = [[0 for i in range(size)] for j in range(size)]
    display_grid = [['-' for i in range(size)] for j in range(size)]

    points = []

    while len(points) < size:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)

        if (x, y) not in points:
            original_grid[x][y] = "X"
            points.append((x, y))

    return (original_grid, display_grid)


def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end=' ')
        print()


def user_input(size):
    x, y = list(map(int, input('Enter 2 points separated by space for the grid block: ').split()))

    if x in range(size) and y in range(size):
        return (x, y)
    print(f"The values should be numbers from 0 to {size - 1}")
    return user_input(size)


def check_win(original_grid, display_grid):

    for o_row, d_row in zip(original_grid, display_grid):
        for o_element, d_element in zip(o_row, d_row):
            if o_element == 0 and d_element == '-':
                return False
    return True


def Game():
    play = True
    size = int(input('Enter the grid size: '))
    original_grid, display_grid = generate_grid(size)

    while play:
        print_grid(display_grid)
        x, y = user_input(size)

        if original_grid[x][y] == 'X':
            print('You loose!!')
            print("ORIGIONAL GRID".center(30, '*'))
            print_grid(original_grid)
            play = False

        else:
            display_grid = ud.update_display(display_grid, original_grid, x, y)


        if check_win(original_grid, display_grid):
            print("You win!!")
            print("ORIGIONAL GRID".center(30, '*'))
            print_grid(original_grid)
            play = False

    if not play:
        choice = input("Would you like to play again?? Y/n: ")

        if choice.lower() in ['y', 'yes']:
            play = True
            return Game()

    print("Bye! Hope to see you next time!!!")


if __name__ == '__main__':
    Game()

