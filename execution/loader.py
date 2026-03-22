def load_program(memory, instructions):
    for address, inst in enumerate(instructions):
        memory.write(address, inst)
