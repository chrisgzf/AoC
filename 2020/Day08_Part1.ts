import * as fs from "fs";

// Read input
const inputFile = fs.readFileSync("Day08_Input", {
  encoding: "utf8",
  flag: "r",
});

type Instruction = {
  op: string;
  param: number;
};

type SupportedOperations = {
  [key: string]: (param: number) => void;
};

let pc = 0;
let accum = 0;

const operations: SupportedOperations = {
  acc: (param) => {
    pc++;
    accum += param;
  },
  jmp: (param) => {
    pc += param;
  },
  nop: (param) => {
    pc++;
  },
};

const program: Instruction[] = inputFile
  .trim()
  .split("\n")
  .map((line) => {
    const [op, param] = line.split(" ");
    return { op, param: parseInt(param) };
  });

const linesRun = new Set<number>();

const runInstructionAtLine = (line: number) => {
  linesRun.add(line);
  const { op, param } = program[line];
  operations[op](param);
  if (linesRun.has(pc)) {
    console.log(accum);
    return;
  }
  if (pc >= 0 && pc < program.length) {
    runInstructionAtLine(pc);
  }
};

runInstructionAtLine(pc);
