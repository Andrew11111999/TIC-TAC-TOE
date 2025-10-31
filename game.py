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
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'x'  # начальная буква
    # повторяйте, пока в игре все еще есть пустые квадраты
    # (нам не нужно беспокоиться о победителе, потому что мы просто вернем его
    # который разрывает цикл)
    while game.empty_squares():
        # получите ход от соответствующего игрока
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # давайте определим функцию для совершения движения!
