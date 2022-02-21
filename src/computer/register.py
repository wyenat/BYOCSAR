from copy import copy


class Register:
    def __init__(self, action, comp):
        self.value = 0
        self.comp = comp
        self.action = action
        self.name = " - "
        self.next = None

    def set_next(self, next):
        self.next = next

    def consume(self):
        self.action(self.value, self.comp)
        self.value = 0

    def get(self, val):
        if self.next != None:
            self.next.get(copy(self.value))
        self.value = val
        if self.name == "exec" and val != 0:
            print(f"EXEC REACHED with {val}, dumping state")
            self.comp.pretty_print()
            self.consume()
