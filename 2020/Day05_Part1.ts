import * as fs from "fs";

// Read input
const input = fs
  .readFileSync("Day05_Input", {
    encoding: "utf8",
    flag: "r",
  })
  .trim()
  .split("\n");

// The row and col parts of the boarding passes are actually binary strings
const answer = input
  .map((boardingPass) =>
    parseInt(
      boardingPass
        .replace(/F/g, "0")
        .replace(/B/g, "1")
        .replace(/L/g, "0")
        .replace(/R/g, "1"),
      2
    )
  )
  .reduce((acc, curr) => (curr > acc ? curr : acc), 0);

console.log(answer);
