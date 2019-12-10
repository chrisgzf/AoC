import math, itertools

with open("Day10_Input") as f:
    the_map = f.readlines()
    the_map = [x.strip() for x in the_map]

asteroids = set()
for y in range(len(the_map)):
    for x in range(len(the_map[y])):
        if the_map[y][x] == "#":
            asteroids.add((x, y))

dist_from_stn = lambda a: abs(a[0] - x1) + abs(a[1] - y1) # manhattan distance

def angle_from_stn(ast_line):
    ast = ast_line[0]
    x, y = ast
    angle = math.atan2(x - x1, y - y1)
    return math.pi - angle

# station is at (23, 19) NOTE: this is HARDCODED.
# you can easily derive the coords from your part 1 solution
station = (23, 19)
asteroids.remove(station)
x1, y1 = station
ast_lines = []

# this portion of the code separates the asteroids into collinear clusters
while asteroids:
    x2, y2 = asteroids.pop()
    in_a_row = [(x2, y2)]
    dy = y2 - y1
    dx = x2 - x1
    if dy == 0:
        if x2 < x1: # LHS
            collinear = set(filter(lambda a: a[1] == y1 and a[0] < x1, asteroids))
        else: # RHS
            collinear = set(filter(lambda a: a[1] == y1 and a[0] > x1, asteroids))
    elif dx == 0:
        if y2 < y1: # Higher
            collinear = set(filter(lambda a: a[0] == x1 and a[1] < y1, asteroids))
        else: # Lower
            collinear = set(filter(lambda a: a[0] == x1 and a[1] > y1, asteroids))
    else:
        collinear = set()
        for x3, y3 in asteroids:
            scale_x = (x3 - x1) / dx
            scale_y = (y3 - y1) / dy
            if scale_x == scale_y and scale_x > 0 and scale_y > 0:
                # x3y3 collinear to x1y1 x2y2
                collinear.add((x3, y3))
    asteroids = asteroids - collinear

    # sort the asteroids by manhattan distance
    in_a_row.extend(collinear)
    in_a_row.sort(key=dist_from_stn)
    ast_lines.append(in_a_row)

# this sorts the lines by the angle they make from the y-axis, with the station
# as origin
ast_lines.sort(key=angle_from_stn)

c = itertools.cycle(ast_lines)
count = 0
for x in c:
    last_destroyed = x.pop(0)
    count += 1
    if count == 200:
        print(last_destroyed[0] * 100 + last_destroyed[1])
        break
