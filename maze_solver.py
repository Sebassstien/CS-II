# Collaborators:
# Sebastien LaFontaine
# Spencer Ollmann

filename = "maze.txt"


def find_path(maze : list[list[str]], position : tuple[int, int]) -> bool:
    # if there is another path while backtracking it should stop removing X and take the path
    maze[position[0]][position[1]] = 'X'
    if maze[position[0]][position[1]-1] == 'O':
        return True
    
    if maze[position[0]+1][position[1]] == ' ':
        if not find_path(maze, [position[0]+1,position[1]]):
            maze[position[0]+1][position[1]] = ' '
            return False
    if maze[position[0]-1][position[1]] == ' ':        
        if not find_path(maze, [position[0]-1,position[1]]):
            maze[position[0]-1][position[1]] = ' '
            return False
    if maze[position[0]][position[1]+1] == ' ':
        if not find_path(maze, [position[0],position[1]+1]):
            maze[position[0]][position[1]+1] = ' '
            return False
    if maze[position[0]][position[1]-1] == ' ':
        if not find_path(maze, [position[0],position[1]-1]):
            maze[position[0]][position[1]-1] = ' '
            return False
    return False
# Open the maze file and read its contents
with open(filename, "r") as file:
    file_contents = file.readlines()
    for i in range(len(file_contents)):
        file_contents[i] = file_contents[i].strip()
    maze = []
    for i in range(len(file_contents)):
        maze.append([])
        for j in file_contents[i]:
            maze[i].append(j)
    maze_height = len(maze) 
    maze_width = max(len(line) for line in maze)


for x in range(maze_width):
    if 'I' == maze[0][x]:
        find_path(maze, [1,x])
for i in maze:
    print(i)