import math
import random


class Player:
    def __init__(self, letter):
        # буква "х" или "о"
        self.letter = letter

    # мы хотим, чтобы все игроки определяли свой следующий ход по ходу игры
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # получите случайное действительное место для нашего следующего хода
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
            # мы собираемся проверить, что это правильное значение, попытавшись привести
            # это целое число, а если это не так, то мы говорим, что оно недействительно
            # если это место недоступно на доске, мы также объявляем его недействительным
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # если они окажутся успешными, то ура!
            except ValueError:
                print('Недопустимый квадрат. Пробовать снова.')

        return val
