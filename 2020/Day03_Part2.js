// run this in the browser console itself
const input = document.querySelector("pre").innerText.trim().split("\n");
const yLen = input.length;
const xLen = input[0].length;
const getX = (x) => x % xLen;

[[1,1], [3,1], [5,1], [7,1], [1,2]].map(([dx, dy]) => {
  let count = 0;
  let x = 0;
  let y = 0;

  while (y < yLen) {
    if (input[y].charAt(x) === "#") {
      count++;
    }
    x = getX(x + dx);
    y += dy;
  }
  return count;
}).reduce((acc, curr) => acc * curr, 1);