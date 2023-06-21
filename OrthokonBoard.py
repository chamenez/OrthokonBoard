"""
Name: Dominic Chavez
Date: 5/22/2021
Description: Code for a game of Orthokon.
"""


class OrthokonBoard:
    """
    Creates board, game status and moving ability.
    """

    def __init__(self):
        self._board = [
            ['R', 'R', 'R', 'R'],
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0'],
            ['Y', 'Y', 'Y', 'Y']
            ]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        return self._current_state

    def make_move(self, from_row, from_column, to_row, to_column):
        """Conditionals checking validity of movement."""

        if self._current_state != "UNFINISHED":
            return False

        """Checks for invalid starting position."""
        if from_row not in range(4) or from_column not in range(4):
            return False
        if to_row not in range(4) or to_column not in range(4):
            return False

        """Checks for player movement."""
        if self._board[to_row][to_column] == self._board[from_row][from_column]:
            return False

        if self._board[to_row][to_column] != "0":
            return False

        """Checks for valid diagonal or orthogonal."""
        y = abs(to_column - from_column)
        x = abs((to_row - from_row))
        if x != 0:
            if y / x != 1 and y / x != 0:
                return False

        """Diagonal move (column and row are both different)."""
        if from_row != to_row and from_column != to_column:
            # We know that a diagonal move has happened
            row_change = int((to_row - from_row) / abs(to_row - from_row))
            column_change = int((to_column - from_column) / abs(to_column - from_column))
            row_iter = from_row + row_change
            column_iter = from_column + column_change

            while row_iter != to_row and column_iter != to_column:
                if self._board[row_iter][column_iter] != '0':
                    return False
                row_iter += row_change
                column_iter += column_change

        """Orthogonal move (column XOR row are different)."""
        if from_row != to_row and from_column == to_column:
            # up-down
            row_change = int((to_row - from_row) / abs(to_row - from_row))  # SHOULD be 1 or -1
            row_iter = from_row + row_change

            while row_iter != to_row:
                if self._board[row_iter][from_column] != '0':
                    return False
                row_iter += row_change
        elif from_row == to_row and from_column != to_column:
            # left-right move
            column_change = int((to_column - from_column) / abs(to_column - from_column))  # SHOULD be 1 or -1
            column_iter = from_column + column_change

            while column_iter != to_column:
                if self._board[from_row][column_iter] != '0':
                    return False
                column_iter += column_change

        my_color = ''
        opponent_color = ''
        """Changes respective pieces on board."""
        if self._board[from_row][from_column] == 'Y':
            my_color = 'Y'
            opponent_color = 'R'
        else:
            my_color = 'R'
            opponent_color = 'Y'
        self._board[to_row][to_column] = my_color
        self._board[from_row][from_column] = '0'

        """Changes surrounding player to active player color."""
        if (to_row - 1) in range(4):
            if self._board[to_row - 1][to_column] == opponent_color:
                self._board[to_row - 1][to_column] = my_color

        if (to_row + 1) in range(4):
            if self._board[to_row + 1][to_column] == opponent_color:
                self._board[to_row + 1][to_column] = my_color

        if (to_column - 1) in range(4):
            if self._board[to_row][to_column - 1] == opponent_color:
                self._board[to_row][to_column - 1] = my_color

        if (to_column + 1) in range(4):
            if self._board[to_row][to_column + 1] == opponent_color:
                self._board[to_row][to_column + 1] = my_color

        """Checks for winner."""
        total_red = 0
        total_yellow = 0
        for i in range(4):
            for j in range(4):
                if self._board[i][j] == "R":
                    total_red += 1
                elif self._board[i][j] == "Y":
                    total_yellow += 1
        if total_red == 8:
            self._current_state = "RED_WON"
        elif total_yellow == 8:
            self._current_state = "YELLOW_WON"

        """Check for valid opponent moves."""
        valid_moves = 0

        for i in range(4):
            for j in range(4):
                if self._board[i][j] == opponent_color: #  Example if Red makes move, checks surroundings of yellow
                    # Check all the surrounding squares. First, see if they're valid. Then check if they're blank
                    if (i - 1) in range(4) and ((j - 1) in range(4)) and self._board[i - 1][j - 1] == '0':
                        valid_moves += 1
                        break
                    if (i - 1) in range(4) and self._board[i - 1][j] == '0':
                        valid_moves += 1
                        break
                    if (i - 1) in range(4) and ((j + 1) in range(4)) and self._board[i - 1][j + 1] == '0':
                        valid_moves += 1
                        break
                    if (j - 1) in range(4) and self._board[i][j - 1] == '0':
                        valid_moves += 1
                        break
                    if (j + 1) in range(4) and self._board[i][j + 1] == '0':
                        valid_moves += 1
                        break
                    if (i + 1) in range(4) and (j - 1) in range(4) and self._board[i + 1][j - 1] == '0':
                        valid_moves += 1
                        break
                    if (i + 1) in range(4) and self._board[i + 1][j] == '0':
                        valid_moves += 1
                        break
                    if (i + 1) in range(4) and (j + 1) in range(4) and self._board[i + 1][j + 1] == '0':
                        valid_moves += 1
                        break

        if valid_moves == 0:
            if my_color == 'R':
                self._current_state = "RED_WON"
            else:
                self._current_state = "YELLOW_WON"
        return True

    def see_board(self):
        for i in self._board:
            print(i)