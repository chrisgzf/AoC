import Foundation

var validNumbers: [Int: Set<String>] = [:]
func parseRule(_ line: String) {
    let pattern = (try?
        NSRegularExpression(pattern: "(.+): (\\d+)-(\\d+) or (\\d+)-(\\d+)"))!
    let match = pattern.firstMatch(in: line, options: [], range:
        NSRange(location: 0, length: line.utf16.count))!
    let name = String(line[Range(match.range(at: 1), in: line)!])
    let a = Int(line[Range(match.range(at: 2), in: line)!])!
    let b = Int(line[Range(match.range(at: 3), in: line)!])!
    let c = Int(line[Range(match.range(at: 4), in: line)!])!
    let d = Int(line[Range(match.range(at: 5), in: line)!])!

    for i in a ... b {
        if validNumbers[i] != nil {
            validNumbers[i]?.insert(name)
        } else {
            validNumbers[i] = Set([name])
        }
    }
    for i in c ... d {
        if validNumbers[i] != nil {
            validNumbers[i]?.insert(name)
        } else {
            validNumbers[i] = Set([name])
        }
    }
}

// Read Rules
while let line = readLine() {
    if line == "" {
        break
    }
    parseRule(line)
}

var tickets: [[Int]] = []

// Read your ticket
_ = readLine()
tickets.append(readLine()!
    .split { $0 == "," }
    .compactMap { Int($0) })
_ = readLine()

// Read nearby tickets
_ = readLine()
var errorRate = 0

while let line = readLine() {
    let ticket = line
        .split { $0 == "," }
        .compactMap { Int($0) }
    let isValid = ticket
        .filter { validNumbers[$0] == nil }
        .count == 0
    if isValid {
        tickets.append(ticket)
    }
}

var foundFields: Set<String> = Set([])
var fields: [String] = []
for _ in 0 ..< tickets[0].count {
    fields.append("")
}

// `found` is a flag that checks if all fields are already found
var found = false
while !found {
    found = true
    for col in 0 ..< tickets[0].count {
        if fields[col] != "" {
            // Skip if already found
            continue
        }
        found = false
        let colAllChoices = tickets.compactMap { validNumbers[$0[col]] }
        let colCandidates = colAllChoices
            .reduce(colAllChoices[0]) { $0.intersection($1) }
            .subtracting(foundFields)

        if colCandidates.count == 1 {
            // narrowed down to one candidate!
            let name = colCandidates.first!
            foundFields.insert(name)
            fields[col] = name
        }
    }
}

var ans = 1
for (i, key) in fields.enumerated() {
    if key.starts(with: "departure") {
        ans *= tickets[0][i]
    }
}

print(ans)
