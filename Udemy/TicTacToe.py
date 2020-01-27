board = [' ']*10
syms = ['','X','O']

def reset_board():
    global board
    board = [' ']*10

def print_board(board):
    print('\n'*128)
    print('   |   |   ')
    print(' %s | %s | %s ' % (board[1],board[2],board[3]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' %s | %s | %s ' % (board[4],board[5],board[6]))
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' %s | %s | %s ' % (board[7],board[8],board[9]))
    print('   |   |   ')

def game():
    reset_board()
    winner = 0
    turn = 1
    fin = False
    while not fin:
        print_board(board)
        play(turn)
        fin, winner = win(board)
        turn = turn % 2 + 1
    if winner == 0:
        print('The game was a draw!')
    else:
        print('Player %d wins!' % winner)

def play(turn):
    pos = 0
    sym = syms[turn]
    while pos == 0:
        attempt = int(input('Player %d, where would you like to play? ' % turn))
        if attempt in range(1,10) and board[attempt] == ' ':
            pos = attempt
    board[pos] = sym

def win(board):
    fin = False
    winner = 0
    xwin = ['X','X','X']
    owin = ['O','O','O']
    if board[1:4] == xwin or board[4:7] == xwin or board[7:10] == xwin or board[1:8:3] == xwin or board[2:9:3] == xwin or board[3:10:3] == xwin or board[1:10:4] == xwin or board[3:8:2] == xwin:
        fin = True
        winner = 1
    if board[1:4] == owin or board[4:7] == owin or board[7:10] == owin or board[1:8:3] == owin or board[2:9:3] == owin or board[3:10:3] == owin or board[1:10:4] == owin or board[3:8:2] == owin:
        fin = True
        winner = 2
    if ' ' not in set(board[1:10]):
        fin = True
    return fin, winner

game()