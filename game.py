import time


from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # мы будем использовать единый список для повторения доски размером 3х3
        self.current_winner = None  # следите за победителем!

    def print_board(self):
        # это просто получение строк
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 и т.д. (указывает нам, какой номер какому ящику соответствует)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Если ход правильный, то сделайте этот ход (назначьте квадрат букве).
        # Затем верните значение true. Если значение неверно, верните значение false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Выигрывает, если выпадет 3 раза подряд в любом месте.. мы должны проверить все это!
        # Сначала давайте проверим строку
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # проверить столбец
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # проверить диагональ
        # Но только в том случае, если в квадрате четное число (0, 2, 4, 6, 8)
        # это единственные ходы, которые возможны для выигрыша диагонали
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # диагональ слева направо
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # диагональ справа налево
            if all([spot == letter for spot in diagonal2]):
                return True

        # если все это не сработает
        return False


def play(game, x_player, o_player, print_game=True):
    # возвращает победителя игры (букву)! или нет - в случае ничьей
    if print_game:
        game.print_board_nums()

    letter = 'X'  # начальная буква
    # повторяйте, пока в игре все еще есть пустые квадраты
    # (нам не нужно беспокоиться о победителе, потому что мы просто вернем его
    # который разрывает цикл)
    while game.empty_squares():
        # получите ход от соответствующего игрока
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # давайте определим функцию для совершения движения!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' делает ход к квадрату {square}')
                game.print_board()
                print('')  # просто пустая строка

            if game.current_winner:
                if print_game:
                    print(letter + 'выиграл!')
                return letter

            # После того как мы сделали свой ход, нам нужно чередовать буквы
            letter = 'O' if letter == 'X' else 'X'  # переключает проигрыватель

        # небольшой перерыв, чтобы было немного легче читать
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
