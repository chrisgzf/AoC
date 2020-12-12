import math

with open("Day12_Input") as f:
    data = f.readlines()

x = 0
y = 0
wx = 10
wy = 1

for move in data:
    op = move[0]
    param = int(move[1:])
    if op == "N":
        wy += param
    elif op == "S":
        wy -= param
    elif op == "W":
        wx -= param
    elif op == "E":
        wx += param
    elif op == "L":
        # add angle because atan2 0 at E, (180, 0] from W to E (anticlockwise)
        # [0, -180] from E to W (clockwise)
        deg = math.atan2(wy, wx) + math.radians(param)
        dist = math.hypot(wy, wx)
        wx = dist * math.cos(deg)
        wy = dist * math.sin(deg)
    elif op == "R":
        deg = math.atan2(wy, wx) - math.radians(param)
        dist = math.hypot(wy, wx)
        wx = dist * math.cos(deg)
        wy = dist * math.sin(deg)
    elif op == "F":
        x += param * wx
        y += param * wy

print(abs(x) + abs(y))
