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

let oneJolt = 0;
let threeJolt = 1;

const getJolts = (n: number): void => {
  if (adapters.has(n + 1)) {
    oneJolt++;
    getJolts(n + 1);
  } else if (adapters.has(n + 3)) {
    threeJolt++;
    getJolts(n + 3);
  }
};

getJolts(0);
console.log(oneJolt * threeJolt);
