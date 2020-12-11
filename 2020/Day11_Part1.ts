import * as fs from "fs";

// Read input
let seats: string[][] = <string[][]>fs
  .readFileSync("Day11_Input", {
    encoding: "utf8",
    flag: "r",
  })
  .trim()
  .split("\n")
  .map((x) => Array.from(x));

const nRows = seats.length;
const nCols = seats[0].length;

const directions = [
  [0, -1],
  [0, 1],
  [-1, 0],
  [1, 0],
  [1, 1],
  [1, -1],
  [-1, -1],
  [-1, 1],
];

const isOccupied = (seats: string[][], y: number, x: number): boolean => {
  if (y < 0 || x < 0 || y >= nRows || x >= nCols) {
    return false;
  }
  const curr = seats[y][x];
  if (curr === "#") {
    return true;
  }
  return false;
};

function generateNextIteration(): boolean {
  let changed = false;
  const nextSeats = new Array(nRows)
    .fill(null)
    .map((_) => new Array(nCols).fill(null));

  for (let i = 0; i < nRows; i++) {
    for (let j = 0; j < nCols; j++) {
      const curr = seats[i][j];
      const numAdjacentOccupied = directions
        .map(([dx, dy]) => isOccupied(seats, i + dy, j + dx))
        .filter((x) => x).length;

      const noAdjacentOccupied = numAdjacentOccupied === 0;
      const fourOrMoreOccupied = numAdjacentOccupied >= 4;

      if (curr === "L" && noAdjacentOccupied) {
        nextSeats[i][j] = "#";
        changed = true;
      } else if (curr === "#" && fourOrMoreOccupied) {
        nextSeats[i][j] = "L";
        changed = true;
      } else {
        nextSeats[i][j] = curr;
      }
    }
  }
  seats = nextSeats;

  return changed;
}

while (generateNextIteration()) {
  // seats.map((x) => x.join("")).forEach((x) => console.log(x));
  // console.log("");
}

const ans = seats
  .map((row) => row.filter((x) => x === "#").length)
  .reduce((acc, cur) => acc + cur);

console.log(ans);
