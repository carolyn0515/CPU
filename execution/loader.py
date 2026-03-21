# assembler가 만든 Instruction list를 memory에 올리는 역할
# program_text
# → assemble()
# → [Instruction, Instruction, ...]
# → load_program(memory, instructions)
# → memory[0], memory[1], ...

def load_program(memory, instructions):
    for address, inst in enumerate(instructions):
        memory.write(address, inst)
