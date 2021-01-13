#
# Project: Kunstmatige intelligentie in Vier op een rij
#
# names: Dylan Ploeger & Christiaan de Jong
#

import random


def in_a_row_n_east(char, row_start, col_start, data, length):
    """Starting from (row, col) of (row_start, col_start)
       within the 2d list-of-lists data (array),
       returns True if there are length amount of chars in a row
       heading east and returns False otherwise.
    """
    height = len(data)
    width = len(data[0])
    if row_start < 0 or row_start > height - 1:
        return False
    if col_start < 0 or col_start + (length-1) > width - 1:
        return False
    for i in range(length):
        if data[row_start][col_start+i] != char:
            return False
    return True


def in_a_row_n_south(char, row_start, col_start, data, length):
    """Starting from (row, col) of (row_start, col_start)
       within the 2d list-of-lists data (array),
       returns True if there are length amount of chars in a row
       heading south and returns False otherwise.
    """
    height = len(data)
    width = len(data[0])
    if row_start < 0 or row_start + (length - 1) > height - 1:
        return False
    if col_start < 0 or col_start > width - 1:
        return False
    for i in range(length):
        if data[row_start + i][col_start] != char:
            return False
    return True


def in_a_row_n_northeast(char, row_start, col_start, data, length):
    """Starting from (row, col) of (row_start, col_start)
       within the 2d list-of-lists data (array),
       returns True if there are length amount of chars in a row
       heading northeast and returns False otherwise.
    """
    height = len(data)
    width = len(data[0])
    if row_start - (length - 1) < 0 or row_start > height - 1:
        return False
    if col_start < 0 or col_start + (length - 1) > width - 1:
        return False
    for i in range(length):
        if data[row_start - i][col_start + i] != char:
            return False
    return True


