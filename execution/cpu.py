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
                value = self.resolve_operand(src)
                self.registers.write(dst,value)
                

            elif opcode == Opcode.ADD:
                op1 = operands[0]
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)
                self.registers.write("R0", v1+v2)

            elif opcode == Opcode.SUB:
                op1 = operands[0]
            
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)
                self.registers.write("R0", v1-v2)

            elif opcode == Opcode.HALT:
                print(self.registers.dump())
                break

            self.pc.increment()
    
    def resolve_operand(self, operand):
        if isinstance(operand, int):
            return operand
        elif isinstance(operand, str):
            return self.registers.read(operand)
        else:
            raise ValueError(f"Invalid operand: {operand}")