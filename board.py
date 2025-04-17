from graphics import *

class Position:
    """Represents a position on the board."""
    def __init__(self, x : int = 0, y : int = 0):
        """Initializes a new Position with given x and y."""
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def times(self, scalar):
        return Position(self.x * scalar, self.y * scalar)

    def distance_to(self, other):
        """Finds the distance between two Positions."""
        v = other - self
        v.x = abs(v.x)
        v.y = abs(v.y)
        if 0 == v.x or 0 == v.y or v.x == v.y:
            return max(v.x, v.y)
        return None #(v.x**2 + v.y**2)**0.5

class Piece:
    """Represents a game piece on the board."""
    def __init__(self, color: str, position: Position):
        self.color = color.lower()
        self.position = position

    def __str__(self):
        return self.color

    def __repr__(self):
        return f"Piece(color='{self.color}', position={self.position})"


class Board:
    """Represents the game board."""
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

    def initialize_pieces(self):
        for col in range(1, self.cols - 1):
            self.board[0][col] = Piece('black', Position(col, 0))
            self.board[self.rows - 1][col] = Piece('black', Position(col, self.rows - 1))
        for row in range(1, self.rows - 1):
            self.board[row][0] = Piece('white', Position(0, row))
            self.board[row][self.cols - 1] = Piece('white', Position(self.cols - 1, row))

    def in_bounds(self, position: Position):
        """Checks for the board limits."""
        return (position.x > self.rows or position.x < 0 or position.y > self.cols or position.y < 0)

    def move_pieces(self, initial_position: Position, selected_position: Position):
        """Moves a piece from initial position to a selected position."""
        piece = self.get_piece(initial_position)
        if piece is None:
            return
        if not (0 <= selected_position.x < self.cols and 0 <= selected_position.y < self.rows):
            return
        self.board[initial_position.y][initial_position.x] = None
        self.board[selected_position.y][selected_position.x] = piece
        piece.position = selected_position

    def available_moves(self, position: Position):
        """Calculates the available moves for a piece at given position."""
        piece = self.get_piece(position)
        if piece is None:
            return []
        moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            check_position = Position(position.x + dx, position.y + dy)
            if self.in_bounds(check_position):
                continue
            distance = self.num_pieces_in_line(position, check_position)
            if distance == 0:
                continue
                 
            new_x = position.x + dx * distance
            new_y = position.y + dy * distance
            new_pos = Position(new_x, new_y)
            if not (0 <= new_x < self.cols and 0 <= new_y < self.rows):
                continue

            blocked = False
            for step in range(1, distance):
                intermediate_x = position.x + dx * step
                intermediate_y = position.y + dy * step
                intermediate_pos = Position(intermediate_x, intermediate_y)
                intermediate_piece = self.get_piece(intermediate_pos)
                if intermediate_piece and intermediate_piece.color != piece.color:
                    blocked = True
                    break
            if blocked:
                continue
            
            target_piece = self.get_piece(new_pos)
            if target_piece is None or target_piece.color != piece.color:
                moves.append(new_pos)
        return moves

    def get_piece(self, position: Position):
        """Retrieves the piece at a given position on the board."""
        if 0 <= position.y < self.rows and 0 <= position.x < self.cols:
            return self.board[position.y][position.x]
        return None

    def num_pieces_in_line(self, position_1: Position, position_2: Position):
        """Count the number of pieces on a line following the direction."""
        dx = (position_2.x - position_1.x != 0)
        dy = (position_2.y - position_1.y != 0)
        if dx == 0 and dy == 0:
            return 0
        count = 0
        x, y = position_1.x, position_1.y
        if dx and not dy:
            x = 0
            while x < self.cols:
                if self.get_piece(Position(x, y)) is not None:
                    count += 1
                x += dx
        if dy and not dx:
            y = 0
            while y < self.rows:
                if self.get_piece(Position(x, y)) is not None:
                    count += 1
                y += dy
        if dy and dx:
            dir_x = 1
            dir_y = 1
            if position_2.x - position_1.x < 0:
                dir_x = -1
            if position_2.y - position_1.y < 0:
                dir_y = -1
            while 0 < x < self.cols-1 and 0 < y < self.rows-1:
                x -= dir_x
                y -= dir_y
            while 0 <= x < self.cols and 0 <= y < self.rows:
                if self.get_piece(Position(x, y)) is not None:
                    count += 1
                x += dir_x
                y += dir_y
        return count

    def are_connected(self, color: str) -> bool:
        """Check if all the pieces of the color are connected."""
        color = color.lower()
        visited = set()
        positions = [
            Position(x, y)
            for y in range(self.rows)
            for x in range(self.cols)
            if isinstance(self.board[y][x], Piece) and self.board[y][x].color == color
        ]
        if not positions:
            return True

        def dfs(position):
            stack = [position]
            while stack:
                current = stack.pop()
                if (current.x, current.y) in visited:
                    continue
                visited.add((current.x, current.y))
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                              (0, -1), (0, 1),
                              (1, -1), (1, 0), (1, 1)]:
                    nx, ny = current.x + dx, current.y + dy
                    if 0 <= nx < self.cols and 0 <= ny < self.rows:
                        neighbor = self.board[ny][nx]
                        if isinstance(neighbor, Piece) and neighbor.color == color and (nx, ny) not in visited:
                            stack.append(Position(nx, ny))

        dfs(positions[0])
        return len(visited) == len(positions)

class Game:
    """Keeps of turns and the board movements."""
    def __init__(self, rows: int, cols: int):
        self.board = Board(rows, cols)
        self.turn = "black"
        self.selected_piece = None
        self.board.initialize_pieces()

    def is_movable(self, pos: Position) -> bool:
        """Check if the piece is movable."""
        piece = self.board.get_piece(pos)
        return isinstance(piece, Piece) and piece.color == self.turn

    def move_piece(self, position_1: Position, position_2: Position):
        """Move the piece to the desired position."""
        if not self.is_movable(position_1):
            print("Invalid selection. Choose a piece of your color.")
            return
        if position_2 in self.board.available_moves(position_1):
            self.board.move_pieces(position_1, position_2)
            self.turn = "white" if self.turn == "black" else "black"
            self.selected_piece = None
            print(f"Moved piece to {position_2}")
        else:
            print("Invalid Move")

    def check_winner(self):
        """Checks the winner after every round."""
        black_connected = self.board.are_connected("black")
        white_connected = self.board.are_connected("white")
        if black_connected and white_connected:
            return "Tie"
        elif black_connected:
            return "Black wins"
        elif white_connected:
            return "White wins"
        return None