var numbers = (readLine()?
    .split { $0 == "," }
    .map { Int($0)! }
)!

var seen: [Int: (Int, Int?)] = [:]

var lastNum: Int = 0

func updateSeen(_ i: Int, _ n: Int) {
    if let prev = seen[n] {
        seen[n] = (i, prev.0)
    } else {
        seen[n] = (i, nil)
    }
}

numbers.enumerated().forEach {
    let (i, num) = $0
    updateSeen(i, num)
    lastNum = num
}

for i in numbers.count ..< 30_000_000 {
    let prev = seen[lastNum]!
    if let second = prev.1 {
        // was spoken
        lastNum = prev.0 - second
    } else {
        // first time
        lastNum = 0
    }
    updateSeen(i, lastNum)
}

print(lastNum)
