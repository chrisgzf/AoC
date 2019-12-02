with open("Day02_Input") as f:
    original_prog = f.read().strip().split(",")
    original_prog = list(map(int, original_prog))

output = 0

for noun in range(100):
    for verb in range(100):
        prog = original_prog.copy()
        prog[1] = noun
        prog[2] = verb

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

        output = prog[0]
        if output == 19690720:
            print(noun)
            print(verb)
            break
    if output == 19690720:
            break

