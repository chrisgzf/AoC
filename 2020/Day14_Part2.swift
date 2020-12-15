import Foundation

func parseLine(_ line: String) -> (String, String) {
    let pattern = (try? NSRegularExpression(pattern: "(.+) = (.+)"))!
    let match = pattern.firstMatch(in: line, options: [], range: NSRange(location: 0, length: line.utf16.count))!
    let op = String(line[Range(match.range(at: 1), in: line)!])
    let param = String(line[Range(match.range(at: 2), in: line)!])
    return (op, param)
}

func parseMemLocation(_ line: String) -> Int {
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

func getDestinationAddresses(_ mask: String, _ n: Int) -> [Int] {
    let binary = getBinary(n)
    let beforeX: [Character] = mask.enumerated().map {
        let (i, c) = $0
        if c == "0" {
            return binary[binary.index(binary.startIndex, offsetBy: i)]
        } else if c == "1" {
            return "1"
        }
        return "X"
    }
    var addresses: [Int] = []

    func generateAddresses(_ accum: inout [Character], _ i: Int) {
        if i >= beforeX.count {
            addresses.append(Int(String(accum), radix: 2)!)
            return
        }
        if beforeX[i] != "X" {
            accum.append(beforeX[i])
            generateAddresses(&accum, i + 1)
            return
        }
        var accum_new = accum
        accum_new.append("0")
        generateAddresses(&accum_new, i + 1)
        accum.append("1")
        generateAddresses(&accum, i + 1)
    }

    var empty_accum: [Character] = []
    generateAddresses(&empty_accum, 0)
    return addresses
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
    let originalLoc = parseMemLocation(op)
    let addresses = getDestinationAddresses(mask, originalLoc)
    addresses.forEach { memory[$0] = Int(param)! }
}

let sum = memory
    .map { $0.1 }
    .reduce(0) { $0 + $1 }

print(sum)
