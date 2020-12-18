import Foundation

let ACTIVE: Character = "#"
let INACTIVE: Character = "."

var directions: [(Int, Int, Int, Int)] = []
for dx in -1 ... 1 {
    for dy in -1 ... 1 {
        for dz in -1 ... 1 {
            for dw in -1 ... 1 {
                let dir = (dx, dy, dz, dw)
                if dir == (0, 0, 0, 0) {
                    continue
                }
                directions.append(dir)
            }
        }
    }
}

var state: [[[[Character]]]] = [[[]]]
while let line = readLine() {
    state[0][0].append(Array(line))
}

func getCell(_ x: Int, _ y: Int, _ z: Int, _ w: Int) -> Character {
    if x < 0 || y < 0 || z < 0 || w < 0 || w >= state.count ||
        z >= state[0].count || y >= state[0][0].count ||
        x >= state[0][0][0].count
    {
        return INACTIVE
    }
    return state[w][z][y][x]
}

func isActive(_ x: Int, _ y: Int, _ z: Int, _ w: Int) -> Bool {
    return getCell(x, y, z, w) == ACTIVE
}

func runOneGeneration() {
    var nextState: [[[[Character]]]] =
        Array(repeating:
            Array(repeating:
                Array(repeating:
                    Array(repeating: INACTIVE, count: state[0][0][0].count + 2),
                    count: state[0][0][0].count + 2),
                count: state[0][0][0].count + 2),
            count: state[0][0][0].count + 2)

    for w in -1 ... state.count {
        for z in -1 ... state[0].count {
            for y in -1 ... state[0][0].count {
                for x in -1 ... state[0][0][0].count {
                    let cell = getCell(x, y, z, w)
                    let numActiveNeighbours = directions
                        .map { isActive(x + $0.0, y + $0.1, z + $0.2, w + $0.3) }
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
                    nextState[w + 1][z + 1][y + 1][x + 1] = nextCell
                }
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
    }
    .map {
        $0.map {
            $0.reduce(0) { $0 + $1 }
        }
    }
    .map {
        $0.reduce(0) {
            $0 + $1
        }
    }

// Swift compiler doesn't let me chain another .reduce to the previous chain...
// "compiler is unable to type-check this expression in reasonable time"
let ans = numActive.reduce(0) { $0 + $1 }

print(ans)
