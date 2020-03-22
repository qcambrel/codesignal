def rotateImage(a):
    return [list(reversed(row)) for row in list(zip(*a))]