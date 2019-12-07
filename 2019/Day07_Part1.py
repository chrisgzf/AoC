import math, itertools

with open("Day07_Input") as f:
    prog = f.read().strip().split(",")
    prog = list(map(int, prog))

def intcode(phase):
    global input_signal
    this_prog = prog.copy()
    i = 0
    input_count = 0
    while i < len(this_prog):
        op = this_prog[i]
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
            input1 = this_prog[i + 1]
            input2 = this_prog[i + 2]
            out = this_prog[i + 3]
            this_prog[out] = ((this_prog[input1] if param1 == 0 else input1) +
                        (this_prog[input2] if param2 == 0 else input2))
            i += 4
        elif op == 2:
            # multiply
            input1 = this_prog[i + 1]
            input2 = this_prog[i + 2]
            out = this_prog[i + 3]
            this_prog[out] = ((this_prog[input1] if param1 == 0 else input1) *
                        (this_prog[input2] if param2 == 0 else input2))
            i += 4
        elif op == 3:
            if input_count == 0:
                this_prog[this_prog[i + 1]] = phase
            else:
                assert input_count == 1
                this_prog[this_prog[i + 1]] = input_signal
            input_count += 1
            i += 2
        elif op == 4:
            input_signal = this_prog[this_prog[i + 1]]
            # print(this_prog[this_prog[i + 1]])
            i += 2
        elif op == 5:
            input1 = this_prog[i + 1]
            input2 = this_prog[i + 2]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 != 0):
                i = input2
            else:
                i += 3
        elif op == 6:
            input1 = this_prog[i + 1]
            input2 = this_prog[i + 2]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 == 0):
                i = input2
            else:
                i += 3
        elif op == 7:
            input1 = this_prog[i + 1]
            input2 = this_prog[i + 2]
            out = this_prog[i + 3]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 < input2):
                this_prog[out] = 1
            else:
                this_prog[out] = 0
            i += 4
        elif op == 8:
            input1 = this_prog[i + 1]
            input2 = this_prog[i + 2]
            out = this_prog[i + 3]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 == input2):
                this_prog[out] = 1
            else:
                this_prog[out] = 0
            i += 4
        elif op == 99:
            # quit
            break
        else:
            print(f"{op} fuuuck")
            exit(0)

max_thruster = -math.inf

for amp_a, amp_b, amp_c, amp_d, amp_e in itertools.permutations(range(5)):
    input_signal = 0
    intcode(amp_a)
    intcode(amp_b)
    intcode(amp_c)
    intcode(amp_d)
    intcode(amp_e)
    max_thruster = max(max_thruster, input_signal)

print(max_thruster)