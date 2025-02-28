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
                    elif neighbors_color != agent_color:  
                        unalike_neighbors += 1

    total_neighbors = alike_neighbors + unalike_neighbors
    return alike_neighbors / total_neighbors if total_neighbors > 0 else 1 


def update_simulation(grid, similar, size):
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
    x1, y1 = x * cell_size, y * cell_size
    x2, y2 = x1 + cell_size, y1 + cell_size
    square = g.Rectangle(g.Point(x1, y1), g.Point(x2, y2))
    square.setFill(color)
    square.setOutline("black")
    square.draw(win)

def draw_grid(size, cell_size, win, grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            color = grid[x][y]  
            draw_square(win, x, y, cell_size, color)

def initialize_grid(size, empty_ratio, red_blue_ratio):
    num_empty = int(size * size * empty_ratio)
    total_agent = size * size - num_empty
    num_red = int(total_agent * red_blue_ratio)
    num_blue = int(total_agent - num_red)
    
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
        draw_grid(size, cell_size, win, grid) 
        previous_grid = [row[:] for row in grid] 
        
        grid = update_simulation(grid, similar, size) 
        iteration += 1
        
        if grid == previous_grid:
            print(f"Simulation stabilized after {iteration} iterations.")
            break 

        time.sleep(0.5) 
        win.update()

    return grid

if __name__ == "__main__":
    size = 20
    win_size = 600
    cell_size = win_size // size
    empty_ratio = 0.1
    red_blue_ratio = 0.5
    similar = 0.3

    win = g.GraphWin("Schelling's Model of Segregation", win_size, win_size, autoflush= False)
    final_grid = run_simulation(size, empty_ratio, red_blue_ratio, similar, win, cell_size)  
    win.getMouse()
    win.close()