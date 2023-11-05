# крестики нолики
print("========= Крестики- нолики =============")

#создаем список клеток игрового поля
field = list(range(1,10))
# функция рисования
def draw_board(field):
     print('-'*12)
     for i in range(3):
        print('|', field[0+i*3], '|', field[1+i*3], '|', field[2+i*3], '|' )
        print('-'*12)

#функция определения ячейки ввода
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input('Куда поставим ' + player_token + ' ?')

        try:
            player_answer = int(player_answer)
        except:
            print('Неккоректный ввод')
            continue
        if player_answer >= 1 and player_answer <=9:
            if(str(field[player_answer - 1]) not in "XO"):
                field[player_answer -1] = player_token
                valid = True
            else:
                print("Эта клетка занята")
        else:
            print('Введите число от1 до 9')



#Функция проверки выигрыша
def check_win(field):
    #выигрышные поля
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if field[each[0]] == field[each[1]]== field[each[2]]:
            return field[each[0]]
    return False

def main(field):
    counter = 0
    win = False
    while not win:
        draw_board(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1
        if counter >4:
            tmp =check_win(field)
            if tmp:
                print(tmp, 'Вы выиграли')
                win = True
                break
        if counter == 9:
            print( "Ничья")
            break
    draw_board(field)
main(field)
