import Foundation

var validNumbers: [Int: Bool] = [:]
func parseRule(_ line: String) {
    let pattern = (try?
        NSRegularExpression(pattern: "(.+): (\\d+)-(\\d+) or (\\d+)-(\\d+)"))!
    let match = pattern.firstMatch(in: line, options: [], range:
        NSRange(location: 0, length: line.utf16.count))!
    // let name = String(line[Range(match.range(at: 1), in: line)!])
    let a = Int(line[Range(match.range(at: 2), in: line)!])!
    let b = Int(line[Range(match.range(at: 3), in: line)!])!
    let c = Int(line[Range(match.range(at: 4), in: line)!])!
    let d = Int(line[Range(match.range(at: 5), in: line)!])!

    for i in a ... b {
        validNumbers[i] = true
    }
    for i in c ... d {
        validNumbers[i] = true
    }
}

// Read Rules
while let line = readLine() {
    if line == "" {
        break
    }
    parseRule(line)
}

// Read your ticket
while let line = readLine() {
    if line == "" {
        break
    }
}

// Read nearby tickets
_ = readLine()
var errorRate = 0
while let line = readLine() {
    errorRate += line
        .split { $0 == "," }
        .compactMap { Int($0) }
        .filter { validNumbers[$0] == nil }
        .reduce(0) { $0 + $1 }
}

print(errorRate)
