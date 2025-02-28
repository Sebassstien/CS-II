from pytest import approx
from segregation import neighbor_similarity
from segregation import initialize_grid

def test_neighbor_similarity():
    red_grid=[["red","red","red"],["red","red","red"],["red","red","red"]]
    assert neighbor_similarity(0,0,red_grid) == approx(1)

def test_initialize_grid():
    pass