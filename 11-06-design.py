"""

Chess

    set up a new board
        create the data for the board
        display it somehow -> GUI, Text
    run game module = multiple functions
        check win condition
            checkmate = a function that can check the board state for that.
            check = the king is being attacked a function for that.
            stalemates = cycling board positions (more design needed)
                remember all board states based on their move.

    save game feature
        create some file format that is the chess board states

    load game feature

    computer AI
        difficulty level


"""

import unittest


def count_a(a_string):
    #if not isinstance(a_string, str):
    #    return 0
    count = 0
    for i in range(len(a_string)):
        if a_string[i].lower() == 'a':
            count += 1

    return count


class ACountTester(unittest.TestCase):

    def test_three_as(self):
         self.assertEqual(count_a('baaab'), 3)

    def test_five_as(self):
         self.assertEqual(count_a('aaaaa'), 5)

    def test_capital_as(self):
        self.assertEqual(count_a('AAABBAA'), 5)

    def test_problem_1(self):
        with self.assertRaises(TypeError):
            count_a(3)

unittest.main()
