class RegisterFile:
    def __init__(self):
        self.regs = {f"R{i}": 0 for i in range(10)}
    def read(self, name):
        if name not in self.regs:
            raise ValueError(f"Invalid Register: {name}")
        return self.regs[name]
    def write(self, name, value):
        if name not in self.regs:
            raise ValueError(f"Invalid Register: {name}")
        if not isinstance(value, int):
            raise ValueError(f"Register value must be int: {value}")
        self.regs[name] = value
    def dump (self):
        return dict(self.regs)