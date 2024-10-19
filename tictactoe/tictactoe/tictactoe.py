"""
Tic Tac Toe Player
"""

import math, copy

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
    count_x = 0
    count_o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x +=1
            elif board[i][j] == O:
                count_o +=1
    if count_x == count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    if possible_actions == None:
        return False
    else:
        return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]] != EMPTY or action[0] < 0 or action[1] < 0:
        raise ValueError
    else:
        board2 = copy.deepcopy(board)
        board2[action[0]][action[1]] = player(board2)
        return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        elif board[0][j] == board[1][j] == board[2][j] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O

    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None or not any(EMPTY in row for row in board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]
    elif player(board) == O:
        return min_value(board)[1]


def max_value(board):
    optimal_move = None
    if terminal(board):
        return utility(board), optimal_move
    v = -math.inf
    for action in actions(board):
        min_val = min_value(result(board, action))[0]
        if min_val > v:
            v = min_val
            optimal_move = action
    return v, optimal_move

def min_value(board):
    optimal_move = None
    if terminal(board):
        return utility(board), optimal_move
    v = math.inf
    for action in actions(board):
        max_val = max_value(result(board, action))[0]
        if max_val < v:
            v = max_val
            optimal_move = action
    return v, optimal_move

