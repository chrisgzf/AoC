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

let target = 0;
for (let i = 25; i < data.length; i++) {
  const currVal = data[i];
  if (!findPair(i, currVal)) {
    target = data[i];
    break;
  }
}

for (let i = 0; i < data.length; i++) {
  let sum = 0;
  for (let j = i; j < data.length && sum <= target; j++) {
    sum += data[j];
    if (sum === target) {
      let min = Infinity;
      let max = -1;
      for (let k = i; k < j + 1; k++) {
        min = Math.min(min, data[k]);
        max = Math.max(max, data[k]);
      }
      console.log(min + max);
      process.exit(0);
    }
  }
}
