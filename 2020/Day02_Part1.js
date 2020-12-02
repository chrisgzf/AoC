// run this in the browser console itself
document.querySelector("pre").innerText.trim().split("\n")
  .map(l => l.match(/(.+)-(.+) (.): (.*)/))
  .map(m => {
   // m[1] is the first number, m[2] is second number
   // m[3] is the letter, m[4] is the full string
   const count = (m[4].match(new RegExp(m[3], "g")) || []).length;
   return m[1] > count || count > m[2];
  })
  .filter(x => x)
  .length;
