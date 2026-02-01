from strainman.canvas import canvas_creator
from strainman.square import square
from strainman import __version__
import numpy as np
import tomllib

print(f"Using Strainman Package version: {__version__}")

# Open config file and set variables to values in file
with open('config.toml', 'rb') as f:
    config = tomllib.load(f)
size = config['size']
square_size = config['square_size']
square_x_location = config['square_x_location']
square_y_location = config['square_y_location']
dx = config['dx']
dy = config['dy']

# Prevent canvas from being represented with ellipses
np.set_printoptions(threshold=np.inf)

# Open output file, run functions, and write outputs to file
f = open("output.txt", "w+")
canvas = canvas_creator(size)
f.write(str(canvas))
f.write("\n")
sq = square(square_size, np.array([square_x_location, square_y_location]))
canvas = sq.draw(canvas)
f.write(str(canvas))
f.write("\n")
canvas = sq.move(canvas, dx, dy)
f.write(str(canvas))
canvas = sq.mesh_extract(canvas)
f.write(str(canvas))
f.close()