"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    xcount = 0
    ocount = 0
    for row in board:
        for box in row:
            if box is X:
                xcount += 1
            elif box is O:
                ocount += 1

    return X if xcount <= ocount else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionslist = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is EMPTY:
                actionslist.add((i, j))

    return actionslist


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] > 2 or action[1] > 2 or action[0] < 0 or action[1] < 0:
        raise Exception('invalid')

    if board[action[0]][action[1]] is not EMPTY:
        raise Exception('invalid')

    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    if winner(board):
        return True

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] is EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    state = winner(board)
    if state == X:
        return 1
    elif state == O:
        return -1
    else:
        return 0


def minval(board):
    if terminal(board):
        return utility(board)

    minvalue = 2
    for action in actions(board):
        new_board = result(board, action)

        value = maxval(new_board)
        minvalue = min(value, minvalue)

    return minvalue


def maxval(board):
    if terminal(board):
        return utility(board)

    maxvalue = -2
    for action in actions(board):
        new_board = result(board, action)

        value = minval(new_board)
        maxvalue = max(value, maxvalue)

    return maxvalue


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # return random.choice(actions(board))

    bestaction = None

    if not terminal(board):
        if player(board) == X:
            maxvalue = -2
            for action in actions(board):
                new_board = result(board, action)

                value = minval(new_board)
                if value > maxvalue:
                    bestaction = action
                    maxvalue = value

        if player(board) == O:
            minvalue = 2
            for action in actions(board):
                new_board = result(board, action)

                value = maxval(new_board)
                if value < minvalue:
                    bestaction = action
                    minvalue = value

    return bestaction
