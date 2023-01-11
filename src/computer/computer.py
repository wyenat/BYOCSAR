from computer.register import Register
from computer.stack import Stack
from computer.functions import mapping, exec
import time
from verbose.verbose import Verbose

class Computer:
    def __init__(self, nb_reg, verbose: Verbose):
        previous = None
        self.registers = []
        for i in range(nb_reg):
            register = Register(exec, self)
            if previous != None:
                previous.set_next(register)
            previous = register
            self.registers.append(register)
        self.toskip = 0
        self.toprint = ""
        self.actions = []
        self.stack = Stack()
        self.verbose = verbose

    def read(self):
        while self.stack.stack:
            val = self.stack.read()
            self.registers[0].get(val)
            self.pretty_print()
        print(self.toprint)

    def execute(self):
        for e, r in enumerate(self.registers):
            if self.toskip != 0:
                self.toskip -= 1
            else:
                if r.name != "exec":
                    r.consume()
                else:
                    r.value = 0

    def pretty_print(self):
        if not self.verbose.flag:
            return
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
            reg_vals += "{:02X}".format(int(str(r.value), 16)) + " | "
        print(reg_nums + "\n" + reg_func + "\n" + reg_vals)
        print("#" * 80 + "\n#" + " " * 34 + "STACK DUMP" + " " * 34 + "#\n" + "#" * 80)
        print(self.stack)
        print("#" * 80 + "\n#" + " " * 34 + "STDOUT FLU" + " " * 34 + "#\n" + "#" * 80)
        print(self.toprint)
        print("#" * 80 + "\n#" + " " * 34 + "ACTION    " + " " * 34 + "#\n" + "#" * 80)
        while len(self.actions):
            print(self.actions.pop())
        time.sleep(self.verbose.time)
