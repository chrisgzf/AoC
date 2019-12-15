NUM_PARAMS = 3

with open("Day13_Input") as f:
    prog = f.read().strip().split(",")
    prog = list(map(int, prog))

prog = prog + [0] * 100000 # pad with extra zeroes for additional memory

buffer = 0
param = [None] * NUM_PARAMS
i = 0
relative_base = 0

input_count = 0
xs, ys, blocks = [], [], []
while True:
    opcode = prog[i]
    opcode = str(opcode)

    # parse all parameter types first
    for x in range(NUM_PARAMS):
        try:
            param[x] = int(opcode[-3-x])
        except:
            param[x] = 0
    
    # parse opcode
    opcode = int(opcode[-2:])

    # evaluate the positional inputs based on their modes
    read = [prog[i + x] for x in range(1, 1 + NUM_PARAMS)]
    write = read[:] # copy unedited read list for write operations
    for x in range(NUM_PARAMS):
        if param[x] == 0: # position mode
            try:
                read[x] = prog[read[x]]
            except IndexError:
                continue # forced n-parsing is parsing vals beyond prog size
        elif param[x] == 1: # immediate mode
            continue
        elif param[x] == 2: # relative mode
            read[x] = prog[relative_base + read[x]]
            write[x] = relative_base + write[x]
        else: # unrecognised mode
            raise Exception(f"Unrecognised mode for instruction {i + 1}\
                            where param {x + 1} gives mode code {param[x]}.")

    # check opcodes
    if opcode == 1: # addition [op, in1, in2, write]
        prog[write[2]] = read[0] + read[1]
        i += 4
    elif opcode == 2: # multiplication [op, in1, in2, write]
        prog[write[2]] = read[0] * read[1]
        i += 4
    elif opcode == 3: # read input buffer [op, write]
        prog[write[0]] = buffer
        i += 2
    elif opcode == 4: # write to output buffer [op, read]
        message = read[0]
        input_count %= 3
        if input_count == 0:
            xs.append(message)
        elif input_count == 1:
            ys.append(message)
        elif input_count == 2:
            blocks.append(message)
        input_count += 1

        # buffer = read[0]
        # print(f"OPCODE 4: {buffer}")
        i += 2
    elif opcode == 5: # jump if true [op, check-nonzero, jump]
        if (read[0] != 0):
            i = read[1]
        else:
            i += 3
    elif opcode == 6: # jump if false [op, check-zero, jump]
        if (read[0] == 0):
            i = read[1]
        else:
            i += 3
    elif opcode == 7: # less than [op, a, less-than b, write-1]
        if (read[0] < read[1]):
            prog[write[2]] = 1
        else:
            prog[write[2]] = 0
        i += 4
    elif opcode == 8: # equals [op, a, equals b, write-1]
        if (read[0] == read[1]):
            prog[write[2]] = 1
        else:
            prog[write[2]] = 0
        i += 4
    elif opcode == 9: # adjust relative base [op, correction]
        relative_base += read[0]
        i += 2
    elif opcode == 99: # halt
        print("HALTED")
        break
    else: # unrecognised opcode
        raise Exception(f"Unrecognised opcode {opcode} in instruction {i + 1}")

print(blocks)
print(len(list(filter(lambda x: x == 2, blocks))))