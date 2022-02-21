from inspect import ArgInfo
from os import error
from computer.computer import Computer
from computer.functions import mapping, get_register, name_map


class Parser:
    def __init__(self, argv):
        if len(argv) <= 1:
            raise Exception(
                "You did not entered enough argument. Please enter a .sr file."
            )
        self.file = open(argv[1]).read().split("\n")
        self.computer = None
        self.verbose = False
        if "-v" in argv:
            self.verbose = True
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
            raise Exception(
                "Less than 2 lines! You're trying to run an "
                + "uninitialized computer, or initialize a computer for nothing..."
                + "\nStopping execution."
            )

        # 2 check that both all data is hexa
        autorized = [hex(i)[2:].zfill(2).upper() for i in range(256)]
        for e, s in enumerate(self.file):
            not_ok = [i for i in s.split() if i not in autorized]
            if not_ok:
                exception_text = f"The line {e+1} is ill-formed. Here is a list:"
                for n, w in enumerate(not_ok):
                    exception_text += f"\nCharacter {n} is {w}"
                raise Exception(exception_text)

    def init_registers(self):
        nb_reg = len(self.file[0].split())
        self.computer = Computer(nb_reg, self.verbose)
        for i in self.file[0].split():
            self.computer.registers[get_register(i)].action = mapping[i[1]]
            self.computer.registers[get_register(i)].name = name_map[i[1]]

    def init_stack(self):
        for f in self.file[1:]:
            for i in f.split():
                self.computer.stack.add(i)

    def get_computer(self):
        return self.computer

