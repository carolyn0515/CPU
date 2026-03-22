# 여러 줄 문자열 입력
# 줄마다 parse_line 호출
# Instruction list 셍성

# [assemble() → parse_line() → Instruction]

from assembler.parser import parse_line

def assemble(program_text: str):
    lines = program_text.split("\n")

    # label table 생성
    labels = {}
    instruction_index = 0
    for line in lines:
        stripped = line.strip()

        if not stripped: continue

        if stripped.endswith(":"): 
            label = stripped[:-1]
            labels[label] = instruction_index
            continue
        
        instruction_index += 1

    instructions = []

    for line in lines:
        stripped = line.strip()

        if not stripped or stripped.endswith(":"): continue

        inst = parse_line(stripped)

        if inst.opcode in {"J", "JZ", "JN"}:
            target = inst.operands[0]
            if isinstance(target, str) and target in labels:
                inst.operands[0] = labels[target]
            
        instructions.append(inst)

    return instructions
