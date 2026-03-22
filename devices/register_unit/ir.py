class InstructionRegister:
    def __init__(self):
        self.instruction = None

    def load(self, instruction):
        self.instruction = instruction

    def read(self):
        return self.instruction