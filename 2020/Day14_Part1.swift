import Foundation

func parseLine(_ line: String) -> (String, String) {
    let pattern = (try? NSRegularExpression(pattern: "(.+) = (.+)"))!
    let match = pattern.firstMatch(in: line, options: [], range: NSRange(location: 0, length: line.utf16.count))!
    let op = String(line[Range(match.range(at: 1), in: line)!])
    let param = String(line[Range(match.range(at: 2), in: line)!])
    return (op, param)
}

func getMemLocation(_ line: String) -> Int {
    let pattern = (try? NSRegularExpression(pattern: "mem\\[(.+)\\]"))!
    let match = pattern.firstMatch(in: line, options: [], range: NSRange(location: 0, length: line.utf16.count))!
    let location = Int(line[Range(match.range(at: 1), in: line)!])!
    return location
}

func getBinary(_ n: Int) -> String {
    var binaryString = String(n, radix: 2)
    for _ in 0 ..< 36 - binaryString.count {
        binaryString = "0" + binaryString
    }
    return binaryString
}

func applyBitmask(_ mask: String, _ n: Int) -> Int {
    let binary = getBinary(n)
    return Int(String(mask.enumerated().map {
        let (i, c) = $0
        if c == "X" {
            return binary[binary.index(binary.startIndex, offsetBy: i)]
        }
        return c
    }), radix: 2)!
}

var input: [(String, String)] = []
while let line = readLine() {
    input.append(parseLine(line))
}

var mask = ""
var memory: [Int: Int] = [:]

input.forEach {
    let (op, param) = $0
    if op == "mask" {
        mask = param
        return
    }
    let loc = getMemLocation(op)
    memory[loc] = applyBitmask(mask, Int(param)!)
}

let sum = memory
    .map { $0.1 }
    .reduce(0) { $0 + $1 }

print(sum)
