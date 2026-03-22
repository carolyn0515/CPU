from dataclasses import dataclass, field
from typing import List, Union

Operand = Union[str, int]

@dataclass
class Instruction:
    opcode: str
    operands: List[Operand] = field(default_factory=list)
    
    def __post_init__(self):
        self.opcode = self.opcode.upper()

    def __str__(self):
        if not self.operands:
            return self.opcode
        ops = ", ".join(map(str, self.operands))
        return f"{self.opcode} {ops}"

    def __repr__(self):
        return f"Instruction(opcode={self.opcode}, operands={self.operands})"

class Opcode:
    MOV = "MOV"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"

    CMP = "CMP"
    C = "C"

    J = "J"
    JZ = "JZ"
    JN = "JN"
    B = "B"

    HALT = "HALT"

    ALL = {
        MOV, ADD, SUB, MUL, DIV,
        CMP, C,
        J, JZ, JN, B,
        HALT
    }