import * as fs from "fs";

type Pair = {
  key: string;
  val: string;
};

type Passport = Pair[];

// Preprocess input
const inputFile = fs.readFileSync("Day04_Input", {
  encoding: "utf8",
  flag: "r",
});

const passports: Passport[] = [[]];

inputFile
  .trim()
  .split("\n")
  .forEach((line) => {
    if (!line) {
      // Add new empty passport
      passports.push([]);
    } else {
      // Extract all key-value pairs
      const allPairs = line.split(" ").map((kvPair) => kvPair.split(":"));
      allPairs.forEach(([key, val]) =>
        passports[passports.length - 1].push({ key, val })
      );
    }
  });

// Check each passport for required keys
const required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

const answer = passports
  .map(
    (passport) =>
      required
        .map(
          (requiredKey) =>
            // true if required key is not found
            passport.filter((pair) => pair.key === requiredKey).length === 0
        )
        // true if passport doesn't have >= 1 required key
        .filter((x) => x).length > 0
  )
  // filter for false (i.e. correct passports)
  .filter((x) => !x).length;

console.log(answer);
