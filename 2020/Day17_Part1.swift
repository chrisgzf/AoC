let ACTIVE: Character = "#"
let INACTIVE: Character = "."

var directions: [(Int, Int, Int)] = []
for dx in -1 ... 1 {
    for dy in -1 ... 1 {
        for dz in -1 ... 1 {
            let dir = (dx, dy, dz)
            if dir == (0, 0, 0) {
                continue
            }
            directions.append(dir)
        }
    }
}

var state: [[[Character]]] = [[]]
while let line = readLine() {
    state[0].append(Array(line))
}

func getCell(_ x: Int, _ y: Int, _ z: Int) -> Character {
    if x < 0 || y < 0 || z < 0 || z >= state.count || y >= state[0].count || x >= state[0][0].count {
        return INACTIVE
    }
    return state[z][y][x]
}

func isActive(_ x: Int, _ y: Int, _ z: Int) -> Bool {
    return getCell(x, y, z) == ACTIVE
}

func runOneGeneration() {
    var nextState: [[[Character]]] =
        Array(repeating:
            Array(repeating:
                Array(repeating: INACTIVE, count: state[0][0].count + 2),
                count: state[0][0].count + 2),
            count: state[0][0].count + 2)
    for z in -1 ... state.count {
        for y in -1 ... state[0].count {
            for x in -1 ... state[0][0].count {
                let cell = getCell(x, y, z)
                let numActiveNeighbours = directions
                    .map { isActive(x + $0.0, y + $0.1, z + $0.2) }
                    .filter { $0 }
                    .count
                let nextCell: Character
                if cell == ACTIVE {
                    if numActiveNeighbours == 2 || numActiveNeighbours == 3 {
                        nextCell = ACTIVE
                    } else {
                        nextCell = INACTIVE
                    }
                } else if numActiveNeighbours == 3 {
                    nextCell = ACTIVE
                } else {
                    nextCell = INACTIVE
                }
                nextState[z + 1][y + 1][x + 1] = nextCell
            }
        }
    }
    state = nextState
}

for _ in 0 ..< 6 {
    runOneGeneration()
}

let numActive = state
    .map {
        $0.map {
            $0.reduce(0) { x, y in
                if y == ACTIVE {
                    return x + 1
                } else {
                    return x
                }
            }
        }
    }
    .map {
        $0.reduce(0) { $0 + $1 }
    }
    .reduce(0) {
        $0 + $1
    }

print(numActive)
