class Position:
    def __init__(self, x : int = 0, y : int = 0):
        """Initializes a new Position with given x and y."""
        self.x = x
        self.y = y
    
    def __repr__(self):
        """Returns a representation of the Position."""
        return f"<{self.x:.1f}, {self.y:.1f}>"
    
    def __str__(self):
        """Returns a simplify representation of the Position."""
        return self.__repr__()

    def __eq__(self, other):
        """Check if two Position are equal."""
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        """Adds two Positions."""
        return Position(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Substracts two Positions."""
        return Position(self.x - other.x, self.y - other.y)
            
    def times(self, scalar):
        """Multiplies the Position by a scalar."""
        return Position(self.x * scalar, self.y * scalar)
    
    def distance_to(self, other):
        """Finds the distance between two Positions."""
        v = other-self
        v.x = abs(v.x)
        v.y = abs(v.y)
        if 0 == v.x or 0 == v.y or v.x == v.y:
            return max(v.x,v.y)

class Piece:
    color = None
    def __init__(self, color, position: Position):
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
                self.board[0][col] = Piece('black', Position(0, col))
                self.board[self.rows - 1][col] = Piece('black', Position(self.rows- 1, col))
        for row in range(1, self.rows - 1):
            if row <= 6:
                self.board[row][0] = Piece('white', Position(row, 0))
                self.board[row][self.cols - 1] = Piece('white', Position(row, self.cols - 1))

    def move_pieces(self): #It should take a position to move from a position to move another
        pass
    
    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    

def highlight_space(pos: Position):
    pass #graphics code here
def unhighlight_space(pos: Position):
    pass #graphics code here

class Game:
    board = Board(8,8)
    turn = "black"
    def __init__(self):
        pass
    def is_movable(self,pos: Position) -> bool:
        if not isinstance(self.board.board[pos.y][pos.x], Piece):
            return False
        if self.board.board[pos.y][pos.x].color != self.turn:
            return False
        return True
    
    def valid_moves(self,pos1: Position):
        if not self.is_movable(pos1):
            return
        #return lsit of all spaces piece can move to
        return []
    
    def num_pieces_in_line(self, pos1:Position, pos2:Position):
        pass #determine direction of line then iterate through line counting pieces

    def select_piece(self, pos1: Position):
        if not self.is_movable(pos1):
            return
        for i in self.valid_moves(pos1):
            highlight_space(i)

    def move_piece(self,pos1: Position, pos2: Position):
        if not self.is_movable(pos1):
            return
        if pos2.distance_to(pos1) == self.num_pieces_in_line(pos1,pos2):
            if isinstance(self.board.get_piece(pos2), Piece):
                return
            self.board.move_pieces(pos1,pos2)
        