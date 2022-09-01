from random import randint

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за переделы доски"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size
        self.hid = hid
        self.count = 0
        self.field = [["O"]*size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        res = "   "
        for i, col in enumerate(self.field):
            if i < 9:
                res += f"    {i+1} "
            else:
                res += f"    {i+1}"
        for i, row in enumerate(self.field):
            if i < 9:
                res += f"\n{i+1}   |  " + "  |  ".join(row) + "  |"
            else:
                res += f"\n{i+1}  |  " + "  |  ".join(row) + "  |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def countor(self, ship, verb = False):
        near =[
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1,-1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.countor(ship)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.shooten(d):
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.countor(ship, verb = True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "T"
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        #в общем так и не разобрался, как сюда подключить логику изменения поля выстрела AI в зависимости от размера поля. Не хватило времени разобраться....
        d = Dot(randint(0, 9), randint(0, 9))
        print(f"Ход компьютера: {d.x+1} {d.y+1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print("Введите две координаты! ")
                continue

            x, y = cords

            if not(x.isdigit()) or not (y.isdigit()):
                print("Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot (x-1, y-1)

class Game():
    def greet(self):
        print("-------------------------")
        print("|          ИГРА         |")
        print("|       МОРСКОЙ БОЙ     |")
        print("-------------------------")
        print("|  Для выстрела ввести: |")
        print("|   x - номер строки    |")
        print("|   y - номер столбца   |")
        print("_________________________")

    def __init__(self, size = 4):
        Game.greet(self)
        self.size = int(input('Введите размер поля (от 4 до 10): '))
        pl = self.random_board()
        co = self.random_board()
        co.hid = False  #открыть, скрыть корабли противника
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        board = Board(size = self.size)
#здесь тоже проблемы с логикой, не понимаю, как развернуть обратно цикл при неверном выборе, пробовал while, не вышло...
        if self.size == 4:
            lens = [2, 2, 1, 1]
        elif self.size == 5:
            lens = [2, 2, 1, 1, 1]
        elif self.size == 6:
            lens = [3, 2, 2, 1, 1, 1, 1]
        elif self.size == 7:
            lens = [3, 2, 2, 2, 1, 1, 1, 1, 1]
        elif self.size == 8:
            lens = [4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1]
        elif self.size == 9:
            lens = [5, 4, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        elif self.size == 10:
            lens = [6, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        else:
            print("Введите верный размер поля!")
            Game.start(self)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def print_boards(self):
        print("-" * 25)
        print("Поле пользователя: ")
        print(self.us.board)
        print("-" * 25)
        print("Поле компьютера: ")
        print(self.ai.board)
        print("-" * 25)

    def loop(self):
        num = 0
        while True:
            self.print_boards()
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()

            if repeat:
                num -=1

            if self.ai.board.defeat():
                self.print_boards()
                print("-"*25)
                print("Пользователь выиграл!")
                break

            if self.us.board.defeat():
                self.print_boards()
                print("-"*25)
                print("Компьютер выиграл!")
                break
            num +=1

    def start(self):
        self.loop()


g = Game()
g.start()