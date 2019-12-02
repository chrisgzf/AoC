with open("Day02_Input") as f:
    prog = f.read().strip().split(",")
    prog = list(map(int, prog))
prog[1] = 12
prog[2] = 2

for i in range(0, len(prog), 4):
    op = prog[i]
    input1 = prog[i + 1]
    input2 = prog[i + 2]
    out = prog[i + 3]
    if op == 1:
        # add
        prog[out] = prog[input1] + prog[input2]
    elif op == 2:
        # multiply
        prog[out] = prog[input1] * prog[input2]
    elif op == 99:
        # quit
        break

print(prog[0])