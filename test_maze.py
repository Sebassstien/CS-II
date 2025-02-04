class Wall:
	x = -1
	y = -1
	up = False
	down = False
	left = False
	right = False
	# _x and _y are the walls coordinates. _up, _down, _left, and _right are connection booleans
	def __init__(self, _x, _y, _up, _down, _left, _right):
		self.x = _x
		self.y = _y
		self.up = _up
		self.down = _down
		self.left = _left
		self.right = _right
		return
	def getUp(self):
		return self.up
	def getDown(self):
		return self.down
	def getLeft(self):
		return self.left
	def getRight(self):
		return self.right
	def print(self):
		if self.up and self.down and self.left and self.right:
			print('+', end='')
		elif self.up and self.left and self.right:
			print('⫠', end='')
		elif self.up and self.left and self.down:
			print('⊣', end='')
		elif self.up and self.right and self.down:
			print('⊢', end='')
		elif self.up and self.left:
			print('˩', end='')
		elif self.up and self.right:
			print('꜖', end='')
		elif self.down and self.left and self.right:
			print('⫟', end='')
		elif self.down and self.left:
			print('˥', end='')
		elif self.down and self.right:
			print('꜒', end='')
		elif self.up or self.down:
			print('|', end='')
		elif self.left or self.right:
			print('−', end='')
		elif not self.up and not self.down and not self.left and not self.right:
			print('*', end='')
		return
		
with open("maze.txt", "r") as file:
	file_contents = file.read()
	mazeSpaces = []
	#Check if there is a '#' to set the value as True
	for lineNum in range(len(file_contents.splitlines())):
		line = file_contents.splitlines()[lineNum]
		for c in range(len(line)):
			right = False
			left = False
			up = False
			down = False
			if '#' != line[c]:
				if c+1 < len(line):
					print('O', end='')
				mazeSpaces.append(None)
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
			mazeSpaces.append(Wall(c, len(file_contents.splitlines())-lineNum, up, down, left, right))
			
			
	# Draw the walls and connections
			mazeSpaces[-1].print()
		print('')
	print("")
	for i in range(len(mazeSpaces)):
		if None == mazeSpaces[i]:
			print(' ',end='')
			continue
		mazeSpaces[i].print()
		if i+1 < len(mazeSpaces):
			if (False == mazeSpaces[i].getRight()) and (mazeSpaces[i+1] != None):
				print('')
	print('')
