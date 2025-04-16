from graphics import *
from board import Game, Position, Board, Piece

# Graphics part
win = GraphWin("Line of Action", 600, 600)
win.setBackground("white")

SQUARE_SIZE = 60
BOARD_SIZE = 8

game = Game(BOARD_SIZE, BOARD_SIZE)
board = game.board 

# Keep track of highlighted squares
highlighted_squares = []

# Draw the grid and pieces
def draw_board():
    global highlighted_squares
    for square in highlighted_squares:
        square.undraw()
    highlighted_squares = []

    for row in range(board.rows):
        for col in range(board.cols):
            # Draw the square
            rect = Rectangle(Point(col * SQUARE_SIZE, row * SQUARE_SIZE), Point((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE))
            rect.setFill(color_rgb(255, 204, 229) if (row + col) % 2 == 0 else color_rgb(153, 204, 255))
            rect.draw(win)

            # Draw the piece 
            piece = board.get_piece(Position(col, row))
            if piece:
                center = Point(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                circle = Circle(center, SQUARE_SIZE // 3)
                if piece.color == "black":
                    circle.setFill("black")
                elif piece.color == "white":
                    circle.setFill("white")
                circle.draw(win)

def get_click_position(click_point):
    x = int(click_point.getX() // SQUARE_SIZE)
    y = int(click_point.getY() // SQUARE_SIZE)
    return Position(x, y)

def highlight_moves(available_moves):
    global highlighted_squares
    for move in available_moves:
        p1 = Point(move.x * SQUARE_SIZE, move.y * SQUARE_SIZE)
        p2 = Point((move.x + 1) * SQUARE_SIZE, (move.y + 1) * SQUARE_SIZE)
        square = Rectangle(p1, p2)
        square.setOutline("green")
        square.setWidth(3)
        square.draw(win)
        highlighted_squares.append(square)

# Main Game Loop
def start_game_graphics():
    selected_piece_pos = None
    draw_board()

    while True:
        click_point = win.getMouse()  
        click_pos = get_click_position(click_point)

        # If no piece is selected, try to select a piece
        if selected_piece_pos is None:
            if game.is_movable(click_pos):
                selected_piece_pos = click_pos
                available_moves = board.available_moves(click_pos)
                highlight_moves(available_moves)
            else:
                print("Invalid piece. Select a piece of your color.")
        else:
            # Move the piece
            if click_pos in board.available_moves(selected_piece_pos):
                game.move_piece(selected_piece_pos, click_pos)
                selected_piece_pos = None  
                draw_board()  
            else:
                print("Invalid move. Try again.")
                selected_piece_pos = None  
                draw_board() 

        # Check for a winner or a tie
        winner = game.check_winner()
        if winner:
            print(winner)
            message = Text(Point(win.getWidth() / 2, win.getHeight() - 20), f"{winner}. Click to close.")
            message.setSize(16)
            message.draw(win)
            win.getMouse() 
            break 

    win.close()  

start_game_graphics()