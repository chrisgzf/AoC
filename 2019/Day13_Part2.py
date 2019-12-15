NUM_PARAMS = 3

with open("Day13_Input") as f:
    prog = f.read().strip().split(",")
    prog = list(map(int, prog))

prog = prog + [0] * 100000 # pad with extra zeroes for additional memory
prog[0] = 2

param = [None] * NUM_PARAMS
i = 0
relative_base = 0

input_count = 0
xs, ys, blocks = [], [], []
last_x, last_y = 0, 0
ball_x, ball_y = 0, 0
paddle_x, paddle_y = 0, 0

def print_game():
    game = [[" " for _ in range(max(xs) + 1)] for __ in range(max(ys) + 1)]
    for x, y, b in zip(xs, ys, blocks):
        if b == 1:
            game[y][x] = "|"
        elif b == 2:
            game[y][x] = "8"
        elif b == 3:
            game[y][x] = "-"
        elif b == 4:
            game[y][x] = "o"
    print("\n".join(map(lambda x: "". join(x), game)))

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
        move = -1 if ball_x < paddle_x else 1 if ball_x > paddle_x else 0
        # if move != 0:
        #     old = blocks.index(3)
        #     del blocks[old]
        #     del xs[old]
        #     del ys[old]
        prog[write[0]] = move
        i += 2
    elif opcode == 4: # write to output buffer [op, read]
        message = read[0]
        input_count %= 3
        if input_count == 0:
            xs.append(message)
            last_x = message
        elif input_count == 1:
            ys.append(message)
            last_y = message
        elif input_count == 2:
            # print_game()
            if last_x == -1 and last_y == 0:
                # score display
                del xs[-1]
                del ys[-1]
                score = message
                print(f"Score is {score}")
            else:
                if message == 4:
                    ball_x = last_x
                    ball_y = last_y
                if message == 3:
                    paddle_x = last_x
                    paddle_y = last_y
                blocks.append(message)
        input_count += 1
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
