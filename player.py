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
        pass
