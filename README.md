
---

# 🧠 CPU Simulator

This project implements a modular CPU simulator that models how fundamental hardware components cooperate to execute instructions.

Rather than implementing instruction execution as a simple sequential program,
this simulator explicitly separates CPU responsibilities into logical hardware-like units:

* Control Unit
* Register Unit
* Memory Unit
* Processing Unit

The simulator focuses on realistic modeling of:

* Instruction cycle stages
* Internal register transfers
* Control signal orchestration
* Memory interaction
* Data path movement

This architecture enables extensibility toward advanced CPU features such as pipeline simulation, interrupt handling, and cache hierarchy modeling.

---

# 📦 Project Structure

```text
HW1/
│
├── assembler/
│
├── devices/
│   ├── control_unit/
│   │   ├── control_unit.py
│   │   ├── state_machine.py
│   │   ├── micro_ops.py
│   │   └── role.md
│   │
│   ├── memory_unit/
│   │   ├── memory.py
│   │   ├── memory_io.py
│   │   ├── mar.py
│   │   ├── mdr.py
│   │   └── role.md
│   │
│   ├── processing_unit/
│   │   ├── alu.py
│   │   ├── flags.py
│   │   ├── temp_register.py
│   │   └── role.md
│   │
│   ├── register_unit/
│   │   ├── pc.py
│   │   ├── ir.py
│   │   ├── sp.py
│   │   ├── gpr.py
│   │   ├── register_file.py
│   │   └── role.md
│
├── execution/
├── isa/
├── programs/
├── tests/
├── main.py
└── README.md
```

---

# 🧩 CPU Architecture Overview

The simulator models a classical CPU architecture where execution is driven by a control unit coordinating register transfers and computation.

Each device module represents a logical hardware component.

---

## 🎛 Control Unit

Controls the entire instruction execution process.

### `control_unit.py`

* Orchestrates instruction cycle
* Determines execution sequence
* Updates Program Counter
* Handles branching, jumping, and HALT

### `state_machine.py`

Defines CPU execution stages:

* FETCH
* DECODE
* OPERAND_FETCH
* EXECUTE
* WRITE_BACK

Controls transition between stages.

### `micro_ops.py`

Defines internal CPU micro-operations such as:

* Instruction fetch sequence
* Register-to-ALU data transfer
* Memory read/write control
* Result write-back

---

## 💾 Memory Unit

Handles storage and CPU–memory communication.

### `memory.py`

* Represents main memory
* Stores instructions and runtime data

### `memory_io.py`

* Provides memory access interface

  * `read(address)`
  * `write(address, value)`

### `mar.py`

* Memory Address Register
* Holds address for memory access

### `mdr.py`

* Memory Data Register
* Temporarily stores data read from or written to memory

---

## 🧮 Processing Unit

Performs arithmetic and logical operations.

### `alu.py`

Implements operations:

* ADD
* SUB
* AND
* OR
* CMP

### `flags.py`

Stores CPU condition flags:

* Zero
* Carry
* Sign
* Overflow

### `temp_register.py`

* Temporary storage for ALU results
* Used before write-back stage

---

## 📚 Register Unit

Maintains CPU internal execution state.

### `pc.py`

* Program Counter
* Holds address of next instruction

### `ir.py`

* Instruction Register
* Stores currently executing instruction

### `sp.py`

* Stack Pointer
* Used for stack-based instructions

### `gpr.py`

* Defines general-purpose registers

### `register_file.py`

* Unified interface for reading/writing general registers

---

# 🧾 Assembler Layer

Located in `assembler/`.

Responsible for:

* Parsing assembly programs
* Resolving labels
* Validating opcode and operand formats
* Generating internal instruction objects

---

# 📐 ISA Layer

Located in `isa/`.

Defines:

* Instruction formats
* Opcode definitions
* Addressing modes
* Operand semantics

The Control Unit relies on ISA definitions during instruction decoding.

---

# ⚙ Execution Engine

Located in `execution/`.

Responsibilities:

* Initialize CPU components
* Run instruction execution loop
* Support micro-step execution
* Provide execution tracing and debugging

---

# 🚀 Entry Point

`main.py` performs:

* Program loading
* CPU initialization
* Execution start
* Final state output

---

# 🔄 Instruction Execution Cycle

The CPU repeatedly executes:

```text
FETCH → DECODE → OPERAND FETCH → EXECUTE → WRITE BACK → REPEAT
```

Execution continues until a HALT instruction is encountered.

---

# ⚡ Detailed Runtime Flow

## 1. Program Load

1. Assembly program is parsed by `assembler/`
2. ISA rules from `isa/` define instruction semantics
3. Instructions are written into memory using:

   * `memory_io.py`
   * `memory.py`

---

## 2. CPU Initialization

Registers and internal components are reset:

* PC initialized to program start
* IR cleared
* SP set to stack base
* GPR reset
* MAR / MDR cleared
* FLAGS reset
* TEMP register cleared
* State machine set to FETCH

---

## 3. FETCH Stage

Files involved:

* `pc.py`
* `mar.py`
* `memory_io.py`
* `memory.py`
* `mdr.py`
* `ir.py`
* `micro_ops.py`

Execution:

```text
MAR ← PC
MDR ← Memory[MAR]
IR ← MDR
PC ← PC + 1
```

---

## 4. DECODE Stage

Files involved:

* `ir.py`
* `control_unit.py`
* `state_machine.py`
* `isa/`

Control Unit determines:

* Opcode type
* Operand structure
* Addressing mode
* Required execution path

---

## 5. OPERAND FETCH Stage

Operands are prepared using:

* `register_file.py`
* `gpr.py`
* `memory_unit` modules (if memory access required)

---

## 6. EXECUTE Stage

Files involved:

* `alu.py`
* `flags.py`
* `temp_register.py`
* `control_unit.py`

Operations performed:

* Arithmetic/logic computation
* Flag updates
* Branch condition evaluation
* Memory access (for LOAD / STORE)

---

## 7. WRITE BACK Stage

Results are committed to:

* Register File
* Memory
* Program Counter

Files involved:

* `register_file.py`
* `memory_io.py`
* `temp_register.py`
* `pc.py`

---

## 8. Next Instruction

`state_machine.py` transitions back to FETCH.
Execution continues until HALT.

---

# 🧠 Example Instruction Lifecycle

Instruction:

```text
ADD R1, R2
```

Execution sequence:

1. Fetch instruction into IR
2. Decode operands
3. Read R1 and R2 from register file
4. ALU computes result
5. Flags updated
6. Result stored in R1
7. Next instruction fetch begins

---

# 🎯 Design Goals

* Explicit modeling of register transfer operations
* Separation of control logic and datapath
* Realistic instruction cycle simulation
* Modular hardware abstraction
* Expandability toward:

  * Stack execution
  * Interrupt handling
  * Pipeline architecture
  * Cache hierarchy modeling

---

# ✅ Conclusion

This CPU simulator demonstrates how independent hardware-like units collaborate to execute instructions.

By modeling control flow, register state transitions, ALU operations, and memory interaction explicitly,
the project provides a structured and extensible framework for CPU architecture simulation.

---