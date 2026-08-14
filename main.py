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


def play_round(score):
    board = create_board()
    current_player = 'X'
    while True:
        display_board(board)
        make_move(board, current_player)
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
    while True:
        display_header('TIC TAC TOE!')
        play_round(score)
        display_score(score)
        if input('Play again? (y/n): ').lower() != 'y':
            break

if __name__ == '__main__':
    play_game()