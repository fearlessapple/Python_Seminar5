# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

player_count = 0
bot_count = 0
candy = 2021

print('Кидаем жребий!')
flag = randint(0, 1)
if flag == True:
    print('Поздравляем! Вы ходите первым!')
else:
    print('Увы, но выиграл бот.')     

def input_player():
    player_num = int(input('Введите кол-во конфет, которое хотите взять: '))
    while player_num > 28 or player_num < 1:
        print('Нарушаете правила игры!')
        player_num = int(input('Заново введите кол-во конфет, которое хотите взять: '))
    return player_num   

def print_player(a, b, c):
    print(f'Вы взяли {a} конфет, теперь у вас {b} конфет, осталось всего {c} конфет.')

def print_bot(d, e, f):
    print(f'Бот взял {d} конфет, теперь у него {e} конфет, осталось всего {f} конфет.')

while candy > 28:
    if flag:
        p_num = input_player()
        player_count += p_num
        candy -= p_num
        flag = False
        print_player(p_num, player_count, candy) 
    else:
        b_num = randint(1, 28)
        bot_count += b_num
        candy -= b_num
        flag = True
        print_bot(b_num, bot_count, candy)

if flag:
    print('Вы победили!')
else:
    print('Победил бот. Вы проиграли :(')    
