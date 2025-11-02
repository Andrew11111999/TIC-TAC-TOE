import math
import random


class Player:
    def __init__(self, letter):
        # игрок использует букву 'X' или 'O' для обозначения своего хода
        self.letter = letter

    # мы хотим, чтобы все игроки определяли свой следующий ход по ходу игры
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # выберите случайный доступный ход из доступных на доске
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'очередь. Входной ход (0-8):')
            # проверяем, что ввод пользователя является числом и доступным ходом на доске
            # если нет, просим ввести снова
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # если они окажутся успешными, то ура!
            except ValueError:
                print('Недопустимый квадрат. Пробовать снова.')

        return val
