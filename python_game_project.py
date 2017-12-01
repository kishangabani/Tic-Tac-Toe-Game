from IPython.display import clear_output
import random


def display_game_board(board):
    clear_output()
    print("   |   | ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   | ")
    print("-------------")
    print("   |   | ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   | ")
    print("-------------")
    print("   |   | ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   | ")


def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input("PLAYER 1 : What Do You want 'X' or 'O' ?")

    if marker.upper() == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def winner_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[1] == mark and board[4] == mark) or
            (board[2] == mark and board[8] == mark and board[5] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark))


def random_choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check_avail(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check_avail(board, i):
            return False
    return True


def player_choose_position(board):      #Choose the position one by one, for both player
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check_avail(board, int(position)):
        position = input("Choose your next position : [1-9] ")

    return int(position)


def reaplay_game():
    return input("Do you want to play again? Enter YES or NO ").startswith('Y')


print("Tic Tac Toe Game !!!")  # PYTHON

while True:
    game_board = [' '] * 10
    player1_mark, player2_mark = player_input()
    player_turn = random_choose_first()
    print(player_turn + " will play FIRST!")
    game_running = True

    while game_running:
        if player_turn == "Player 1":   #For Player 1

            display_game_board(game_board)
            position = player_choose_position(game_board)
            place_marker(game_board, player1_mark, position)

            if winner_check(game_board, player1_mark):
                display_game_board(game_board)
                print("Player 1 win the GAME!!!!")
                game_running = False
            else:
                if full_board_check(game_board):
                    display_game_board(game_board)
                    print("Game is a DRAW!!")
                    break
                else:
                    player_turn = 'Player 2'
        else:
            display_game_board(game_board)      #For Player 2
            position = player_choose_position(game_board)
            place_marker(game_board, player2_mark, position)

            if winner_check(game_board, player2_mark):
                display_game_board(game_board)
                print("Player 2 win the GAME!!!!")
                game_running = False

            else:
                if full_board_check(game_board):
                    display_game_board(game_board)
                    print("Game is a DRAW!!!")
                    break
                else:
                    player_turn = 'Player 1'

    if not reaplay_game():
        break
