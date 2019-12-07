import math, itertools

with open("Day07_Input") as f:
    prog = f.read().strip().split(",")
    prog = list(map(int, prog))

def intcode(phase, mem, amp_code):
    global input_signal
    global done
    this_prog = mem
    enter_phase = i[amp_code] == 0
    while i[amp_code] < len(this_prog):
        op = this_prog[i[amp_code]]
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
            input1 = this_prog[i[amp_code] + 1]
            input2 = this_prog[i[amp_code] + 2]
            out = this_prog[i[amp_code] + 3]
            this_prog[out] = ((this_prog[input1] if param1 == 0 else input1) +
                        (this_prog[input2] if param2 == 0 else input2))
            i[amp_code] += 4
        elif op == 2:
            # multiply
            input1 = this_prog[i[amp_code] + 1]
            input2 = this_prog[i[amp_code] + 2]
            out = this_prog[i[amp_code] + 3]
            this_prog[out] = ((this_prog[input1] if param1 == 0 else input1) *
                        (this_prog[input2] if param2 == 0 else input2))
            i[amp_code] += 4
        elif op == 3:
            if enter_phase:
                this_prog[this_prog[i[amp_code] + 1]] = phase
                enter_phase = False
            else:
                this_prog[this_prog[i[amp_code] + 1]] = input_signal
            i[amp_code] += 2
        elif op == 4:
            input_signal = this_prog[this_prog[i[amp_code] + 1]]
            # print(this_prog[this_prog[i[amp_code] + 1]])
            i[amp_code] += 2
            return
        elif op == 5:
            input1 = this_prog[i[amp_code] + 1]
            input2 = this_prog[i[amp_code] + 2]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 != 0):
                i[amp_code] = input2
            else:
                i[amp_code] += 3
        elif op == 6:
            input1 = this_prog[i[amp_code] + 1]
            input2 = this_prog[i[amp_code] + 2]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 == 0):
                i[amp_code] = input2
            else:
                i[amp_code] += 3
        elif op == 7:
            input1 = this_prog[i[amp_code] + 1]
            input2 = this_prog[i[amp_code] + 2]
            out = this_prog[i[amp_code] + 3]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 < input2):
                this_prog[out] = 1
            else:
                this_prog[out] = 0
            i[amp_code] += 4
        elif op == 8:
            input1 = this_prog[i[amp_code] + 1]
            input2 = this_prog[i[amp_code] + 2]
            out = this_prog[i[amp_code] + 3]
            input1 = this_prog[input1] if param1 == 0 else input1
            input2 = this_prog[input2] if param2 == 0 else input2
            if (input1 == input2):
                this_prog[out] = 1
            else:
                this_prog[out] = 0
            i[amp_code] += 4
        elif op == 99:
            # quit
            if amp_code == "E":
                done = True
            break
        else:
            print(f"{op} fuuuck")
            exit(0)

max_thruster = -math.inf

for amp_a, amp_b, amp_c, amp_d, amp_e in itertools.permutations(range(5, 10)):
    input_signal = 0
    mem_A = prog.copy()
    mem_B = prog.copy()
    mem_C = prog.copy()
    mem_D = prog.copy()
    mem_E = prog.copy()
    i = { a : b for a, b in zip("ABCDE", [0, 0, 0, 0, 0])}
    done = False
    while (not done):
        intcode(amp_a, mem_A, "A")
        intcode(amp_b, mem_B, "B")
        intcode(amp_c, mem_C, "C")
        intcode(amp_d, mem_D, "D")
        intcode(amp_e, mem_E, "E")
    max_thruster = max(max_thruster, input_signal)

print(max_thruster)