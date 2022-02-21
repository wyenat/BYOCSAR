from computer.register import Register
from computer.stack import Stack
from computer.functions import mapping, noop
import sys
import time


class Computer:
    def __init__(self, nb_reg):
        previous = None
        self.registers = []
        for i in range(nb_reg):
            register = Register(noop, self)
            if previous != None:
                previous.set_next(register)
            previous = register
            self.registers.append(register)
        self.toskip = 0
        self.toprint = ""
        self.stack = Stack()

    def read(self):
        while self.stack.stack:
            val = self.stack.read()
            self.registers[0].get(val)
        print(self.toprint)

    def execute(self):
        for e, r in enumerate(self.registers):
            if self.toskip != 0:
                self.toskip -= 1
            else:
                print(f"\nR{e+1} executes {r.value} with {r.name}", file=sys.stderr)
                if r.name != "exec":
                    r.consume()
                else:
                    r.value = 0

    def pretty_print(self):
        print("\n" * 24)
        print(
            "#" * 80 + "\n#" + " " * 32 + "REGISTERS DUMP" + " " * 32 + "#\n" + "#" * 80
        )
        reg_nums = ""
        reg_func = ""
        reg_vals = " "
        for e, r in enumerate(self.registers):
            reg_nums += "R" + "{:02}".format(e + 1) + " |"
            reg_func += r.name.ljust(4, " ") + "|"
            reg_vals += "{:02X}".format(r.value) + " | "
        print(reg_nums + "\n" + reg_func + "\n" + reg_vals)
        print("#" * 80 + "\n#" + " " * 34 + "STACK DUMP" + " " * 34 + "#\n" + "#" * 80)
        print(self.stack)
        time.sleep(1)
