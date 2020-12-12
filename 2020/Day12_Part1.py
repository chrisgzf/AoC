import math

with open("Day12_Input") as f:
    data = f.readlines()

deg = 90
x = 0
y = 0

for move in data:
    op = move[0]
    param = int(move[1:])
    if op == "N":
        y += param
    elif op == "S":
        y -= param
    elif op == "W":
        x -= param
    elif op == "E":
        x += param
    elif op == "L":
        deg -= param
    elif op == "R":
        deg += param
    elif op == "F":
        x += param * math.sin(math.radians(deg))
        y += param * math.cos(math.radians(deg))

print(abs(x) + abs(y))
