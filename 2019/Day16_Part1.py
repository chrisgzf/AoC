import numpy as np

with open("Day16_Input") as f:
    signal = f.read().strip()

def gen_pattern(i):
    i += 1
    pattern = [0] * i + [1] * i + [0] * i + [-1] * i
    while len(pattern) < len(signal) + 1:
        pattern += pattern
    pattern = np.array(pattern[1: len(signal) + 1])
    return pattern

patterns = {}
def fft(signal):
    signal = np.array(list(map(int, signal)))
    out = ""
    for i in range(len(signal)):
        if i in patterns:
            pattern = patterns[i]
        else:
            pattern = gen_pattern(i)
            patterns[i] = pattern
        out += str(sum(signal * pattern))[-1]
    return out
        
num_phases = 100
for i in range(num_phases):
    signal = fft(signal)
print(signal[:8])