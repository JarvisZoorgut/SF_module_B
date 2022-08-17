#B_exam_commit

def start():
    print('')
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

def field(f):
    print('  0 1 2')
    for i in range(len(f)):
        print(str(i),*f[i])

def move(f):
    global x, y
    while True:
        move = input('Введите координаты : ').split()
        if len(move) != 2:
            print('Введите две координаты')
            continue
        if not(move[0].isdigit() and move[1].isdigit()):
            print('Введите числа')
            continue
        x,y = map(int, move)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из поля')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x, y

def game_proceed():
    global count, player
    while True:
        field(f)
        print('')
        if count == 9:
            print('!!! НИЧЬЯ !!!')
            print('')
            next_game = input('Хотите сыграть заново (y/n)? ')
            print('')
            if next_game == 'y':
                new_game()
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
        if win(f, player):
            print('')
            print('Игра окончена!')
            print(f'Победил игрок', player)
            field(f)
            print('')
            next_game = input('Хотите сыграть заново (y/n)? ')
            print('')
            if next_game == 'y':
                new_game()
            else:
                print('До скорой встречи ;)')
            break
        count += 1

def move_bot(f):
    from random import randint
    global x, y
    while True:
        x = randint(0, 2)
        y = randint(0, 2)
        move = [x, y]
        if len(move) != 2:
            continue
        x,y = map(int, move)
        if f[x][y] != '-':
            continue
        break
    return x, y

def game_proceed_bot():
    global count, player
    while True:
        field(f)
        print('')
        if count == 9:
            print('!!! НИЧЬЯ !!!')
            print('')
            next_game = input('Хотите сыграть заново (y/n)? ')
            print('')
            if next_game == 'y':
                new_game()
            else:
                print('До скорой встречи ;)')
            break
        if count % 2 == 0:
            player = 'X'
            print('Ход человека - Х')
            x, y = move(f)
        else:
            player = '0'
            print('Ход компьютера - 0')
            x, y = move_bot(f)

        f[x][y] = player
        if win(f, player):
            print('')
            print('Игра окончена!')
            if player == 'X':
                print('Победил человек!')
                print('Нео, ты свободен!')
            else:
                print('Победил компьютер!')
                print('Ты навсегда останешься в матрице, Нео!')
            field(f)
            print('')
            next_game = input('Хотите сыграть заново (y/n)? ')
            print('')
            if next_game == 'y':
                new_game()
            else:
                print('До скорой встречи ;)')
            break
        count += 1

def st_game():
    global count, f
    count = 0
    f = [['-'] * 3 for _ in range(3)]
    if set_player == 'y':
        game_proceed_bot()
    else:
        game_proceed()

def win(f, player):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbol = []
        for c in cord:
            symbol.append(f[c[0]][c[1]])
        if symbol == [player, player, player]:
            return True
    return False

def new_game():
    global set_player
    set_player = input('Вы хотите сыграть с компьютером (y/n)? ')
    st_game()

start()
new_game()