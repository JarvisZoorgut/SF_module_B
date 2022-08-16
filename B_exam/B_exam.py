#B_exam_commit

def start():
    print('00000000000000')
    print('Х    ИГРА    Х')
    print('Х  КРЕСТИКИ  Х')
    print('Х   НОЛИКИ   Х')
    print('00000000000000')
    print('')
    print('ПРАВИЛА ИГРЫ:')
    print('1. Ход выполнятся путем задания двух координат игрового поля через пробел')
    print('   первая координата - строка, вторая - столбец.')
    print('2. Побеждает - победитель!')
    print('')
    print('!!! В БОЙ !!!')
    print('')

def field(f):
    print('  0 1 2')
    for i in range(len(f)):
        print(str(i),*f[i])

def move(f):
    while True:
        move = input('Введите координаты : ').split()
        if len(move) != 2:
            print('Введите две координаты')
            continue
        if not(move[0].isdigit() and move[1].isdigit()):
            print('Введите числа')
            continue
        x,y = map(int,move)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из поля')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x,y

def game_proceed():
    global count
    while True:
        field(f)
        print('')
        if count == 2:
            print('!!! НИЧЬЯ !!!')
            print('')
            next_game = input('Хотите сыграть заново (y/n)?')
            print('')
            if next_game == 'y':
                st_game()
            else:
                print('До скорой встречи ;)')
            break
        if count % 2 == 0:
            player = 'X'
            print('Ходит  - Х')
        else:
            player = '0'
            print('Ходит  - 0')
        x, y = move(f)
        f[x][y] = player
        count += 1

def st_game():
    global count, f
    count = 0
    f = [['-'] * 3 for _ in range(3)]
    start()
    game_proceed()

st_game()


