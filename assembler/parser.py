from isa.instruction import Instruction, Opcode

def parse_operand(token: str):
    token = token.strip()
    
    if token.upper().startswith("R") and token[1:].isdigit():
        return token.upper()
    elif token.startswith("0x") or token.startswith("0X"):
        return int(token, 16)
    try:
        return int(token)
    except ValueError:
        return token

def parse_line(line: str):
    line = line.strip()
    if not line: return None

    parts = line.split(maxsplit=1)

    opcode = parts[0].upper()
    if opcode not in Opcode.ALL:
        raise ValueError(f"Invalid opcode: {opcode}")
    if len(parts) == 1:
        return(Instruction(opcode, []))
    
    operand_tokens = parts[1].split(",")
    operands = []
    for token in operand_tokens:
        operands.append(parse_operand(token))

    return Instruction(opcode, operands)
