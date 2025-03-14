# Collaborators:
# Sebastien LaFontaine
# Spencer Ollmann

FILENAME = "maze.txt"


def find_path(maze : list[list[str]], position : tuple[int, int]) -> bool:
    # if there is another path while backtracking it should stop removing X and take the path
    maze[position[0]][position[1]] = 'X'
    if maze[position[0]+1][position[1]] == 'O':
        return True
    de = True #dead end
    if maze[position[0]+1][position[1]] == ' ':
        if find_path(maze, [position[0]+1,position[1]]):
            de = False
    if maze[position[0]-1][position[1]] == ' ':        
        if find_path(maze, [position[0]-1,position[1]]):
            de = False
    if maze[position[0]][position[1]+1] == ' ':
        if find_path(maze, [position[0],position[1]+1]):
            de = False
    if maze[position[0]][position[1]-1] == ' ':
        if find_path(maze, [position[0],position[1]-1]):
            de = False
    if de:
        maze[position[0]][position[1]] = '-'
    return not de

# Open the maze file and read its contents
with open(FILENAME, "r") as file:
    maze = [list(line.strip()) for line in file.readlines()]
    
    maze_height = len(maze) 
    maze_width = max(len(line) for line in maze)


for x in range(maze_width):
    if 'I' == maze[0][x]:
        if not find_path(maze, [1,x]):
            print("No path found!")
        else:
            print("Path found!")
            for y in range(maze_height):
                for x in range(maze_width):
                    if '-' == maze[y][x]:
                        maze[y][x] = ' '
            for i in maze: 
                print(''.join(i))
        break
