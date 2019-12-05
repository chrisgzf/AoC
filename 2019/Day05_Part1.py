with open("Day05_Input") as f:
    prog = f.read().strip().split(",")
    prog = list(map(int, prog))

print(len(prog))
i = 0
inst_input = 1
while i < len(prog):
    op = prog[i]
    a = str(op)
    op = int(a[-2:])
    try:
        param1 = int(a[-3])
    except:
        param1 = 0
    try:
        param2 = int(a[-4])
    except:
        param2 = 0
    try:
        param3 = int(a[-5])
    except:
        param3 = 0
    if op == 1:
        # add
        input1 = prog[i + 1]
        input2 = prog[i + 2]
        out = prog[i + 3]
        prog[out] = ((prog[input1] if param1 == 0 else input1) +
                     (prog[input2] if param2 == 0 else input2))
        i += 4
    elif op == 2:
        # multiply
        input1 = prog[i + 1]
        input2 = prog[i + 2]
        out = prog[i + 3]
        prog[out] = ((prog[input1] if param1 == 0 else input1) *
                     (prog[input2] if param2 == 0 else input2))
        i += 4
    elif op == 3:
        prog[prog[i + 1]] = inst_input
        i += 2
    elif op == 4:
        inst_input = prog[prog[i + 1]]
        i += 2
    elif op == 99:
        # quit
        break
    else:
        print(f"{op} fuuuck")
        exit(0)

    print(inst_input)
print(inst_input)
