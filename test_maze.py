with open("maze.txt", "r") as file:
    file_contents = file.read()

for line in file_contents.splitlines():
    print(line)