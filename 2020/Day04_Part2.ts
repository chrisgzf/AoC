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

const inRange = (x: string, lo: number, hi: number): boolean => {
  const num = parseInt(x);
  return lo <= num && num <= hi;
};

const isValidHgt = (x: string): boolean => {
  const matches = Array.from(x.matchAll(/(.+)(cm|in)/g));
  if (matches.length === 0) {
    return false;
  }
  const [_, num, unit]: [string, string, string] = <[string, string, string]>(
    matches[0]
  );
  if (unit === "cm") {
    return inRange(num, 150, 193);
  } else {
    return inRange(num, 59, 76);
  }
};

interface ValidationMap {
  [key: string]: (x: string) => boolean;
}

// Check each passport for required keys
const required: ValidationMap = {
  byr: (x) => inRange(x, 1920, 2002),
  iyr: (x) => inRange(x, 2010, 2020),
  eyr: (x) => inRange(x, 2020, 2030),
  hgt: isValidHgt,
  hcl: (x) => /^#(?:[0-9]|[a-f]){6}$/.test(x),
  ecl: (x) => /^amb|blu|brn|gry|grn|hzl|oth$/.test(x),
  pid: (x) => /^\d{9}$/.test(x),
};

const answer = passports
  .map(
    (passport) =>
      Object.keys(required)
        .map((requiredKey) =>
          // true if required key is validated as correct
          {
            const val = passport.filter((pair) => pair.key === requiredKey)[0]
              ?.val;
            if (!val) {
              return false;
            }
            return required[requiredKey](val);
          }
        )
        // true if passport has any invalid keys
        .filter((x) => !x).length > 0
  )
  // filter for false (i.e. correct passports)
  .filter((x) => !x).length;

console.log(answer);
