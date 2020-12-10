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

// dp[i] is the number of ways to get to outputJolt from i
const dp: number[] = [];

// only 1 way to get to outputJolt from outputJolt
dp[outputJolt] = 1;

for (let i = outputJolt - 1; i >= 0; i--) {
  if (adapters.has(i) || i === 0) {
    const next_1 = dp[i + 1] ? dp[i + 1] : 0;
    const next_2 = dp[i + 2] ? dp[i + 2] : 0;
    const next_3 = dp[i + 3] ? dp[i + 3] : 0;
    dp[i] = next_1 + next_2 + next_3;
  }
}

console.log(dp[0]);
