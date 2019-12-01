def calc_fuel(line):
    n = int(line.strip())
    fuel = 0
    while (n >= 1):
        add = (n := n // 3 - 2)
        fuel += add if add > 0 else 0
    return fuel
    
print(sum(map(calc_fuel, open("Day01_Input").readlines())))