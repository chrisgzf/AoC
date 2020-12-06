import * as fs from "fs";

// Preprocess input
const inputFile = fs.readFileSync("Day06_Input", {
  encoding: "utf8",
  flag: "r",
});

const groups: Set<string>[][] = [[]];

inputFile
  .trim()
  .split("\n")
  .forEach((line) => {
    if (!line) {
      // Add new empty group
      groups.push([]);
    } else {
      // Append to last group
      groups[groups.length - 1].push(new Set(line));
    }
  });

/**
 * Returns the set intersection of set x and set y.
 *
 * @param x set X
 * @param y set Y
 * @return set intersection of X and Y
 */
const intersection = (x: Set<string>, y: Set<string>): Set<string> => {
  return new Set(Array.from(x).filter((xx) => y.has(xx)));
};

console.log(
  groups
    .map((group) => group.reduce(intersection).size)
    .reduce((acc, curr) => acc + curr)
);
