##  Collaborators:
##  Sebastien LaFontaine
##  Spencer Ollmann

import graphics as g

filename = "maze.txt"

def draw_line(p1, p2, win):
    line = g.Line(p1, p2)
    line.setWidth(3)       
    line.setOutline("black") 
    line.draw(win)
    return win

# Open the maze file and read its contents
with open(filename, "r") as file:
    file_contents = file.readlines() 

    maze_height = len(file_contents) 
    maze_width = max(len(line) for line in file_contents)

    win = g.GraphWin("Maze", 400, 400)
    win.setCoords(-1.5, maze_height - 0.5, maze_width - 0.5, -1.5)

# Loop through each column and row in the maze to find horizontal walls and draw horizontal lines
for y in range(maze_height):
    line = file_contents[y]
    start_point = None 
    for x in range(len(line)): 
        if line[x] == '#':  
            if start_point is None:
                start_point = g.Point(x, y)  
            end_point = g.Point(x, y)
        else:
            if start_point is not None:
                draw_line(start_point, end_point, win)  
                start_point = None

    if start_point is not None:
        draw_line(start_point, end_point, win)

# Loop through each row and column in the maze to find vertical walls and draw vertical lines
for x in range(maze_width):
    start_point = None 
    for y in range(maze_height):
        line = file_contents[y][x] if x < len(file_contents[y]) else ' '
        if line == '#':
            if start_point is None:
                start_point = g.Point(x, y)  
            end_point = g.Point(x, y) 
        else:
            if start_point is not None:
                draw_line(start_point, end_point, win)  
                start_point = None  

    if start_point is not None:
        draw_line(start_point, end_point, win)

win.getMouse()
win.close()