sum = 0
mem = set()
found = False
with open("d1.txt") as f:
    lines = f.readlines()
    
i = 0
while not found:
    i += 1
    # print("lol")
    for line in lines:
        opr, num = line[0], int(line[1:])
        if opr == "-":
            sum -= num
        else:
            sum += num
        if sum in mem:
            found = True
            print(sum)
            break
        else:
            mem.add(sum)
print(i)