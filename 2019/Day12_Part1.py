import re

with open("Day12_Input") as f:
    positions = f.readlines()
    positions = [x.strip() for x in positions]

pattern = "x=([^,]*).{2}y=([^,]*).{2}z=([^>]*)"

moons = []
for moon in positions:
    info = [int(i) for i in re.findall(pattern, moon)[0]] + [0, 0, 0]
    moons.append(info)

# i save my pos and vels per moon with [posx, posy, posz, velx, vely, velz]

for step in range(1000):
    # applying gravity
    velocity_changes = [[0] * len(moons), [0] * len(moons), [0] * len(moons)]
    pos = [list(a) for a in list(zip(*moons))]

    # fetching all velocity changes
    for a in range(3): # 0 is x, 1 is y, 2 is z
        for i in range(len(pos[a])):
            rest = pos[a][:]
            del rest[i]
            for b in rest:
                if pos[a][i] > b:
                    velocity_changes[a][i] -= 1
                elif pos[a][i] < b:
                    velocity_changes[a][i] += 1

    # applying velocity changes
    for axis_no in range(len(velocity_changes)):
        for moon_no in range(len(velocity_changes[axis_no])):
            moons[moon_no][3 + axis_no] += velocity_changes[axis_no][moon_no]

    # applying velocity (i.e. changing position)
    for moon_no in range(len(moons)):
        for axis in range(3):
            moons[moon_no][axis] += moons[moon_no][axis + 3]

print(moons)

print(sum(map(lambda x: sum(map(abs, x[:3])) * sum(map(abs, x[3:])), moons)))