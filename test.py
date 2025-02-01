import graphics as g;
def main():
	with open("/Users/spencerollmann/xcoding/CS172/CS172.2/maze.txt") as f:
		win = g.GraphWin("Maze", 400, 400);
		size = 5;
		win.setCoords(-0.5, -0.5, size+0.5, size+0.5);
		while True:
			line = f.readline();
			if '' == line:
				break;
			for i in range(len(line)):
				if '#' == line[i]:
					l = g.Line(g.Point(1.0,5.0), g.Point(1.0, 4.0));
					l.setWidth(3);
					l.draw(win);
					win.getMouse();
					win.close();
					print('-', end='');
				else:
					print(' ', end='');
			print('');
			win.getMouse();
			win.close();
		
if "__main__" == __name__:
	main();

