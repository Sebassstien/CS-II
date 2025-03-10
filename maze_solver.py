# Collaborators:
# Sebastien LaFontaine
# Spencer Ollmann

filename = "maze.txt"


def find_path(maze : list[list[str]], position : tuple[int, int]) -> bool:
    if len(maze)-1 == position[1]:
        maze[position[0]][position[1]-1] = 'O'
        return True
    
    if maze[position[0]+1][position[1]] == ' ':
        maze[position[0]+1] = maze[position[0]+1][0:position[1]]+maze[position[0]+1][position[1]:] if position[1] > 0 else maze[position[0]+1][position[1]:]
        if not find_path(maze, [position[0]+1,position[1]]):
            maze[position[0]+1][position[1]] = ' '
            return False
    if maze[position[0]-1][position[1]] == ' ':
        maze[position[0]-1][position[1]] = 'X'        
        if not find_path(maze, [position[0]-1,position[1]]):
            maze[position[0]-1][position[1]] = ' '
            return False
    if maze[position[0]][position[1]+1] == ' ':
        maze[position[0]][position[1]+1] = 'X'
        if not find_path(maze, [position[0],position[1]+1]):
            maze[position[0]][position[1]+1] = ' '
            return False
    if maze[position[0]][position[1]-1] == ' ':
        maze[position[0]][position[1]-1] = 'X'
        if not find_path(maze, [position[0],position[1]-1]):
            maze[position[0]][position[1]-1] = ' '
            return False
    return False
# Open the maze file and read its contents
with open(filename, "r") as file:
    file_contents = file.readlines() 

    maze_height = len(file_contents) 
    maze_width = max(len(line) for line in file_contents)


for x in range(maze_width):
    if ' ' == file_contents[0][x]:
        find_path(file_contents, [0,x])
print(file_contents)