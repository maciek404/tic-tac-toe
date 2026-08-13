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
        if position in ['1','2','3','4','5','6','7','8','9']:
            if board[int(position) - 1] == ' ':
                board[int(position) - 1] = player
                return board
            else:
                print("That position is already taken!")
        else:
            print("Wrong input, please try again!")

def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for comb in winning_combinations:
        if board[comb[0]] == player and board[comb[1]] == player and board[comb[2]] == player:
            return True

    return False

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

print("Welcome to Tic Tac Toe!")
display_board(board)
while True:
    make_move(board, 'X')
    display_board(board)
    if check_winner(board, 'X'):
        print(f'Player X wins!')
        break
    elif ' ' not in board:
        print("It's a draw!")
        break
    make_move(board, 'O')
    display_board(board)
    if check_winner(board, 'O'):
        print('Player O wins!')
        break
    elif ' ' not in board:
        print("It's a draw!")
        break
