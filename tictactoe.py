"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    """
    # Initialise counts
    Xcount = 0
    Ocount = 0

    # Get count of each symbol
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xcount += 1
            elif board[i][j] == O:
                Ocount += 1

    # Turn goes to O if X has more symbols, else X
    if Xcount > Ocount:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialise set
    actions = set()

    # Add all EMPTY cells to set
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check action is valid
    if board[action[0]][action[1]]:
        raise Exception('Invalid move.')

    newboard = copy.deepcopy(board)
    symbol = player(board)
    newboard[action[0]][action[1]] = symbol
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check each row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    # Check each column
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if winner
    if winner(board):
        return True

    # Check if board is full
    if len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # If winner
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    # If draw
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def MAX_VALUE(board):
        if terminal(board):
            return ((utility(board), None))
        v = -math.inf
        move = None
        for action in actions(board):
            value = max(v, MIN_VALUE(result(board, action))[0])
            if value > v:
                v, move = value, action
        return ((v, move))

    def MIN_VALUE(board):
        if terminal(board):
            return ((utility(board), None))
        v = math.inf
        move = None
        for action in actions(board):
            value = min(v, MAX_VALUE(result(board, action))[0])
            if value < v:
                v, move = value, action
        return ((v, move))

    if player(board) == X:
        return(MAX_VALUE(board)[1])
    else:
        return(MIN_VALUE(board)[1])
