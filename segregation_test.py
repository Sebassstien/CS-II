from pytest import approx
from segregation import neighbor_similarity
from segregation import initialize_grid
from segregation import update_simulation

def test_neighbor_similarity():
    red_grid=[["red","red","red"],["red","red","red"],["red","red","red"]]
    assert neighbor_similarity(0,0,red_grid) == approx(1)

    white_grid=[["white","white","white"],["white","white","white"],["white","white","white"]]
    assert neighbor_similarity(0,0,white_grid) == approx(1)

    blue_grid=[["blue","blue","blue"],["blue","blue","blue"],["blue","blue","blue"]]
    assert neighbor_similarity(0,0,blue_grid) == approx(1)

    mostly_blue_grid=[["red","blue","blue"],["blue","blue","blue"],["blue","blue","blue"]]
    assert neighbor_similarity(0,0,mostly_blue_grid) == approx(0)

    multicolor_grid=[["blue","red","blue"],["white","red","red"],["white","blue","blue"]]
    assert neighbor_similarity(1,1,multicolor_grid) == approx(2.0/6.0)

def test_grid(grid, size, empty_ratio, red_blue_ratio):
    assert len(grid) == size
    assert len(grid[0]) == size
    empty_cells = 0
    red_cells = 0
    blue_cells = 0
    for i in grid:
        for j in i:
            if j == "white":
                empty_cells +=1
            elif j == "red":
                red_cells +=1
            elif j == "blue":
                blue_cells +=1
            else:
                assert False # invalid grid cell
    assert empty_cells == approx(size*size*empty_ratio)
    assert red_cells == approx((size*size-empty_cells)*red_blue_ratio,abs=1)
    assert blue_cells == approx((size*size-empty_cells-red_cells))

def test_initialize_grid():
    size,empty_ratio,red_blue_ratio = 20,0.1,0.7
    grid = initialize_grid(size,empty_ratio,red_blue_ratio)
    test_grid(grid, size, empty_ratio, red_blue_ratio)

def test_update_simulation():
    size,empty_ratio,red_blue_ratio = 20,0.1,0.7
    grid = initialize_grid(size,empty_ratio,red_blue_ratio)
    for i in range(10):
        similarity = 0.3
        update_simulation(grid, similarity)
        test_grid(grid, size, empty_ratio, red_blue_ratio)
