from helper import *
import math
import copy

BLOCK_LENGTH = 4
EMPTY = 0
HUMAN_TOKEN = 2
AI_TOKEN = 1

def count_token(block, token):
        return block.count(token)


def count_empty(block):
    return block.count(EMPTY)

# Makes an evaluation based on blocks of 4 tokens
def evaluate_block(block, token):
    score = 0
    token_count = count_token(block, token)
    empty_count = count_empty(block)
    opponent_token_count = count_token(block, opponent(token))

    if token_count == 4:
        score += 1000
    elif token_count == 3 and empty_count == 1:
        score += 20
    elif token_count == 2 and empty_count == 2:
        score += 8

    if opponent_token_count == 3 and empty_count == 1:
        score -= -16

    return score


# Changes the player
def opponent(player):
    if player == AI_TOKEN:
        return HUMAN_TOKEN
    else:
        return AI_TOKEN


# Evaluates the position of the token
def evaluate_position(arr, player):
    score = 0

    # # Score horizontal
    for r in range(N_ROWS):
        for c in range(N_COLS - 3):
            block = [arr[r][c + i] for i in range(BLOCK_LENGTH)]
            score += evaluate_block(block, player)

    # # Score vertical
    for c in range(N_COLS):
        for r in range(N_ROWS - 3):
            block = [arr[r + i][c] for i in range(BLOCK_LENGTH)]
            score += evaluate_block(block, player)

    # # Score positive diagonal
    for r in range(N_ROWS - 3):
        for c in range(N_COLS - 3):
            block = [arr[r + i][c + i] for i in range(BLOCK_LENGTH)]
            score += evaluate_block(block, player)

    # # Score negative diagonal
    for r in range(N_ROWS - 3):
        for c in range(N_COLS - 3):
            block = [arr[r + 3 - i][c + i] for i in range(BLOCK_LENGTH)]
            score += evaluate_block(block, player)

    # # Score center column
    center_count = 0
    for i in range(N_ROWS):
        if arr[i][N_COLS // 2] == player:
            center_count += 1
    score += center_count * 5
    return score


# returns a list of all available locations

def get_available_locations(arr):
    return [col for col in range(N_COLS) if not column_is_full(arr, col)]

# Checks if the node is a terminal one
def if_terminal_node(arr):
    return is_victory(arr) or len(get_available_locations(arr)) == 0


# MinMax algorithm combined with alpha-beta pruning for optimization.
def minimax(arr, depth, alpha, beta, player, maxPlayer):
    available_locations = get_available_locations(arr)
    is_terminal = if_terminal_node(arr)
    if depth == 0 or is_terminal:
        if is_terminal:
            if is_victory(arr) == player:
                return (None, 10000000000000000)
            elif is_victory(arr) == opponent(player):
                return (None, -1000000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, evaluate_position(arr, player))
    if maxPlayer:
        value = -math.inf
        column = random.choice(available_locations)
        for col in available_locations:
            arr_copy = copy.deepcopy(arr)
            place_token(arr_copy, col, player)
            last_score = minimax(arr_copy, depth - 1, alpha, beta, player, False)[1]
            if last_score > value:
                value = last_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(available_locations)
        for col in available_locations:
            arr_copy = copy.deepcopy(arr)
            place_token(arr_copy, col, opponent(player))
            last_score = minimax(arr_copy, depth - 1, alpha, beta, player, True)[1]
            if last_score < value:
                value = last_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

'''
def ai(arr, player):
    col, minimax_score = minimax(arr, 1, -math.inf, math.inf, player, True)
    return col
'''


#the heuristic function
def ai(arr, player):
    available_locations = get_available_locations(arr)
    best_score = -10000
    best_choice = random.choice(available_locations)
    for col in available_locations:
        temp_arr= copy.deepcopy(arr)
        place_token(temp_arr, col, player)
        score = evaluate_position(temp_arr, player)
        if score > best_score:
            best_score = score
            best_choice = col

    return best_choice



'''
def ai(arr, player):
    """
    :param arr: current status of the board as type list[list[int]].
    The integers can either be 0 (cell empty), 1 (token of player 1) or 2 (token of player 2).
    :param player: Integer which is either 1 (turn of player 1) or 2 (turn of player 2).
    :return: Integer between 0 and 6 indicating in which row the next token shall be placed.

    Write your own AI in this function, do not change the function signature.
    Feel free to use any of the constants/methods in the helper.py / config.py file.
    You can/shall also override the ai() function in ai2.py to let
    different versions of you AI compete against each other.
    """

    # randomly place tokens
    while True:
        col = random.randint(0, N_COLS - 1)
        if not column_is_full(arr, col):
            return col
'''

'''
def ai(board, piece):
    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        temp_board = copy.deepcopy(board)
        place_token(temp_board, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col
'''


'''
def ai(arr, player):
    """
    :param arr: current status of the board as type list[list[int]].
    The integers can either be 0 (cell empty), 1 (token of player 1) or 2 (token of player 2).
    :param player: Integer which is either 1 (turn of player 1) or 2 (turn of player 2).
    :return: Integer between 0 and 6 indicating in which row the next token shall be placed.

    Write your own AI in this function, do not change the function signature.
    Feel free to use any of the constants/methods in the helper.py / config.py file.
    You can/shall also override the ai() function in ai2.py to let
    different versions of you AI compete against each other.
    """

    # randomly place tokens
    while True:
        col = random.randint(0, N_COLS - 1)
        if not column_is_full(arr, col):
            return col
'''
'''
def ai(arr, player):
    # randomly place tokens
    while True:
        col = random.randint(0, N_COLS - 1)
        if not column_is_full(arr, col):
            return col

'''