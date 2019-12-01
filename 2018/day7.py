with open("d7.txt") as f:
    lines = f.readlines()

for line in lines:
    line = line.replace(" must be finished before step", "").replace("Step ", "").replace(" can begin.", "").strip()
    x, y = line.split(" ")

soln = ""

seconds = 1
n_workers = 5
seconds_pad = 60
worker = [(0, None)] * n_workers

def get_time(txt):
    return ord(txt) - ord("A") + 1 + seconds_pad

while nodes or any(filter(lambda x: x[1] != None, worker)):
    no_inward_edges = list()
    for node in nodes:
        has_edges = False
        for (x, y) in adj:
            if node == y:
                has_edges = True
                break
        if not has_edges:
            no_inward_edges.append(node)

    no_inward_edges.sort()
    
    for job in no_inward_edges:
        for i in range(n_workers):
            if worker[i][0] == 0:
                worker[i] = (get_time(job), job)
                nodes.remove(job)
                break
    
    
    worker = [(x-1, y) if x != 0 else (0,y) for (x, y) in worker]

    for i in range(n_workers):
        if worker[i][0] == 0:
            adj = list(filter(lambda x: x[0] != worker[i][1], adj))
            soln += ("" if worker[i][1] is None else worker[i][1])
            worker[i] = (0, None)
    print(f"Second: {seconds}")
    print(f"Workers: {worker}")
    print(f"Possible Edges: {no_inward_edges}")
    print(f"Soln: {soln}")
    seconds += 1

print(soln)

# With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?