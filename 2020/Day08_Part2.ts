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

// pc stands for program counter (i.e. the current "pointer" in the instructions)
type State = {
  pc: number;
  accum: number;
};

type SupportedOperations = {
  [key: string]: (param: number, state: State) => State;
};

// Implemented as reducers
const operations: SupportedOperations = {
  acc: (param, { pc, accum }) => ({
    pc: ++pc,
    accum: accum + param,
  }),
  jmp: (param, { pc, accum }) => ({
    pc: pc + param,
    accum,
  }),
  nop: (param, { pc, accum }) => ({
    pc: ++pc,
    accum,
  }),
};

const program: Instruction[] = inputFile
  .trim()
  .split("\n")
  .map((line) => {
    const [op, param] = line.split(" ");
    return { op, param: parseInt(param) };
  });

const linesRun = new Set<number>();

const runInstruction = (
  state: State,
  linesRun: Set<number>,
  modified: boolean
) => {
  const { pc, accum } = state;

  // Check for infinite loop
  if (linesRun.has(pc)) {
    return;
  }
  linesRun.add(pc);

  // Check for termination
  if (pc >= program.length) {
    console.log(accum);
    return;
  }

  // Get current line's operator and parameters
  const { op, param } = program[pc];

  // Normal operation if any nop or jmp instructions have already been modified
  if (modified || op === "acc") {
    const nextState = operations[op](param, state);
    runInstruction(nextState, linesRun, modified);
  } else {
    const nextStateNop = operations["nop"](param, state);
    const nextStateJmp = operations["jmp"](param, state);
    // Shallow copy the set
    runInstruction(nextStateNop, new Set(linesRun), op === "jmp");
    runInstruction(nextStateJmp, linesRun, op === "nop");
  }
};

const initialState: State = { pc: 0, accum: 0 };
runInstruction(initialState, new Set(), false);
