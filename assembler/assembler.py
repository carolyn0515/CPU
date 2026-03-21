# 여러 줄 문자열 입력
# 줄마다 parse_line 호출
# Instruction list 셍성

# [assemble() → parse_line() → Instruction]

from assembler.parser import parse_line

def assemble(program_text: str):
    lines = program_text.split("\n")
    instructions = []
    for line in lines:
        inst = parse_line(line)
        if inst is not None:
            instructions.append(inst)
    return instructions