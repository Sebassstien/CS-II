from board import Piece
from board import Position
from board import Board
from board import Game
BOARD_HEIGHT = 8
BOARD_WIDTH = 8

def test_position():
    p1 = Position(1,1)
    p2= Position(3,1)
    assert p1.distance_to(p2) == 2
    p1.y=2
    assert p1.distance_to(p2) == None
    p1 = Position()
    assert p1.x == 0
    assert p1.y == 0


def test_piece():
    p = Piece()
    assert p.color == None
    assert p.position == None

def test_board_init():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    assert len(b.board) == BOARD_HEIGHT
    for i in b.board:
        assert len(i) == BOARD_WIDTH
    
def test_board_initialize_pieces():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.initialize_pieces()
    for i in range(1, len(b.board[0])-1):
        p = b.board[0][i]
        assert isinstance(p, Piece)
        if isinstance(p, Piece):
            assert p.color == "white"