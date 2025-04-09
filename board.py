from vector import Vector


class Piece:
    color = None
    def __init__(self, color, position):
        self.color = color
        self.position = position
    
    def __str__(self):
        return str(self.color)


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def display_board(self, player_1, player_2):
        for row in self.board:
            for col in row:
                if isinstance(col , Piece):
                    if col.color == 'white':
                        print(player_1, end='')
                    elif col.color == 'black':
                        print(player_2, end='')
                    else:
                        print('#')
                else:
                    print(' ', end='')
            print('')

    def initialize_pieces(self):
        for col in range(1, self.cols - 1):
            if col <= 6:
                self.board[0][col] = Piece('black', Vector(0, col))
                self.board[self.rows - 1][col] = Piece('black', Vector(self.rows- 1, col))
        for row in range(1, self.rows - 1):
            if row <= 6:
                self.board[row][0] = Piece('white', Vector(row, 0))
                self.board[row][self.cols - 1] = Piece('white', Vector(row, self.cols - 1))

    def move_pieces(self): #It should take a position to move from a position to move another
        pass

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True