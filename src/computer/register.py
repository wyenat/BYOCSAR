from copy import copy


class Register:
    def __init__(self, action, comp):
        self.value = "00"
        self.comp = comp
        self.action = action
        self.name = " - "
        self.next = None
        self.hex_location = 0

    def set_next(self, next):
        self.next = next
        self.next.hex_location = self.hex_location + 1

    def consume(self):
        self.action(self.value, self.comp)
        self.value = "00"
        self.comp.actions.append(self.pretty_print())
        self.comp.pretty_print()

    def get(self, val: int):
        tmp = self.value
        self.value = val
        self.comp.actions.append(self.pretty_read())
        if self.next != None:
            self.next.get(tmp)
        if self.name == "exec" and int(val, 16) != 0:
            self.consume()

    def pretty_print(self):
        return f"R[{self.hex_location}] : Doing {self.name} for value {self.value}"

    def pretty_read(self):
        return f"R[{self.hex_location}] : Getting value {self.value}"