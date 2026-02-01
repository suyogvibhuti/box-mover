import numpy as np
size = 128
square_size = 50
square_x_location = int(size/2 - square_size/2)
square_y_location = int(size/2 - square_size/2)
dx = 39
dy = 39

class square:
    def __init__(self, size, location):
        #size is int, location is np array of form (x, y)
        self.size = size
        self.location = location
    
    def draw(self, canvas):
        for i in range(self.size):
            for j in range(self.size):
                xpoint = self.location[0] + i
                ypoint = self.location[1] + j
                canvas[xpoint, ypoint] = 1
        return canvas
    
    def undraw(self, canvas):
        for i in range(self.size):
            for j in range(self.size):
                xpoint = self.location[0] + i
                ypoint = self.location[1] + j
                canvas[xpoint, ypoint] = 0
        return canvas

    def move(self, canvas, dx, dy):
        self.undraw(canvas)
        self.location[0] += dx
        self.location[1] += dy
        self.draw(canvas)
        return canvas

def canvas_creator(size):
    canvas = np.zeros((size, size), dtype="int")
    return canvas

canvas = canvas_creator(size)
print(canvas)
print()
sq = square(square_size, np.array([square_x_location, square_y_location]))
canvas = sq.draw(canvas)
print(canvas)
print()
canvas = sq.move(canvas, dx, dy)
print(canvas)