from collections import defaultdict

with open("Day06_Input") as f:
    orbits = f.readlines()
    orbits = list(map(lambda x: x.strip(), orbits))

print(len(orbits))

edges = defaultdict(list)
vertices = set()

for orbit in orbits:
    orbitee, orbiter = orbit.split(")")
    edges[orbiter].append(orbitee)
    vertices.add(orbitee)
    vertices.add(orbiter)

def search_root(orbiter, traversed):
    # i cannot write a DFS properly gg
    if edges[orbiter] == []:
        return False
    results = []
    traversed = traversed.copy()
    for edge in edges[orbiter]:
        if edge == "COM":
            traversed.append(orbiter)
            results.append(traversed)
        else:
            traversed.append(orbiter)
            results.append(search_root(edge, traversed))
    if any(results):
        return list(filter(None, results))[0]
    else:
        return False


print(sum(map(len, filter(None, map(lambda x: search_root(x, list()), vertices)))))