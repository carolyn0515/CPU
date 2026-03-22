class Flags:
    def __init__(self):
        self.zero = False
        self.negative = False

    def reset(self):
        self.zero = False
        self.negative = False

    def update_from_result(self, result):
        self.reset()
        if result == 0:
            self.zero = True
        elif result < 0:
            self.negative = True