from board import Piece
from board import Position
from board import Board
from board import Game

def test_position():
    p1 = Position(1,1)
    p2= Position(3,1)
    assert p1.distance_to(p2) == 2
    p1.y=2
    assert p1.distance_to(p2) == None
    p1 = Position()
    assert p1.x == 0
    assert p1.y == 0
    

def 