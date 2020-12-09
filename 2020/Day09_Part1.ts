import * as fs from "fs";

// Read input
const data = fs
  .readFileSync("Day09_Input", {
    encoding: "utf8",
    flag: "r",
  })
  .trim()
  .split("\n")
  .map((l) => parseInt(l.trim()));

const findPair = (i: number, target: number): boolean => {
  for (let j = i - 25; j < i; j++) {
    for (let k = i - 25; k < i; k++) {
      if (j === k) {
        continue;
      }
      if (data[j] + data[k] === target) {
        return true;
      }
    }
  }
  return false;
};

for (let i = 25; i < data.length; i++) {
  const currVal = data[i];
  if (!findPair(i, currVal)) {
    console.log(data[i]);
    break;
  }
}
