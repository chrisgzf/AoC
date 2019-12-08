with open("Day08_Input") as f:
    picture = f.read().strip()

l = 25
b = 6
layersize = l * b
layers = [picture[i:i+layersize] for i in range(0, len(picture), layersize)]

assert len(picture) / layersize == len(layers)
picture = [[" " for _ in range(l)] for __ in range(b)]

for row in range(b):
    for col in range(l):
        for layer in layers:
            colour = layer[row*l + col]
            if colour != "2":
                picture[row][col] = " " if colour == "0" else "O"
                break

print("\n".join(map(lambda x: " ".join(x), picture)))