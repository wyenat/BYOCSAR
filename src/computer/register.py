from copy import copy


class Register:
    def __init__(self, action, comp):
        self.value = "00"
        self.comp = comp
        self.action = action
        self.name = " - "
        self.next = None

    def set_next(self, next):
        self.next = next

    def consume(self):
        self.action(self.value, self.comp)
        self.value = "00"

    def get(self, val):
        tmp = self.value
        self.value = val
        if self.next != None:
            self.next.get(tmp)
        if self.name == "exec" and int(val, 16) != 0:
            self.consume()
