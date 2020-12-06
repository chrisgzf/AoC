import * as fs from "fs";

// Preprocess input
const inputFile = fs.readFileSync("Day06_Input", {
  encoding: "utf8",
  flag: "r",
});

const groups: string[] = [""];

inputFile
  .trim()
  .split("\n")
  .forEach((line) => {
    if (!line) {
      // Add new empty string (i.e. empty group)
      groups.push("");
    } else {
      // Append to last group
      groups[groups.length - 1] += line;
    }
  });

console.log(
  groups.map((x) => new Set(x).size).reduce((acc, curr) => acc + curr)
);
