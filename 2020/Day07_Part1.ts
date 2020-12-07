import * as fs from "fs";

// Preprocess input
const inputFile = fs.readFileSync("Day07_Input", {
  encoding: "utf8",
  flag: "r",
});

type Graph = { [key: string]: string[] };

const graph: Graph = {};

// Preprocess rules into a graph
const parseLineToRule = (line: string): void => {
  const [_, mainColor, containedColorsText] = Array.from(
    line.matchAll(/^(.+) bags contain (.+)\.$/)
  )[0];
  containedColorsText.split(", ").forEach((text) => {
    const matches = Array.from(text.matchAll(/^(\d+) (.+) bags?$/));
    if (matches.length > 0) {
      const [_, count, color] = matches[0];
      if (!graph[color]) {
        graph[color] = [mainColor];
      } else {
        graph[color].push(mainColor);
      }
    }
  });
};

inputFile.trim().split("\n").forEach(parseLineToRule);

// Start to find ancestor count of shiny gold

const START_COLOR = "shiny gold";
const visited = new Set<string>();

const visit = (target: string) => {
  visited.add(target);
  graph[target]?.filter((neighbour) => !visited.has(neighbour)).forEach(visit);
};

visit(START_COLOR);
console.log(visited.size - 1); // -1 because we visit shiny gold as well
