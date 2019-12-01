with open("d8.txt") as f:
    strr = f.read().replace(" ", ",")

lines = []
while strr is not "":
    n = 76
    if len(strr) <= n:
        print(strr)
        break
    while strr[n-1] != ",":
        n -= 1
    print(strr[:n])
    strr = strr[n:]

