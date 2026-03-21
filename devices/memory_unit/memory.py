class Memory:
    def __init__(self, size):
        self.memory = [None] * size

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value