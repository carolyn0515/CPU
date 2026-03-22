from isa.instruction import Opcode

class CPU:
    def __init__(self, memory, pc, ir, registers, flags):
        self.memory = memory
        self.pc = pc
        self.ir = ir
        self.registers = registers
        self.flags = flags

    def run(self):

        while True:
            address = self.pc.get()
            fetched = self.memory.read(address)
            self.ir.load(fetched)
            instr = self.ir.read()
    
            print(f"[PC={address}] Executing: {instr}")

            opcode = instr.opcode
            operands = instr.operands
        
            if opcode == Opcode.MOV:
                dst = operands[0]
                src = operands[1]
                value = self.resolve_operand(src)
                self.registers.write(dst, value)

            elif opcode == Opcode.ADD:
                op1 = operands[0]
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)
                self.registers.write("R0", v1 + v2)

            elif opcode == Opcode.SUB:
                op1 = operands[0]
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)
                self.registers.write("R0", v1 - v2)

            elif opcode == Opcode.CMP:
                op1 = operands[0]
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)
                result = v1 - v2
                self.flags.update_from_result(result)

            elif opcode == Opcode.JZ:
                target = self.resolve_operand(operands[0])
                if self.flags.zero:
                    self.pc.set(target)
                    continue

            elif opcode == Opcode.JN:
                target = self.resolve_operand(operands[0])
                if self.flags.negative:
                    self.pc.set(target)
                    continue

            elif opcode == Opcode.J:
                target = self.resolve_operand(operands[0])
                self.pc.set(target)
                continue
            
            elif opcode == Opcode.MUL:
                op1 = operands[0]
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)
                self.registers.write("R0", v1 * v2)

            elif opcode == Opcode.DIV:
                op1 = operands[0]
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)

                if v2 == 0:
                    raise ZeroDivisionError("Division by zero")

                self.registers.write("R0", v1 // v2)

            elif opcode == Opcode.C:
                op1 = operands[0]
                op2 = operands[1]
                v1 = self.resolve_operand(op1)
                v2 = self.resolve_operand(op2)

                if v1 < v2:
                    self.registers.write("R0", 1)
                else:
                    self.registers.write("R0", 0)
            
            elif opcode == Opcode.B:
                target = self.resolve_operand(operands[0])
                if self.registers.read("R0") == 1:
                    self.pc.set(target)
                    continue

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