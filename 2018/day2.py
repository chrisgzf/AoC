with open("d2.txt") as f:
    lines = f.readlines()

def proc_line(line):
    line = line.strip()
    elements = set(line)
    print(elements)
    counts = set(map(lambda x: line.count(x), elements))
    print(counts)
    print((2 in counts, 3 in counts))
    return (2 in counts, 3 in counts)

print(list(map(proc_line, lines)))
n_2s, n_3s = zip(*map(proc_line, lines))
n_2s = len(list(filter(None, n_2s)))
n_3s = len(list(filter(None, n_3s)))
print(n_2s * n_3s)