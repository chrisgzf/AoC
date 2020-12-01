with open("Day01_Input") as f:
    entries = f.readlines()
    entries = list(map(int, entries))


def solve():
    for i in range(len(entries)):
        for j in range(len(entries)):
            if entries[i] + entries[j] == 2020:
                print(entries[i] * entries[j])
                return

solve()