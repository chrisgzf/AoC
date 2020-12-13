let time = Int(readLine()!)!
let buses = (readLine()?
    .split { $0 == "," }
    .filter { $0 != "x" }
    .compactMap { Int($0) })!

let fastestBus = buses
    .map { ($0 - time % $0, $0) }
    .reduce((Int.max, Int.max)) { x, y in
        if x.0 < y.0 {
            return x
        }
        return y
    }

print(fastestBus.0 * fastestBus.1)
