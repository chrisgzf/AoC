import math

with open("Day03_Input") as f:
    wires = f.readlines()

assert len(wires) == 2

# calculate the upper and lower bounds to avoid creating an unneccesarily large
# array (note: this is not needed. you can just set an arbitrarily large 2d
# array of like size 32000 x 32000 and set your origin to be right smack in the
# middle and im sure it will work too)
xmin, ymin, xmax, ymax = 0, 0, 0, 0
for wire in wires:
    xcursor, ycursor = 0, 0
    for move in wire.split(","):
        direction, length = move[0], int(move[1:])
        if direction == "U":
            ycursor += length
            ymax = max(ymax, ycursor)
        elif direction == "D":
            ycursor -= length
            ymin = min(ymin, ycursor)
        elif direction == "L":
            xcursor -= length
            xmin = min(xmin, xcursor)
        elif direction == "R":
            xcursor += length
            xmax = max(xmax, xcursor)

xsize = xmax - xmin + 1 # add one to also count zero
ysize = ymax - ymin + 1 

board = [[0 for _ in range(xsize)] for __ in range(ysize)]
# note: this uses a lot of memory

xorigin, yorigin = abs(xmin), abs(ymin)
# sets your coord system from
# [xmin, ... , 0, ... , xmax] -> [0, ... , -xmin, ... , xmax - xmin]

wire1 = wires[0].split(",")
wire2 = wires[1].split(",")

# load first wire onto board
xcursor, ycursor = xorigin, yorigin
for move in wire1:
    direction, length = move[0], int(move[1:])
    for i in range(length):
        if direction == "U":
            ycursor += 1
        elif direction == "D":
            ycursor -= 1
        elif direction == "L":
            xcursor -= 1
        elif direction == "R":
            xcursor += 1
        board[ycursor][xcursor] = 1

# second wire, find intersections
min_manhattan = math.inf
xcursor, ycursor = xorigin, yorigin
for move in wire2:
    direction, length = move[0], int(move[1:])
    for i in range(length):
        if direction == "U":
            ycursor += 1
        elif direction == "D":
            ycursor -= 1
        elif direction == "L":
            xcursor -= 1
        elif direction == "R":
            xcursor += 1
        if board[ycursor][xcursor] == 1:
            # overlap detected, calculate Manhattan Distance
            manhattan = abs(xcursor - xorigin) + abs(ycursor - yorigin)
            min_manhattan = min(manhattan, min_manhattan)

# output result
print(min_manhattan)