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
        v = other - self
        v.x = abs(v.x)
        v.y = abs(v.y)
        if 0 == v.x or 0 == v.y or v.x == v.y:
            return max(v.x, v.y)
        return (v.x**2 + v.y**2)**0.5

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
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

    def display_board(self, player_1, player_2):
        for row in self.board:
            for col in row:
                if isinstance(col , Piece):
                    if col.color == 'white':
                        print(player_1, end=' ')
                    elif col.color == 'black':
                        print(player_2, end=' ')
                    else:
                        print('#')
                else:
                    print(' ', end=' ')
            print()

    def initialize_pieces(self):
        for col in range(1, self.cols - 1):
            if col <= 6:
                self.board[0][col] = Piece('black', Position(0, col))
                self.board[self.rows - 1][col] = Piece('black', Position(self.rows- 1, col))
        for row in range(1, self.rows - 1):
            if row <= 6:
                self.board[row][0] = Piece('white', Position(row, 0))
                self.board[row][self.cols - 1] = Piece('white', Position(row, self.cols - 1))

    def move_pieces(self, initial_position: Position, selected_position: Position): #It should take a position to move from a position to move another
        piece = self.get_piece(initial_position)
        if piece is None:
            return
        
        self.board[initial_position.y][initial_position.x] = None
        self.board[selected_position.y][selected_position.x] = piece
        piece.position =  selected_position
  
    
    def available_moves(self, position: Position):
        piece = self.get_piece(position)
        if piece is None:
            return []
        
        moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            check_pos = Position(position.x + dx, position.y + dy)
            distance = self.num_pieces_in_line(position, check_pos)
            if distance == 0:
                continue

            new_x = position.x + dx * distance
            new_y = position.y + dy * distance
            new_pos = Position(new_x, new_y)

            if not (0 <= new_x < self.cols and 0 <= new_y < self.rows):
                continue

            target_piece = self.get_piece(new_pos)
            if target_piece is None or target_piece.color != piece.color:
                moves.append(new_pos)

        return moves
        
    def get_piece(self, position: Position):
        return self.board[position.y][position.x]

    def num_pieces_in_line(self, position_1: Position, position_2: Position):
        dx = position_2.x - position_1.x
        dy = position_2.y - position_1.y

        if dx == 0 and dy == 0:
            return 0
            
        direction_x = 0 if dx == 0 else 1 if dx > 0 else -1
        direction_y = 0 if dy == 0 else 1 if dy > 0 else -1

        count = 0
        current_x = position_1.x + direction_x
        current_y = position_1.y + direction_y

        while 0 <= current_x < self.cols and 0 <= current_y < self.rows:
            if self.get_piece(Position(current_x, current_y)) is not None:
                count += 1
            if current_x == position_2.x and current_y == position_2.y:
                break
            current_x += direction_x
            current_y += direction_y
        return count
    
    def are_connected(self, color: str):
        pass #DFS and check if Pieces are equal
    
def highlight_space(pos: Position):
    pass #graphics code here
def unhighlight_space(pos: Position):
    pass #graphics code here

class Game:
    board = Board(8,8)
    turn = "black"
    def __init__(self):
        self.select_pieces = None
    def is_movable(self,pos: Position) -> bool:
        if not isinstance(self.board.board[pos.y][pos.x], Piece):
            return False
        if self.board.board[pos.y][pos.x].color != self.turn:
            return False
        return True
    
    def valid_moves(self,position_1: Position):
        if not self.is_movable(position_1):
            return
        return []
    
    def move_piece(self, position_1: Position, position_2: Position):
        if not self.is_movable(position_1):
            return
        if position_2 in self.valid_moves(position_1):
            self.board.move_pieces(position_1, position_2)
            self.turn = "white" if self.turn == "black" else "black"
            self.selected_piece = None
            for move in self.valid_moves(position_2):
                unhighlight_space(move)
        else:
            print("Invalid Move")


    def select_pieces(self, position: Position):
        if self.selected_piece is not None:
            for move in self.valid_moves(self.selected_piece):
                unhighlight_space(move)
        if not self.is_movable(position):
            self.selected_piece = None
            return
        self.selected_piece = position
        for move in self.valid_moves(position):
            highlight_space(move)

    def check_winner(self):
        pass