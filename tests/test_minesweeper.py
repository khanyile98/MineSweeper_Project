import unittest
import minesweeper
from test_base import captured_io
from io import StringIO
import sys


class MyTestCase(unittest.TestCase):
    grid = [
        ['X', 0, 'X'],
        [0, 0, 'X'],
        [0, 0, 0]
    ]

    def test_generate_grids(self):
        for i in range(100):
            self.assertIsNotNone(minesweeper.generate_grid(5))

        matrix = [
            ['-', '-'],
            ['-', '-']
        ]

        grid = minesweeper.generate_grid(2)[1]
        self.assertEqual(grid, matrix)


    def test_user_inpur(self):
        with captured_io(StringIO("0 3\n0 2\n")) as (out, err):
            minesweeper.user_input(3)

        output = out.getvalue().strip()

        self.assertEqual("""\
Enter 2 points separated by space for the grid block: \
The values should be numbers from 0 to 2
Enter 2 points separated by space for the grid block:""", output)


    def test_check_win_true(self):
        display = [
        ['-', 3, '-'],
        [1, 3, '-'],
        [0, 1, 1]
        ]

        bool_true = minesweeper.check_win(self.grid, display)
        self.assertTrue(bool_true)


    def test_check_win_false(self):
        display = [
        ['-', 3, '-'],
        ['-', '-', '-'],
        [0, 1, 1]
        ]

        bool_false = minesweeper.check_win(self.grid, display)
        self.assertFalse(bool_false)


    def play_win(self):
        with captured_io(StringIO("3\n0 0\nn")) as (out, err):
            minesweeper.Game()

        output = out.getvalue().strip()
        self.assertNotEqual("""\
Enter the grid size: \
- - -
- - -
- - -\
Enter 2 points separated by space for the grid block: \
You loose!!\
********ORIGIONAL GRID********\
X 0 X
0 0 X
0 0 0\
Would you like to play again?? Y/n: \
Bye! Hope to see you next time!!!""", output)

    def test_database_tests_exists(self):
        import test_database

        self.assertTrue('test_database' in sys.modules, "test should be found")


if __name__ == '__main__':
    unittest.main()