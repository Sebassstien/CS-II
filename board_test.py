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
    p = Piece('','')
    assert p.color == ''
    assert p.position == ''

def test_board_init():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    assert len(b.board) == BOARD_HEIGHT
    for i in b.board:
        assert len(i) == BOARD_WIDTH
    
def test_initialize_pieces():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.initialize_pieces()
    for i in range(1, len(b.board[0])-1):
        p = b.board[0][i]
        assert isinstance(p, Piece)
        if isinstance(p, Piece):
            assert p.color == "black"
    for i in range(1, len(b.board[0])-1):
        p = b.board[7][i]
        assert isinstance(p, Piece)
        if isinstance(p, Piece):
            assert p.color == "black"
    for i in range(1, len(b.board)-1):
        p = b.board[i][0]
        assert isinstance(p, Piece)
        if isinstance(p, Piece):
            assert p.color == "white"
    for i in range(1, len(b.board)-1):
        p = b.board[i][7]
        assert isinstance(p, Piece)
        if isinstance(p, Piece):
            assert p.color == "white"

def test_get_piece():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.board[0][0] = Piece('white',Position(0,0))
    b.board[1][1] = Piece('black',Position(1,1))
    b.board[3][3] = Piece('black', Position(3,3))
    b.board[0][1] = Piece('white', Position(0,1))
    assert isinstance(b.get_piece(Position(0,0)),Piece)
    assert not isinstance(b.get_piece(Position(0,1)), Piece)
    assert isinstance(b.get_piece(Position(1,0)), Piece)

def test_num_pieces_in_line():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.board[0][0] = Piece('white',Position(0,0))
    b.board[1][1] = Piece('black',Position(1,1))
    b.board[3][3] = Piece('black', Position(3,3))
    b.board[0][1] = Piece('white', Position(0,1))
    assert b.num_pieces_in_line(Position(1,1), Position(0,0)) == 3
    assert b.num_pieces_in_line(Position(1,1), Position(1,0)) == 2
    assert b.num_pieces_in_line(Position(3,3), Position(3,0)) == 1
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.initialize_pieces()
    assert b.num_pieces_in_line(Position(0,3), Position(0,7)) == 6
    assert b.num_pieces_in_line(Position(0,3), Position(7,3)) == 2
    assert b.num_pieces_in_line(Position(0,3), Position(1,4)) == 2
    assert b.num_pieces_in_line(Position(1,7), Position(7,7)) == 6
    assert b.num_pieces_in_line(Position(1,0), Position(7,0)) == 6
    b.move_pieces(Position(2,0),Position(2,2))
    b.move_pieces(Position(7,2),Position(5,2))
    assert b.num_pieces_in_line(Position(2,7), Position(0,5)) == 2
    assert b.num_pieces_in_line(Position(7,2), Position(5,0)) == 1
    assert b.num_pieces_in_line(Position(7,2), Position(5,0)) == 1
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.initialize_pieces()
    b.move_pieces(Position(7,2),Position(4,2))
    b.board[0][4] = None
    assert b.num_pieces_in_line(Position(5,0), Position(4,1)) == 2


def test_move_pieces():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.board[0][0] = Piece('white',Position(0,0))
    b.board[1][1] = Piece('black',Position(1,1))
    b.board[3][3] = Piece('black', Position(3,3))
    b.board[0][1] = Piece('white', Position(0,1))
    b.move_pieces(Position(1,0), Position(0,0))
    assert b.move_pieces(Position(-7,-7),Position(0,0)) == None
    assert b.move_pieces(Position(7,7),Position(0,0)) == None
    assert b.get_piece(Position(0,0)).color == "white"

def test_available_moves():
    b = Board(BOARD_HEIGHT,BOARD_WIDTH)
    b.board[0][0] = Piece('white',Position(0,0))
    b.board[1][1] = Piece('black',Position(1,1))
    b.board[3][3] = Piece('black', Position(3,3))
    b.board[0][1] = Piece('white', Position(0,1))
    # for i in b.board:
    #     print(i)
    assert b.available_moves(Position(0,0)) == [Position(0,1),Position(2,0)]
    assert b.available_moves(Position(0,1)) == []
    assert b.available_moves(Position(1,0)) == [Position(3,0),Position(2,1),Position(0,1)]

def test_is_movable():
    g = Game(BOARD_HEIGHT,BOARD_WIDTH)
    assert not g.is_movable(Position(4,4))
    assert g.is_movable(Position(1,0))
    assert not g.is_movable(Position(0,1))

def test_move_piece():
    g = Game(BOARD_HEIGHT,BOARD_WIDTH)
    assert g.move_piece(Position(0,0),Position(0,0)) == None
    assert g.move_piece(Position(0,0),Position(1,1)) == None
    assert g.move_piece(Position(1,0),Position(0,0)) == None
    assert g.move_piece(Position(1,0),Position(1,2)) == True
    assert g.move_piece(Position(2,0),Position(2,-2)) == None
    assert g.move_piece(Position(0,1),Position(2,1)) == True
    g.board.board[3][6] = Piece("white",Position(6,3))
    assert g.move_piece(Position(6,0),Position(6,3)) == True

def test_check_winner():
    g = Game(BOARD_HEIGHT, BOARD_WIDTH)
    g.board = Board(BOARD_HEIGHT,BOARD_WIDTH) 
    b = g.board
    b.board[0][0] = Piece('white',Position(1,1))
    b.board[1][1] = Piece('black',Position(0,0))
    b.board[3][3] = Piece('black', Position(3,3))
    b.board[0][1] = Piece('white', Position(0,1))
    assert g.check_winner() == "White wins"
    assert g.check_winner() != "Black wins"
    assert g.check_winner() != "Tie"

    g.board = Board(BOARD_HEIGHT,BOARD_WIDTH) 
    b = g.board
    b.board[0][0] = Piece('black',Position(1,1))
    b.board[1][1] = Piece('white',Position(0,0))
    b.board[3][3] = Piece('white', Position(3,3))
    b.board[0][1] = Piece('black', Position(0,1))
    assert g.check_winner() == "Black wins"
    assert g.check_winner() != "White wins"
    assert g.check_winner() != "Tie"

    g.board = Board(BOARD_HEIGHT,BOARD_WIDTH) 
    b = g.board
    b.board[0][0] = Piece('white',Position(1,1))
    b.board[1][1] = Piece('black',Position(0,0))
    assert g.check_winner() == "Tie"
    assert g.check_winner() != "White wins"
    assert g.check_winner() != "Black wins"
