# Создайте программу для игры в ""Крестики-нолики""

print('/' * 10, 'Крестики-нолики', '/' * 10)

board = list(range(1, 10))


def print_board(board):
    print('-'*13)
    for i in range(3):
        print('|', board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13)


def player_input(player_move):
    flag = False
    while not flag:
        player_inp = int(input('Куда будем ставить ' + player_move + '? '))
        if player_inp >= 1 and player_inp <= 9:
            if (str(board[player_inp-1])) not in 'XO':
                board[player_inp-1] = player_move
                flag = True
            else:
                print('Эта клетка занята!')
        else:
            print('Введите число от 1 до 9')


def win_check(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False            

def main_program(board):
    count = 0
    win = False
    while not win:
        print_board(board)
        if count % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        count += 1

        if count > 4:
            temp = win_check(board)
            if temp:
                print(temp,'Вы выиграли!')
                win = True
                break
        if count == 9:
            print('Ничья!')
            break
    print_board(board)        

main_program(board)
