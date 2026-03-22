
---

# HW1 CPU Simulator

## 1. Overview

This project implements a simple CPU simulator based on the Von Neumann model.
It supports arithmetic operations, data movement, comparison, branching, and program termination.
The simulator reads assembly-like programs, assembles them into internal instructions, loads them into memory, and executes them step by step.

The simulator includes the following architectural components:

* Memory
* Program Counter (PC)
* Instruction Register (IR)
* Register File (`R0`–`R9`)
* Flags
* CPU
* Assembler
* Loader

---

## 2. Project Structure

```text
HW1/
├── assembler/
│   ├── assembler.py
│   └── parser.py
├── devices/
│   ├── memory_unit/
│   │   └── memory.py
│   ├── processing_unit/
│   │   └── flags.py
│   └── register_unit/
│       ├── ir.py
│       ├── pc.py
│       └── register_file.py
├── execution/
│   ├── cpu.py
│   └── loader.py
├── isa/
│   └── instruction.py
├── tests/
│   ├── ADD.txt
│   ├── B.txt
│   ├── B_not_taken.txt
│   ├── C_equal.txt
│   ├── C_false.txt
│   ├── C_true.txt
│   ├── DIV.txt
│   ├── DIV_zero.txt
│   ├── GCD.txt
│   ├── JN.txt
│   ├── JZ.txt
│   ├── MOV.txt
│   ├── MUL.txt
│   └── MUL_DIV_mix.txt
├── main.py
└── README.md
```

---

## 3. Execution Flow

The simulator works in the following order:

1. Read program text
2. Parse each line into an `Instruction`
3. Resolve labels into instruction addresses
4. Load instructions into memory
5. Fetch the current instruction using PC
6. Store the fetched instruction in IR
7. Decode and execute the instruction
8. Update registers, flags, or PC
9. Stop at `HALT`

---

## 4. Supported Instructions

### Arithmetic and Data Movement

* `MOV dst, src`
* `ADD op1, op2` → `R0 = op1 + op2`
* `SUB op1, op2` → `R0 = op1 - op2`
* `MUL op1, op2` → `R0 = op1 * op2`
* `DIV op1, op2` → `R0 = op1 // op2`
* `HALT`

### Slide-Based Comparison and Branch

* `C op1, op2`

  * `R0 = 1` if `op1 < op2`
  * otherwise `R0 = 0`
* `B target`

  * branch only if `R0 == 1`

### Extended Instructions

* `CMP op1, op2`

  * updates `zero` and `negative` flags from `op1 - op2`
* `J target`
* `JZ target`
* `JN target`

---

## 5. Key Design Points

* The simulator explicitly implements both **PC** and **IR** to reflect the Von Neumann model more clearly.
* Arithmetic results are stored in `R0`.
* `C` and `B` follow the slide semantics directly.
* `CMP`, `J`, `JZ`, and `JN` were additionally implemented as extended control-flow instructions.
* The assembler supports label resolution for `J`, `JZ`, `JN`, and `B`.

---

## 6. Error Handling

Division by zero is handled gracefully.

Example:

```text
MOV R1, 10
MOV R2, 0
DIV R1, R2
HALT
```

Output:

```text
Runtime Error: Division by zero
```

---

## 7. Test Programs

The `tests/` directory contains programs for each major function:

* Arithmetic: `ADD.txt`, `MUL.txt`, `DIV.txt`, `DIV_zero.txt`, `MUL_DIV_mix.txt`
* Data movement: `MOV.txt`
* `C/B` semantics: `C_true.txt`, `C_false.txt`, `C_equal.txt`, `B.txt`, `B_not_taken.txt`
* Extended branch instructions: `JN.txt`, `JZ.txt`
* Full program example: `GCD.txt`

---

## 8. Example Output

### Example 1: `ADD.txt`

Program:

```text
MOV R1, 3
MOV R2, 7
ADD R1, R2
HALT
```

Output:

```text
[PC=0] Executing: MOV R1, 3
[PC=1] Executing: MOV R2, 7
[PC=2] Executing: ADD R1, R2
[PC=3] Executing: HALT
{'R0': 10, 'R1': 3, 'R2': 7, 'R3': 0, 'R4': 0, 'R5': 0, 'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0}
```

### Example 2: `B.txt`

Program:

```text
MOV R1, 1
MOV R2, 3
C R1, R2
B 6
MOV R3, 0
J 7
MOV R3, 1
HALT
```

Output:

```text
[PC=0] Executing: MOV R1, 1
[PC=1] Executing: MOV R2, 3
[PC=2] Executing: C R1, R2
[PC=3] Executing: B 6
[PC=6] Executing: MOV R3, 1
[PC=7] Executing: HALT
{'R0': 1, 'R1': 1, 'R2': 3, 'R3': 1, 'R4': 0, 'R5': 0, 'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0}
```

### Example 3: `GCD.txt`

Output:

```text
[PC=0] Executing: MOV R1, 12
[PC=1] Executing: MOV R2, 8
[PC=2] Executing: CMP R1, R2
[PC=3] Executing: JZ 11
[PC=4] Executing: JN 8
[PC=5] Executing: SUB R1, R2
[PC=6] Executing: MOV R1, R0
[PC=7] Executing: J 2
...
[PC=11] Executing: HALT
{'R0': 4, 'R1': 4, 'R2': 4, 'R3': 0, 'R4': 0, 'R5': 0, 'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0}
```

---

## 9. How to Run

Run the simulator with:

```bash
python main.py
```

The program automatically executes all test files in the `tests/` directory.

---

## 10. Summary

This project implements a modular CPU simulator with:

* explicit memory, PC, and IR
* assembler and loader
* arithmetic and movement instructions
* slide-based comparison and branch (`C`, `B`)
* extended control-flow instructions (`CMP`, `J`, `JZ`, `JN`)
* label-based jumps
* graceful runtime error handling
* step-by-step execution trace output

---