def in_a_row_n_southeast(char, row_start, col_start, data, length):
    """Starting from (row, col) of (row_start, col_start)
       within the 2d list-of-lists data (array),
       returns True if there are length amount of chars in a row
       heading southeast and returns False otherwise.
    """
    height = len(data)
    width = len(data[0])
    if row_start < 0 or row_start + (length - 1) > height - 1:
        return False
    if col_start < 0 or col_start + (length - 1) > width - 1:
        return False
    for i in range(length):
        if data[row_start + i][col_start + i] != char:
            return False
    return True


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]
        self.win_length = 4

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2 * self.width + 1) * '-' + '\n'

        for col in range(0, self.width):
            s += ' ' + str(col % 10)

        return s

    def add_move(self, col, ox):
        """Adds a move to the Board.data, with given (int) column and (String x|o)stone character"""
        for row in range(self.height - 1, -1, -1):
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                break

    def clear(self):
        """Clears the (self.data) board"""
        self.data = [[' '] * self.width for row in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.set_board('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.set_board('000000') to
           see them alternate in the left column.

           move_string must be a string of one-digit integers.
        """
        next_checker = 'X'  # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allow_move(self, col):
        """Checks if the move is valid."""
        if col < 0 or col >= self.width:
            return False

        for row in range(self.height - 1, -1, -1):
            if self.data[row][col] == ' ':
                return True
        return False

    def is_full(self):
        """Checks if the Board full"""
        for row in range(0, self.height):
            for col in range(0, self.width):
                if self.data[row][col] == ' ':
                    return False
        return True

    def delete_move(self, col):
        """Deletes last move in a column"""
        for row in range(0, self.height):
            if self.data[row][col] == 'X' or self.data[row][col] == 'O':
                self.data[row][col] = ' '
                break

    def wins_for(self, char):
        """Checks char is a winner."""
        for row in range(self.height):
            for col in range(self.width):
                if in_a_row_n_east(char, row, col, self.data, self.win_length):
                    return True
                if in_a_row_n_south(char, row, col, self.data, self.win_length):
                    return True
                if in_a_row_n_northeast(char, row, col, self.data, self.win_length):
                    return True
                if in_a_row_n_southeast(char, row, col, self.data, self.win_length):
                    return True
        return False

    def host_game(self):
        """Host a game of connect 4"""
        print('Connect 4')
        print(self)
        while True:
            # Player X check input
            while True:
                column_for_x = int(input("Choose a column player X: "))
                if self.allow_move(column_for_x):
                    break
            # Player X set input
            self.add_move(column_for_x, 'X')
            print(self)
            # Player X check win.
            if self.wins_for('X'):
                print('Player X wins!')
                break

            # Check if board is full
            if self.is_full():
                print("Nobody wins and the board is full!")
                break

            # Player O check input
            while True:
                column_for_o = int(input("Choose a column player O: "))
                if self.allow_move(column_for_o):
                    break
            # Player O set input
            self.add_move(column_for_o, 'O')
            print(self)
            # Player O check win.
            if self.wins_for('O'):
                print('Player O wins!')
                break

            # Check if board is full
            if self.is_full():
                print("Nobody wins and the board is full!")
                break


class Player:
    """An AI player for Connect Four."""

    def __init__(self, char, tie_breaking_type, turns):
        """Construct a player for a given checker, tie-breaking type,
           and turns."""
        self.char = char
        self.tie_breaking_type = tie_breaking_type
        self.turns = turns

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player: char = " + self.char + ", "
        s += "tie_breaking_type = " + self.tie_breaking_type + ", "
        s += "turns = " + str(self.turns)
        return s

    def opp_char(self):
        """Returns the opponents (String) character"""
        if self.char == 'X':
            return 'O'
        elif self.char == 'O':
            return 'X'
        # else: error char needs to be X or O...

    def score_board(self, board):
        """Gives a score to board,
        100.0 points if self.char wins,
        50.0 points if self.char did not win or lose,
        0.0 if self.char loses.
        """
        if board.wins_for(self.char):
            return 100.0
        elif board.wins_for(self.opp_char()):
            return 0.0
        else:
            return 50.0

    def tiebreak_move(self, scores):
        """
        Returns the column (index) with the highest score from (list) scores,
        if there are multiple scores the same as the highest score use the self.tie_breaking_type to get the right column.
        LEFT: get the column of the most highest score that is the most to the left of the board.
        RIGHT: get the column of the most highest score that is the most to the right of the board.
        RANDOM: get the column of the most highest score randomly.
        """
        highest_score = max(scores)
        max_indices = [index for index, score in enumerate(scores) if score == highest_score]

        if self.tie_breaking_type == "LEFT":
            return min(max_indices)
        elif self.tie_breaking_type == "RIGHT":
            return max(max_indices)
        elif self.tie_breaking_type == "RANDOM":
            return random.choice(max_indices)



#
# Tests Class Board
#


board1 = Board(7, 6)
board2 = Board(10, 10)
board3 = Board(3, 3)
board4 = Board(5, 5)
board5 = Board(6, 7)

#
# Tests Board.__repr__()
#
assert board1.__repr__() == \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '---------------\n' \
        ' 0 1 2 3 4 5 6'
assert board2.__repr__() == \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '---------------------\n' \
        ' 0 1 2 3 4 5 6 7 8 9'
assert board3.__repr__() == \
        '| | | |\n' \
        '| | | |\n' \
        '| | | |\n' \
        '-------\n' \
        ' 0 1 2'
assert board4.__repr__() == \
        '| | | | | |\n' \
        '| | | | | |\n' \
        '| | | | | |\n' \
        '| | | | | |\n' \
        '| | | | | |\n' \
        '-----------\n' \
        ' 0 1 2 3 4'
assert board5.__repr__() == \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '-------------\n' \
        ' 0 1 2 3 4 5'

#
# Tests Board.add_move(col, ox)
#
board1.add_move(0, 'X')
board1.add_move(0, 'O')
board1.add_move(0, 'X')
board1.add_move(3, 'O')
board1.add_move(4, 'O')
board1.add_move(5, 'O')
board1.add_move(6, 'O')
assert board1.__repr__() == \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '|X| | | | | | |\n' \
        '|O| | | | | | |\n' \
        '|X| | |O|O|O|O|\n' \
        '---------------\n' \
        ' 0 1 2 3 4 5 6'
board2.add_move(5, 'X')
board2.add_move(6, 'O')
board2.add_move(6, 'X')
board2.add_move(7, 'O')
board2.add_move(7, 'O')
board2.add_move(7, 'X')
board2.add_move(8, 'O')
board2.add_move(8, 'O')
board2.add_move(8, 'O')
board2.add_move(8, 'X')
board2.add_move(9, 'O')
board2.add_move(9, 'O')
board2.add_move(9, 'O')
board2.add_move(9, 'O')
board2.add_move(9, 'X')
assert board2.__repr__() == \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | |X|\n' \
        '| | | | | | | | |X|O|\n' \
        '| | | | | | | |X|O|O|\n' \
        '| | | | | | |X|O|O|O|\n' \
        '| | | | | |X|O|O|O|O|\n' \
        '---------------------\n' \
        ' 0 1 2 3 4 5 6 7 8 9'
board3.add_move(1, 'X')
board3.add_move(1, 'O')
board3.add_move(1, 'X')
assert board3.__repr__() == \
        '| |X| |\n' \
        '| |O| |\n' \
        '| |X| |\n' \
        '-------\n' \
        ' 0 1 2'

#
# Tests
#
board1.clear()
assert board1.__repr__() == \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '| | | | | | | |\n' \
        '---------------\n' \
        ' 0 1 2 3 4 5 6'
board2.clear()
assert board2.__repr__() == \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '| | | | | | | | | | |\n' \
        '---------------------\n' \
        ' 0 1 2 3 4 5 6 7 8 9'
board3.clear()
assert board3.__repr__() == \
        '| | | |\n' \
        '| | | |\n' \
        '| | | |\n' \
        '-------\n' \
        ' 0 1 2'

#
# Tests Board.allow_move(col)
#
board3.add_move(0, 'X')
board3.add_move(0, 'X')
board3.add_move(0, 'X')
assert not board3.allow_move(0)
assert board3.allow_move(1)
assert board3.allow_move(2)
assert not board3.allow_move(-1)
assert not board3.allow_move(3)

#
# Tests Board.is_full()
#
assert not board3.is_full()
board3.add_move(1, 'X')
board3.add_move(1, 'X')
board3.add_move(1, 'X')
board3.add_move(2, 'X')
board3.add_move(2, 'X')
board3.add_move(2, 'X')
assert board3.is_full()
board4.add_move(0, 'X')
assert not board4.is_full()
board4.set_board("0000011111222223333344444")
assert board4.is_full()

#
# Tests Board.delete_move()
#
board5.add_move(1, 'X')
board5.add_move(2, 'O')
board5.add_move(2, 'O')
board5.add_move(3, 'O')
board5.add_move(1, 'X')
board5.delete_move(0)
board5.delete_move(1)
board5.delete_move(1)
board5.delete_move(1)
board5.delete_move(2)
assert board5.__repr__() == \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | | | | | |\n' \
        '| | |O|O| | |\n' \
        '-------------\n' \
        ' 0 1 2 3 4 5'

#
# Tests Board.wins_for(ox)
#
board1.set_board('00102030')
assert board1.wins_for('X')
assert board1.wins_for('O')
board1.clear()
board1.set_board('23344545515')
assert board1.wins_for('X')
assert not board1.wins_for('O')


#
# Tests Class Player
#

#
# Tests Player.__repr__()
#
player1 = Player('X', 'LEFT', 10)
assert player1.__repr__() == "Player: char = X, tie_breaking_type = LEFT, turns = 10"
player2 = Player('O', 'RANDOM', 7)
assert player2.__repr__() == "Player: char = O, tie_breaking_type = RANDOM, turns = 7"
player3 = Player('O', 'RIGHT', 6)
assert player3.__repr__() == "Player: char = O, tie_breaking_type = RIGHT, turns = 6"
player4 = Player('X', 'RANDOM', 5)
assert player4.__repr__() == "Player: char = X, tie_breaking_type = RANDOM, turns = 5"
player5 = Player('O', 'LEFT', 1)
assert player5.__repr__() == "Player: char = O, tie_breaking_type = LEFT, turns = 1"

#
# Tests Player.opp_char()
#
assert player1.opp_char() == 'O'
assert player2.opp_char() == 'X'
assert player3.opp_char() == 'X'
assert player4.opp_char() == 'O'
assert player5.opp_char() == 'X'

#
# Tests Player.score_board(board)
#
board1.clear()
board1.set_board('01020305')
assert player1.score_board(board1) == 100.0
assert player2.score_board(board1) == 0.0
board1.clear()
assert player1.score_board(board1) == 50.0
assert player2.score_board(board1) == 50.0

#
# Tests Player.tiebreak_move(scores)
#
scores = [0, 0, 50, 0, 50, 50, 0]
assert player1.tiebreak_move(scores) == 2
assert player2.tiebreak_move(scores) in [2, 4, 5]  # random
assert player3.tiebreak_move(scores) == 5
scores = [0, 0, 50, 0, 100, 50, 0]
assert player1.tiebreak_move(scores) == 4
assert player2.tiebreak_move(scores) == 4  # random, but one choice
assert player3.tiebreak_move(scores) == 4


