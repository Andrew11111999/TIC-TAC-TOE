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


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # случайным образом выберите один из них
        else:
            # вычислите квадрат на основе минимаксного алгоритма
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # себя!!
        other_player = 'O' if player == 'X' else 'X'  # Другой игрок... так что какая бы буква НИ была НЕ u

        # во-первых, мы хотим проверить, был ли предыдущий ход выигрышным
        # это наш базовый вариант
        if state.current_winner == other_player:
            # мы должны вернуть позицию И забить, потому что нам нужно следить за счетом
            # чтобы сработал minimax
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares() + 1)
                    }

        elif not state.empty_squares():  # никаких пустых квадратов
            return {'position': None, 'score': 0}

        # Если ход выполняет max_player, пытаемся выбрать ход с максимальной оценкой
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # мы пытаемся миксимизировать оценку для max_player
        else:
            best = {'position': None, 'score': math.inf}  # следует выбрать минимальный балл

        for possible_move in state.available_moves():
            # шаг 1: сделать ход
            state.make_move(possible_move, player)
            # шаг 2: Рекурсивно оценить ход противника
            sim_score = self.minimax(state, other_player)  # теперь мы меняем игроков

            # шаг 3: Отменить ход (откатить изменения)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # в противном случае это будет испорчено из-за рекурсии

            # шаг 4: Обновить лучший результат в зависимости от игрока
            if player == max_player:  # мы пытаемся максимально увеличить max_player
                if sim_score['score'] > best['score']:
                    best = sim_score  # заменить лучшее
            else:  # но сведите к минимуму другого игрока
                if sim_score['score'] < best['score']:
                    best = sim_score  # заменить лучшее

        return best
