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

def display_board(board):
    horizontal_line = '---+---+---'
    print(f'\n {board[0]} | {board[1]} | {board[2]}')
    print(horizontal_line)
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print(horizontal_line)
    print(f' {board[6]} | {board[7]} | {board[8]}\n')

def make_move(board, player):
    while True:
        position = input(f"Player {player}, choose a position (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9:
            index = int(position) - 1
            if board[index] == ' ':
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

def play_game():

    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']

    print("Welcome to Tic Tac Toe!")
    display_board(board)
    current_player = 'X'
    while True:
        make_move(board, current_player)
        display_board(board)
        if check_winner(board, current_player):
            print(f'Player {current_player} wins!')
            break
        elif ' ' not in board:
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    play_game()