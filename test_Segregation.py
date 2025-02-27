import random
import graphics as g 

def get_neighbors(x, y, grid):
    """Returns a list of neighboring cells that have the same color as (x, y)."""
    sum = 0
    row = len(grid)  # Total number of grid cells (not a 2D array!)
    neighbors = []

    # Find the agent's color from the (x, y, color) list
    agent_color = None
    for cell in grid:
        if cell[0] == x and cell[1] == y:
            agent_color = cell[2]  # Get the color
            break

    if agent_color is None or agent_color == "white":
        return neighbors  # Return empty list if not found or empty cell

    # Check surrounding neighbors
    for dx in range(-1 if x > 0 else 0, 2 if x < row - 1 else 1):
        for dy in range(-1 if y > 0 else 0, 2 if y < row - 1 else 1):
            if dx != 0 or dy != 0:
                neighbor_row = x + dx
                neighbor_column = y + dy

                # Find neighbor in the grid list
                neighbors_color = None
                for cell in grid:
                    if cell[0] == neighbor_row and cell[1] == neighbor_column:
                        neighbors_color = cell[2]  # Get neighbor color
                        break

                if neighbors_color == agent_color:  # Only add if same color
                    neighbors.append(neighbors_color)

    return neighbors

def update_simulation(grid, similar, size):

    unhappy_agents = []
    empty_cells = []
    
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "white":
                empty_cells.append(grid[x][y])
            elif grid[x][y] in ["red", "blue"]:
                neighbors = get_neighbors(x, y,grid)
            if not neighbors:
                unhappy_agents.append(grid[x][y])
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

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "white":
                color = "white"
            elif grid[x][y] == "red":
                color = "red"
            elif grid[x][y] == "blue":
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
    for i in range(size):
        grid.append([[]] * size) 

    for (x, y) in positions[:num_empty]:
        grid[x][y] = "white"

    for (x, y) in positions[num_empty:num_empty + num_red]:
        grid[x][y] = "red"
   
    for (x, y) in positions[num_empty + num_red:]:
        grid[x][y] = "blue"

    print(grid)
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