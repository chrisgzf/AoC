from tqdm import tqdm

with open("Day16_Input") as f:
    signal = f.read().strip()

signal *= 10000
offset = int(signal[:7])
needed_digits = signal[offset:]

def second_half_fft(signal):
    out = ""
    total = 0
    for i in reversed(list(map(int, signal))):
        total += i
        out = str(total)[-1] + out
    return out

for i in tqdm(range(100)):
    needed_digits = second_half_fft(needed_digits)

print(needed_digits[:8])