# CPU Simulator

A Von Neumann model CPU simulator implemented in Python.  
Supports a custom ISA with arithmetic, comparison, and branch instructions — including a working GCD program.

---

## Project Structure

```
HW1/
├── assembler/
│   ├── assembler.py       # 2-pass assembler: label resolution + instruction parsing
│   └── parser.py          # Tokenizes each line into opcode / operands
├── devices/
│   ├── memory_unit/
│   │   └── memory.py      # Address-based instruction memory
│   ├── processing_unit/
│   │   └── flags.py       # Zero / Negative flag management
│   └── register_unit/
│       ├── ir.py           # Instruction Register (IR)
│       ├── pc.py           # Program Counter (PC)
│       └── register_file.py  # General-purpose registers R0–R9
├── execution/
│   ├── cpu.py             # Fetch–Decode–Execute loop
│   └── loader.py          # Loads instructions into memory
├── isa/
│   └── instruction.py     # Instruction dataclass + Opcode definitions
├── tests/                 # 14 test programs (.txt)
└── main.py                # Runs all test files
```

---

## Getting Started

**Requirements:** Python 3.10+, no external libraries.

```bash
# Run all test cases
python main.py

# Run a single test file
python -c "
from pathlib import Path
from main import run_program
run_program(Path('tests/GCD.txt').read_text())
"
```

---

## ISA (Instruction Set Architecture)

Instruction format: `OPCODE operand1, operand2`

Operand types:
- `R0`–`R9` — register
- integer literal — immediate value (decimal or `0x` hex)
- label name — resolved to address by the assembler

| Category | Instruction | Operation |
|---|---|---|
| Data | `MOV Rd, Src` | Rd ← Src |
| Arithmetic | `ADD Rd, Rs` | R0 ← Rd + Rs |
| | `SUB Rd, Rs` | R0 ← Rd − Rs |
| | `MUL Rd, Rs` | R0 ← Rd × Rs |
| | `DIV Rd, Rs` | R0 ← Rd ÷ Rs (integer); raises error if Rs == 0 |
| Comparison | `CMP Rd, Rs` | Updates Zero / Negative flags from (Rd − Rs) |
| | `C Rd, Rs` | R0 ← 1 if Rd < Rs, else R0 ← 0 |
| Control | `J target` | PC ← target (unconditional jump) |
| | `JZ target` | PC ← target if Zero flag is set |
| | `JN target` | PC ← target if Negative flag is set |
| | `B target` | PC ← target if R0 == 1 |
| Termination | `HALT` | Stop execution, print register state |

---

## Architecture

This simulator follows the Von Neumann model with clearly separated components:

```
         ┌─────────┐    Fetch    ┌──────┐
         │ Memory  │ ──────────► │  IR  │
         └─────────┘             └──────┘
              ▲                      │ Decode / Execute
              │ load                 ▼
         ┌──────────┐         ┌──────────────┐
         │  Loader  │         │     CPU      │
         └──────────┘         │  (cpu.py)    │
                              └──────┬───────┘
             ┌────────────────┬──────┘
             ▼                ▼
        ┌──────────┐     ┌───────┐
        │ Register │     │ Flags │
        │   File   │     │ (Z/N) │
        └──────────┘     └───────┘
              ▲
              │ increment / set
         ┌────┴───┐
         │   PC   │
         └────────┘
```

**Fetch–Decode–Execute cycle:**

1. `PC.get()` → fetch instruction from Memory
2. Load into IR
3. Decode opcode
4. Resolve operands (register lookup or immediate value)
5. Execute → update registers / flags
6. `PC.increment()` or `PC.set(target)` on branch

---

## Example: GCD

```
MOV R1, 12
MOV R2, 8
LOOP:
    CMP R1, R2
    JZ  END
    JN  LESS
    SUB R1, R2
    MOV R1, R0
    J   LOOP
LESS:
    SUB R2, R1
    MOV R2, R0
    J   LOOP
END:
    HALT
```

Output:
```
[PC=0]  Executing: MOV R1, 12
[PC=1]  Executing: MOV R2, 8
[PC=2]  Executing: CMP R1, R2
[PC=3]  Executing: JZ 11
[PC=4]  Executing: JN 8
[PC=5]  Executing: SUB R1, R2       ← 12 - 8 = 4
[PC=6]  Executing: MOV R1, R0
[PC=7]  Executing: J 2
[PC=2]  Executing: CMP R1, R2
[PC=3]  Executing: JZ 11
[PC=4]  Executing: JN 8             ← 4 < 8, branch taken
[PC=8]  Executing: SUB R2, R1       ← 8 - 4 = 4
[PC=9]  Executing: MOV R2, R0
[PC=10] Executing: J 2
[PC=2]  Executing: CMP R1, R2       ← 4 == 4
[PC=3]  Executing: JZ 11            ← Zero flag set, branch taken
[PC=11] Executing: HALT
{'R0': 4, 'R1': 4, 'R2': 4, ...}   ← GCD(12, 8) = 4 ✓
```

---

## Test Cases

| File | Test | Expected |
|---|---|---|
| `ADD.txt` | 3 + 7 | R0 = 10 |
| `MUL.txt` | 6 × 7 | R0 = 42 |
| `DIV.txt` | 20 ÷ 4 | R0 = 5 |
| `DIV_zero.txt` | divide by zero | `Runtime Error: Division by zero` |
| `MOV.txt` | register-to-register copy | R2 = R1 |
| `MUL_DIV_mix.txt` | (8 × 3) ÷ 2 | R0 = 12 |
| `C_true.txt` | 2 < 5 | R0 = 1 |
| `C_false.txt` | 5 >= 2 | R0 = 0 |
| `C_equal.txt` | 5 == 5 | R0 = 0 |
| `B.txt` | branch taken (R0 = 1) | R3 = 1 |
| `B_not_taken.txt` | branch not taken (R0 = 0) | R3 = 9 |
| `JZ.txt` | jump on zero flag | skips MOV R0, 999 |
| `JN.txt` | jump on negative flag | skips MOV R0, 999 |
| `GCD.txt` | GCD(12, 8) | R0 = R1 = R2 = 4 |

All 14 tests pass.

---

## Design Notes

**2-pass assembler** — `assembler.py` makes two passes over the source: first to build a label-to-address table, then to resolve branch targets. This allows forward references (e.g. `JZ END` before `END:` is defined).

**Instruction Register** — IR is introduced as a separate component to structurally separate the Fetch and Execute stages, mirroring how real processors work.

**Branch vs jump** — `J` / `JZ` / `JN` use CPU flags; `C` / `B` use R0 as a condition register. This keeps the control flow model simple and explicit.

**Division result** — All arithmetic results (ADD / SUB / MUL / DIV) are stored in `R0`. Source registers are not modified.

---

## Build Environment

- Python 3.10
- macOS
- No external libraries