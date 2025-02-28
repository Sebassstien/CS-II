## Collaborators:
## Spencer Ollmann
## Sebastien LaFontaine

import random
import graphics as g 
import time

def neighbor_similarity(x, y, grid) -> float:
    """Calculates the fraction of similar neighbors for a given agent at (x, y)."""
    
    rows = len(grid)
    columns = len(grid[0])
    alike_neighbors = 0
    unalike_neighbors = 0
    
    agent_color = grid[x][y]  
    if agent_color == "white":  
        return 1 

    for dx in range(-1 if x > 0 else 0, 2 if x < rows - 1 else 1):
        for dy in range(-1 if y > 0 else 0, 2 if y < columns - 1 else 1):
            if dx != 0 or dy != 0: 
                neighbor_x = x + dx
                neighbor_y = y + dy 
                if 0 <= neighbor_x < rows and 0 <= neighbor_y < columns: 
                    neighbors_color = grid[neighbor_x][neighbor_y]
                    if neighbors_color == agent_color:
                        alike_neighbors += 1
                    elif neighbors_color != agent_color and neighbors_color != "white":  
                        unalike_neighbors += 1

    total_neighbors = alike_neighbors + unalike_neighbors
    return alike_neighbors / total_neighbors if total_neighbors > 0 else 1 


def update_simulation(grid, similar):
    """Moves unhappy agents to empty spaces if their neighbor similarity is too low."""

    unhappy_agents = []
    empty_cells = []

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "white":
                empty_cells.append((x, y)) 
            elif grid[x][y] in ["red", "blue"]:
                similarity_ratio = neighbor_similarity(x, y, grid)
                if similarity_ratio < similar: 
                    unhappy_agents.append((x, y))

    if empty_cells and unhappy_agents:  
        random.shuffle(unhappy_agents) 
        random.shuffle(empty_cells)  

        for agent_idx in range(len(unhappy_agents)):
            if not empty_cells: 
                break
            
            agent_x, agent_y = unhappy_agents[agent_idx]
            empty_x, empty_y = empty_cells.pop() 
            
            grid[empty_x][empty_y] = grid[agent_x][agent_y]  
            grid[agent_x][agent_y] = "white" 

    return grid

def draw_square(win, x, y, cell_size, color):
    """Draws a square with side length cell_size at x, y in win"""
    x1, y1 = x * cell_size, y * cell_size
    x2, y2 = x1 + cell_size, y1 + cell_size
    square = g.Rectangle(g.Point(x1, y1), g.Point(x2, y2))
    square.setFill(color)
    square.setOutline("black")
    square.draw(win)

def draw_grid(cell_size, win, grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            color = grid[x][y]  
            draw_square(win, x, y, cell_size, color)

def initialize_grid(size, empty_ratio, red_blue_ratio):
    """Creates a square grid with random colors at each coordinate with size*size cells"""
    num_empty = int(size * size * empty_ratio)
    total_agent = size * size - num_empty
    num_red = int(total_agent * red_blue_ratio)
    
    positions = [(x, y) for x in range(size) for y in range(size)]
    random.shuffle(positions)

    grid = [["white"] * size for i in range(size)] 

    for (x, y) in positions[:num_empty]:
        grid[x][y] = "white"

    for (x, y) in positions[num_empty:num_empty + num_red]:
        grid[x][y] = "red"
   
    for (x, y) in positions[num_empty + num_red:]:
        grid[x][y] = "blue"

    return grid

def run_simulation(size, empty_ratio, red_blue_ratio, similar, win, cell_size):
    """Runs the Schelling model simulation and updates the visualization."""
    
    grid = initialize_grid(size, empty_ratio, red_blue_ratio)
    iteration = 0 

    while True: 
        draw_grid(cell_size, win, grid) 
        previous_grid = [row[:] for row in grid] 
        
        grid = update_simulation(grid, similar) 
        iteration += 1
        
        if grid == previous_grid:
            print(f"Simulation stabilized after {iteration} iterations.")
            break 

        time.sleep(0.5) 
        win.update()

    return grid

if __name__ == "__main__":
    SIZE = 20
    WIN_SIZE = 600
    CELL_SIZE = WIN_SIZE // SIZE
    EMPTY_RATIO = 0.1
    RED_BLUE_RATIO = 0.5
    SIMILAR = 0.3

    win = g.GraphWin("Schelling's Model of Segregation", WIN_SIZE, WIN_SIZE, autoflush= False)
    final_grid = run_simulation(SIZE, EMPTY_RATIO, RED_BLUE_RATIO, SIMILAR, win, CELL_SIZE)  
    win.getMouse()
    win.close()