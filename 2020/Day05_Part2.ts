import * as fs from "fs";

// Read input
const input = fs
  .readFileSync("Day05_Input", {
    encoding: "utf8",
    flag: "r",
  })
  .trim()
  .split("\n");

const seenBoardingPasses = new Set();

input.forEach((boardingPass) =>
  seenBoardingPasses.add(
    parseInt(
      boardingPass
        .replace(/F/g, "0")
        .replace(/B/g, "1")
        .replace(/L/g, "0")
        .replace(/R/g, "1"),
      2
    )
  )
);

for (let i = 0; i < 1 << 10; i++) {
  // short circuiting order is important here for efficiency
  if (
    !seenBoardingPasses.has(i) &&
    seenBoardingPasses.has(i - 1) &&
    seenBoardingPasses.has(i + 1)
  ) {
    console.log(i);
    break;
  }
}
