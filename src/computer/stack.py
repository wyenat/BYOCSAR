class Stack:
    def __init__(self):
        self.stack = []

    def add(self, val):
        self.stack.append(val)

    def reverse(self):
        self.stack = self.stack[::-1]

    def read(self):
        s = self.stack.pop(0)
        return s

    def __str__(self) -> str:
        return "".join(f"{i} " for i in self.stack)

