with open("maze.txt", "r") as file:
    file_contents = file.read()

for lineNum in range(len(file_contents.splitlines())):
    line = file_contents.splitlines()[lineNum]
    for c in range(len(line)):
        right = False
        left = False
        up = False
        down = False
        if '#' != line[c]:
            print(' ', end='')
            continue
        if c-1 >= 0:
            if '#' == line[c-1]:
                left = True
        if c+1 < len(line):
            if '#' == line[c+1]:
                right = True                
        if lineNum - 1 >= 0:
            if '#' == file_contents.splitlines()[lineNum-1][c]:
                up = True
        if lineNum + 1 < len(file_contents.splitlines()):
            if '#' == file_contents.splitlines()[lineNum+1][c]:
                down = True
        if up == True or True == down and left == True or True == right:
            print('+', end='')
        elif up == True or True == down:
            print('|', end='')
        elif left or right:
            print('-', end='')
        elif up == False and False == down and left == False and False == right:
            print('*', end='')
    print('')