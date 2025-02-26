import random
import graphics as g 

def get_neighbors(x, y, grid):

    row = len(grid)
    column = len(grid[0])

    neighbors = []

    agent_color = grid[x][y]
    if agent_color == "white":
        return neighbors

    for dx in range (-1 if (x > 0) else 0, 2 if (x < row - 1) else 1):

        for dy in range(-1 if (y >0) else 0 , 2 if (y < column - 1) else 1):
            if (dx != 0 or dy != 0):
                neighbor_row = x + dx
                neighbor_column = y + dy 
                if 0 <= neighbor_row < row and 0 <= neighbor_column < column:
                    neighbors_color = grid[dx][dy]
                    if neighbors_color == agent_color:
                        neighbors.append(grid[x + dx][y + dy])

    return neighbors
    

def update_simulation(grid, similar, size):

    unhappy_agents = []
    empty_cells = []

    for i, (x ,y,cell_type) in enumerate(grid):
        if cell_type == "white":
            empty_cells.append(i)
        elif cell_type in ["red", "blue"]:
            neighbors = get_neighbors(x, y,grid)
            if not neighbors:
                unhappy_agents.append(i)
                continue

    return grid

def draw_square(win, x, y, cell_size, color):

    x1, y1 = x * cell_size, y * cell_size
    x2, y2 = x1 + cell_size, y1 + cell_size
    square = g.Rectangle(g.Point(x1, y1), g.Point(x2, y2))
    square.setFill(color)
    square.setOutline("black")
    square.draw(win)

def draw_grid(size, cell_size, win, grid):

    for (x, y, cell_type) in grid:

        if cell_type == "white":
            color = "white"
        elif cell_type == "red":
            color = "red"
        elif cell_type == "blue":
            color = "blue"

        draw_square(win, x, y, cell_size, color)

def initialize_grid(size, empty_ratio, red_blue_ratio):

    num_empty = int(size * size * empty_ratio)
    total_agent = (size * size - num_empty)
    num_red = int(total_agent * red_blue_ratio)
    num_blue = int(total_agent - num_red)
    
    positions = [(x , y) for x in range(size) for y in range(size)]
    random.shuffle(positions)

    grid = []

    for (x, y) in positions[:num_empty]:
        grid.append((x, y, "white"))

    for (x, y) in positions[num_empty:num_empty + num_red]:
        grid.append((x, y, "red"))
   
    for (x, y) in positions[num_empty + num_red:]:
        grid.append((x, y, "blue"))

    return grid

def run_simulation(size, empty_ratio, red_blue_ratio, similar, win, cell_size):

    desorganized_grid = initialize_grid(size, empty_ratio, red_blue_ratio)
    
    draw_grid(size, cell_size, win, desorganized_grid)

    updated_grid = update_simulation(desorganized_grid, similar, size)
    
    return updated_grid

if __name__ == "__main__":
    size = 20
    win_size = 600
    cell_size = win_size // size
    empty_ratio = 0.1
    red_blue_ratio = 0.5
    similar = 0.3

    win = g.GraphWin("Schelling's Model of Segregation", win_size, win_size)

    final_grid = run_simulation(size, empty_ratio, red_blue_ratio, similar, win, cell_size)  

    win.getMouse()
    win.close()