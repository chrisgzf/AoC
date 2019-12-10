with open("Day10_Input") as f:
    the_map = f.readlines()
    the_map = [x.strip() for x in the_map]

asteroids = set()
for y in range(len(the_map)):
    for x in range(len(the_map[y])):
        if the_map[y][x] == "#":
            asteroids.add((x, y))

def get_detections(asteroid):
    rest = asteroids.copy()
    rest.remove(asteroid)
    x1, y1 = asteroid
    detected = 0
    while rest:
        x2, y2 = rest.pop()
        dy = y2 - y1
        dx = x2 - x1
        if dy == 0:
            if x2 < x1: # LHS
                collinear = set(filter(lambda a: a[1] == y1 and a[0] < x1, rest))
            else: # RHS
                collinear = set(filter(lambda a: a[1] == y1 and a[0] > x1, rest))
        elif dx == 0:
            if y2 < y1: # Higher
                collinear = set(filter(lambda a: a[0] == x1 and a[1] < y1, rest))
            else: # Lower
                collinear = set(filter(lambda a: a[0] == x1 and a[1] > y1, rest))
        else:
            collinear = set()
            for x3, y3 in rest:
                scale_x = (x3 - x1) / dx
                scale_y = (y3 - y1) / dy
                if scale_x == scale_y and scale_x > 0 and scale_y > 0:
                    # x3y3 collinear to x1y1 x2y2
                    collinear.add((x3, y3))
        rest = rest - collinear
        detected += 1
    return detected

print(max(map(get_detections, asteroids)))