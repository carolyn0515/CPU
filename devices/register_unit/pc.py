class ProgramCounter:
    def __init__(self):
        self.pc = 0
    def get(self):
        return self.pc
    def set(self, address):
        self.pc = address
    def increment(self):
        self.pc += 1