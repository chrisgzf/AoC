// run this in the browser console itself
const input = document.querySelector("pre").innerText.trim().split("\n");
const yLen = input.length;
const xLen = input[0].length;
const getX = (x) => x % xLen;
const dx = 3;
const dy = 1
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

console.log(count);