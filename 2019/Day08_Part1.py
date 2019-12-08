from functools import reduce

with open("Day08_Input") as f:
    picture = f.read().strip()

layersize = 25 * 6
layers = [picture[i:i+layersize] for i in range(0, len(picture), layersize)]

assert len(picture) / layersize == len(layers)

min_zeroes = reduce(lambda a, b: a if a.count("0") < b.count("0") else b,
                    layers)
print(min_zeroes.count("1") * min_zeroes.count("2"))