import random
LINE_DOUBLE = '================================='
LINE_SINGLE = '---------------------------------'
EMPTY = ' '
X_COLOR = '\033[91m'
O_COLOR = '\033[94m'
RESET = '\033[0m'
WINNING_COMBINATIONS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

def display_score(score):
    print(LINE_SINGLE)
    print('              SCORE')
    print(LINE_SINGLE)
    print(f"    X: {score['X']}     O: {score['O']}     Draws: {score['Draws']}")
    print(LINE_SINGLE)

def display_header(text):
    print(LINE_DOUBLE)
    print(f'           {text}')
    print(LINE_DOUBLE)

def display_board(board):
    horizontal_line = '---+---+---'
    print(f'\n            {color_symbol(board[0])} | {color_symbol(board[1])} | {color_symbol(board[2])}')
    print(f'           {horizontal_line}')
    print(f'            {color_symbol(board[3])} | {color_symbol(board[4])} | {color_symbol(board[5])}')
    print(f'           {horizontal_line}')
    print(f'            {color_symbol(board[6])} | {color_symbol(board[7])} | {color_symbol(board[8])}\n')

def create_board():
    return [EMPTY] * 9

def color_symbol(symbol):
    if symbol == 'X':
        return f"{X_COLOR}X{RESET}"
    elif symbol == 'O':
        return f"{O_COLOR}O{RESET}"
    return symbol

def choose_game_mode():
    while True:
        print("1. Player vs Player")
        print("2. Player vs AI")
        choice = input("Choose game mode (1/2): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Wrong input, please choose 1 or 2!")


def make_ai_move(board):
    move = find_winning_move(board, 'O')
    if move is not None:
        board[move] = 'O'
    else:
        move = find_winning_move(board, 'X')
        if move is not None:
            board[move] = 'O'
        else:
            move = find_preferred_move(board)
            if move is not None:
                board[move] = 'O'
            else:
                available_positions = [pos_index for pos_index in range(9) if board[pos_index] == EMPTY]
                board[random.choice(available_positions)] = 'O'

def find_winning_move(board, player):
    for comb in WINNING_COMBINATIONS:
        if board[comb[0]] == player and board[comb[1]] == player and board[comb[2]] == EMPTY:
            return comb[2]
        elif board[comb[1]] == player and board[comb[2]] == player and board[comb[0]] == EMPTY:
            return comb[0]
        elif board[comb[0]] == player and board[comb[2]] == player and board[comb[1]] == EMPTY:
            return comb[1]

def find_preferred_move(board):
    all_corners = [0, 2, 6, 8]
    empty_corners = []
    if board[4] == EMPTY:
        return 4
    for corner in all_corners:
        if board[corner] == EMPTY:
            empty_corners.append(corner)
    if empty_corners:
        return random.choice(empty_corners)
    return None

def make_move(board, player):
    while True:
        position = input(f"Player {player}, choose a position (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9:
            index = int(position) - 1
            if board[index] == EMPTY:
                board[index] = player
                break
            else:
                print("That position is already taken!")
        else:
            print("Wrong input, please try again!")

def check_winner(board, player):
    for comb in WINNING_COMBINATIONS:
        if all(board[index] == player for index in comb):
            return True
    return False

def play_round(score, game_mode):
    board = create_board()
    current_player = 'X'
    while True:
        if game_mode == '1':
            display_board(board)
            make_move(board, current_player)
        else:
            if current_player == 'X':
                display_board(board)
                make_move(board, current_player)
            else:
                make_ai_move(board)
        if check_winner(board, current_player):
            score[current_player] += 1
            display_header(f"PLAYER {current_player} WINS!")
            display_board(board)
            break
        elif EMPTY not in board:
            score['Draws'] += 1
            display_header("IT'S A DRAW!")
            display_board(board)
            break
        current_player = 'O' if current_player == 'X' else 'X'


def play_game():

    score = {
        'X': 0,
        'O': 0,
        'Draws': 0
    }
    display_header('TIC TAC TOE!')
    game_mode = choose_game_mode()
    while True:
        play_round(score, game_mode)
        display_score(score)
        if input('Play again? (y/n): ').lower() != 'y':
            break

if __name__ == '__main__':
    play_game()