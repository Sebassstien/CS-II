with open("maze.txt", "r") as file:
    file_contents = file.read()
    #Check if there is a '#' to set the value as True
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

        # Draw the walls and connections
        if up and down and left and right:
            print('+', end='')
        elif up and left and right:
            print('⫠', end='')
        elif up and left and down:
            print('⊣', end='')
        elif up and right and down:
            print('⊢', end='')
        elif up and left:
            print('⨼', end='')
        elif up and right:
            print('⨽', end='')
        elif down and left and right:
            print('⫟', end='')
        elif down and left:
            print('ɿ', end='')
        elif down and right:
            print('ɾ', end='')
        elif up or down:
            print('|', end='')
        elif left or right:
            print('−', end='')
        elif not up and not down and not left and not right:
            print('*', end='')

    print('')