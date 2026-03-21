from isa.instruction import Opcode

class CPU:
    def __init__(self, memory, pc, registers):
        self.memory = memory
        self.pc = pc
        self.registers = registers

    def run(self):
        while True:
            address = self.pc.get()
            instr = self.memory.read(address)

            opcode = instr.opcode
            operands = instr.operands

            if opcode == Opcode.MOV:
                dst = operands[0]
                src = operands[1]
                # todo

            elif opcode == Opcode.ADD:
                dst = operands[0]
                src = operands[1]
                # todo

            elif opcode == Opcode.SUB:
                dst = operands[0]
                src = operands[1]
                # todo

            elif opcode == Opcode.HALT:
                break

            self.pc.increment()