from tqdm import tqdm

with open("Day16_Input") as f:
    signal = f.read().strip()

signal *= 10000
offset = int(signal[:7])
second_half = signal[int(len(signal)/2):]

def second_half_fft(signal):
    out = ""
    total = 0
    for i in reversed(list(map(int, signal))):
        total += i
        out = str(total)[-1] + out
    return out

for i in tqdm(range(100)):
    second_half = second_half_fft(second_half)

offset -= len(second_half)
print(second_half[offset:offset+8])