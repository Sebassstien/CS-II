import graphics as g
size = 5
win = g.GraphWin("Maze", 400, 400)
win.setCoords(-0.5, -0.5, size + 0.5, size + 0.5)
l = g.Line(g.Point(1.0, 5.0), g.Point(1.0, 4.0))
l.setWidth(3)
l.draw(win)
win.getMouse()
win.close()