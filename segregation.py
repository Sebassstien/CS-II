import random
import graphics as g 

def get_neighbors(x, y, grid):  

    rows = len(grid)
    columns = len(grid[0])

    neighbors = []
    
    agent_color = grid[x][y]
    if agent_color == "white":
        return neighbors

    for dx in range (-1 if (x > 0) else 0, 2 if (x < rows - 1) else 1):  
        for dy in range(-1 if (y >0) else 0 , 2 if (y < columns - 1) else 1):
            if (dx != 0 or dy != 0): 
                neighbor_x = x + dx
                neighbor_y = y + dy 
                if 0 <= neighbor_x < rows and 0 <= neighbor_y < columns: 
                    neighbors_color = grid[neighbor_x][neighbor_y]
                    if neighbors_color == agent_color:
                        neighbors.append(grid[neighbor_x][neighbor_y]) 

    return neighbors 

def neighbor_similarity(x, y, grid) -> float:
    rows = len(grid)
    columns = len(grid[0])
    alike_neighbors = 0;
    unalike_neighbors = 0;
    
    agent_color = grid[x][y] # grid spaces stored as the color at the grid location
    if agent_color == "white": # this should be checked by caller
        return 1

    for dx in range (-1 if (x > 0) else 0, 2 if (x < columns - 1) else 1):  
        for dy in range(-1 if (y >0) else 0 , 2 if (y < rows - 1) else 1):
            if (dx != 0 or dy != 0): # exclude self
                neighbor_x = x + dx
                neighbor_y = y + dy 
                if 0 <= neighbor_x < columns and 0 <= neighbor_y < rows: 
                    neighbors_color = grid[neighbor_x][neighbor_y]
                    if neighbors_color == agent_color:
                        alike_neighbors += 1
                    elif "white" != neighbors_color:
                        unalike_neighbors += 1

    return alike_neighbors/(alike_neighbors+unalike_neighbors)
    

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
    num_blue = int(total_agent - num_red) # unused
    
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