from os import error
from computer.computer import Computer
from computer.functions import mapping, get_register

class Parser:
    def __init__(self, file):
        self.file = open(file).read().split("\n")
        self.computer = Computer()
        self.check()
        self.init_registers()
        self.init_stack()

    """
    It is not so efficient (and coherent with the use of python...) to entirely
    check the code before reading it a second time but :-)
    """
    def check(self):
        # 1 check that there is initialisation
        if len(self.file) < 2:
            raise Exception("Less than 2 lines! You're trying to run an "     +
            "uninitialized computer, or initialize a computer for nothing..." +
            "\nStopping execution.")

        # 2 check that both all data is hexa
        autorized = [hex(i)[2:].zfill(2).upper() for i in range(256)]
        for e,s in enumerate(self.file):
            not_ok = [i for i in s.split() if i not in autorized]
            if not_ok:
                exception_text = f"The line {e+1} is ill-formed. Here is a list:"
                for n,w in enumerate(not_ok):
                    exception_text += f"\nCharacter {n} is {w}"
                raise Exception(exception_text)

    def init_registers(self):
        for i in self.file[0].split():
            print(f"Register {i[0]} with : {i[1]}")
            self.computer.registers[get_register(i)].action = mapping[i[1]]

    def init_stack(self):
        for f in self.file[1:]:
            for i in f.split():
                self.computer.stack.add(i)

    def get_computer(self):
        return self.computer


