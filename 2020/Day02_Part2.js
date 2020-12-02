// run this in the browser console itself
document.querySelector("pre").innerText.trim().split("\n")
  .map(l => l.match(/(.+)-(.+) (.): (.*)/))
  .map(m => m[4][m[1]-1] === m[3] ^ m[4][m[2]-1] === m[3])
  .filter(x => x)
  .length;