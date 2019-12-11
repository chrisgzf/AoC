NUM_PARAMS = 3
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
BLACK, WHITE = 0, 1
TURNLEFT, TURNRIGHT = 0, 1

with open("Day11_Input") as f:
    prog = f.read().strip().split(",")
    prog = list(map(int, prog))

prog = prog + [0] * 100000 # pad with extra zeroes for additional memory

param = [None] * NUM_PARAMS
i = 0
relative_base = 0

canvas = {}
direction = UP
input_buffer = BLACK
output_buffer = 0
message_is_direction = False
x, y = 0, 0
while i < len(prog):
    opcode = prog[i]
    opcode = str(opcode)

    # parse all parameter types first
    for a in range(NUM_PARAMS):
        try:
            param[a] = int(opcode[-3-a])
        except:
            param[a] = 0
    
    # parse opcode
    opcode = int(opcode[-2:])

    # evaluate the positional inputs based on their modes
    read = [prog[i + a] for a in range(1, 1 + NUM_PARAMS)]
    write = read[:] # copy unedited read list for write operations
    for a in range(NUM_PARAMS):
        if param[a] == 0: # position mode
            try:
                read[a] = prog[read[a]]
            except IndexError:
                continue # forced n-parsing is parsing vals beyond prog size
        elif param[a] == 1: # immediate mode
            continue
        elif param[a] == 2: # relative mode
            read[a] = prog[relative_base + read[a]]
            write[a] = relative_base + write[a]
        else: # unrecognised mode
            raise Exception(f"Unrecognised mode for instruction {i + 1}\
                            where param {a + 1} gives mode code {param[a]}.")

    # check opcodes
    if opcode == 1: # addition [op, in1, in2, write]
        prog[write[2]] = read[0] + read[1]
        i += 4
    elif opcode == 2: # multiplication [op, in1, in2, write]
        prog[write[2]] = read[0] * read[1]
        i += 4
    elif opcode == 3: # read input buffer [op, write]
        if (x, y) in canvas:
            input_buffer = canvas[(x, y)]
        else:
            input_buffer = BLACK
        
        prog[write[0]] = input_buffer
        i += 2
    elif opcode == 4: # write to output buffer [op, read]
        output_buffer = read[0]
        if not message_is_direction: # message is colour
            assert output_buffer in {0, 1}
            canvas[(x, y)] = output_buffer
            message_is_direction = True
        else: # message is direction
            assert output_buffer in {TURNLEFT, TURNRIGHT}
            if output_buffer == TURNLEFT:
                if direction == UP:
                    x -= 1
                    direction = LEFT
                elif direction == RIGHT:
                    y += 1
                    direction = UP
                elif direction == DOWN:
                    x += 1
                    direction = RIGHT
                elif direction == LEFT:
                    y -= 1
                    direction = DOWN
            elif output_buffer == TURNRIGHT:
                if direction == UP:
                    x += 1
                    direction = RIGHT
                elif direction == RIGHT:
                    y -= 1
                    direction = DOWN
                elif direction == DOWN:
                    x -= 1
                    direction = LEFT
                elif direction == LEFT:
                    y += 1
                    direction = UP
            message_is_direction = False
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
        print(f"NO. OF PAINTED PANELS: {len(canvas.keys())}")
        print("HALTED")
        break
    else: # unrecognised opcode
        raise Exception(f"Unrecognised opcode {opcode} in instruction {i + 1}")
