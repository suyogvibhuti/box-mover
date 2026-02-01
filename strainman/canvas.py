import numpy as np

def canvas_creator(size):
    # size is int
    canvas = np.zeros((size, size), dtype="int")
    return canvas