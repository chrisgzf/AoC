import * as fs from "fs";

// Preprocess input
const inputFile = fs.readFileSync("Day07_Input", {
  encoding: "utf8",
  flag: "r",
});

type ContainedColors = {
  [key: string]: number;
};

type Graph = { [key: string]: ContainedColors };

const graph: Graph = {};

// Preprocess rules into a graph
const parseLineToRule = (line: string): void => {
  const [_, mainColor, containedColorsText] = Array.from(
    line.matchAll(/^(.+) bags contain (.+)\.$/)
  )[0];

  const containedColors: ContainedColors = {};

  containedColorsText.split(", ").forEach((text) => {
    const matches = Array.from(text.matchAll(/^(\d+) (.+) bags?$/));
    if (matches.length > 0) {
      const [_, count, color] = matches[0];
      containedColors[color] = parseInt(count);
    }
  });

  graph[mainColor] = containedColors;
};

inputFile.trim().split("\n").forEach(parseLineToRule);

const START_COLOR = "shiny gold";

const visit = (target: string): number => {
  const containedColors = graph[target];
  return (
    1 +
    Object.keys(containedColors)
      .map((neighbour) => containedColors[neighbour] * visit(neighbour))
      .reduce((acc, curr) => acc + curr, 0)
  );
};

console.log(visit(START_COLOR) - 1); // -1 because we don't want to count shiny gold
