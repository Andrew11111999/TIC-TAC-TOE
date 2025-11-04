import time

from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        # используем один список для представления доски 3x3
        # каждый элемент - это либо ' ', либо 'X'/'O'
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # current_winner хранит букву победителя, если есть

    def print_board(self):
        # выводим доску построчно в удобочитаемом формате
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 и т.д. Выводим номера ячеек доски, чтобы игроки знали, что куда соответствует
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
        # Если выбранный квадрат пустой, сделайте ход, назначив букву
        # Вернется True, если ход выполнен успешно, иначе False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Проверяем, есть ли 3 одинаковых знака подряд в строке, столбце или диагонали
        # Начинаем со строки, где сделан ход
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # проверить соответствующий столбец
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Проверяем диагонали, только если ход сделан в квадрате с четным индексом (возможные диагональные позиции)
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
    # Запускает игровой цикл, возвращает букву победителя или None при ничьей
    if print_game:
        game.print_board_nums()

    letter = 'X'  # ход начинает игрок с 'X'
    # продолжаем играть, пока есть свободные ячейки
    # победитель определится внутри цикла и прервет игру
    while game.empty_squares():
        # получите ход от соответствующего игрока
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # пытаемся сделать ход на выбранный квадрат
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' делает ход к квадрату {square}')
                game.print_board()
                print('')  # просто пустая строка

            if game.current_winner:
                if print_game:
                    print(letter + ' выиграл!')
                return letter

            # переключаемся на другого игрока
            letter = 'O' if letter == 'X' else 'X'

        # небольшой таймаут для удобства просмотра ходов
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
