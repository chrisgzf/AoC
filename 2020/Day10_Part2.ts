import * as fs from "fs";

// Read input
const adapters = new Set(
  fs
    .readFileSync("Day10_Input", {
      encoding: "utf8",
      flag: "r",
    })
    .trim()
    .split("\n")
    .map((l) => parseInt(l.trim()))
);

const outputJolt = Math.max(...Array.from(adapters)) + 3;

const getJolts = (n: number): number => {
  if (n === outputJolt) {
    return 1;
  }
  if (!adapters.has(n) && n !== 0) {
    return 0;
  }
  return getJolts(n + 1) + getJolts(n + 2) + getJolts(n + 3);
};

console.log(getJolts(0));
