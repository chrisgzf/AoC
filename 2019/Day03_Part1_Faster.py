import math

with open("Day03_Input") as f:
    wires = f.readlines()

assert len(wires) == 2

wire1 = wires[0].split(",")
wire2 = wires[1].split(",")

wire1_pts = set()
wire2_pts = set()

# load first wire onto board
x, y = 0, 0
for move in wire1:
    direction, length = move[0], int(move[1:])
    for i in range(length):
        if direction == "U":
            y += 1
        elif direction == "D":
            y -= 1
        elif direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        wire1_pts.add((x, y))

# load second wire onto board
x, y = 0, 0
for move in wire2:
    direction, length = move[0], int(move[1:])
    for i in range(length):
        if direction == "U":
            y += 1
        elif direction == "D":
            y -= 1
        elif direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        wire2_pts.add((x, y))

# find intersections
intersections = wire1_pts.intersection(wire2_pts)

def get_manhattan_distance(x):
    return abs(x[0]) + abs(x[1])

print(sorted(map(get_manhattan_distance, intersections))[0])