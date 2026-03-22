# assembly text (문자열)
#    ↓
# assembler/parser.py
#    ↓
# Instruction 객체 생성
#    ↓
# isa/instruction.py (객체 구조 정의)
#    ↓
# CPU 실행

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
    HALT = "HALT"
    ALL = {MOV, ADD, SUB, HALT}