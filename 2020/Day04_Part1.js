// run this in the browser console itself
const required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

document
  .querySelector("pre")
  .innerText.trim()
  .split("\n")
  .reduce((acc, l) => `${acc}${l ? l : "\n"}`)
  .split("\n")
  .map((l) => Array.from(l.matchAll(/(.{3}):/g)).map((x) => x[1]))
  .map((l) => required.map((r) => l.includes(r)).filter((x) => !x))
  .filter((l) => l.length === 0).length;
