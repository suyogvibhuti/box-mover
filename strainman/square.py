class square:
    def __init__(self, size, location):
        # size is int, location is np array of form (x, y)
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
        # dx, dy are ints
        self.undraw(canvas)
        self.location[0] += dx
        self.location[1] += dy
        self.draw(canvas)
        return canvas
    
    def mesh_extract(self, canvas):
        # Not sure if the mesh extraction should return a set of points and functions that define the lines between them, or just the canvas with the center of the square hollowed out
        for i in range(self.size - 2):
            for j in range(self.size - 2):
                xpoint = self.location[0] + i + 1
                ypoint = self.location[1] + j + 1
                canvas[xpoint, ypoint] = 0
        return canvas