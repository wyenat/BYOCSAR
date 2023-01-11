from inspect import ArgInfo
from os import error
from verbose.verbose import Verbose
from computer.computer import Computer
from computer.functions import mapping, get_register, name_map
import argparse


class Parser:
    def __init__(self, argv):
        self._define_arguments()
        self.file = open(self.parser.file).read().split("\n")
        self.computer = None
        self.verbose = Verbose(self.parser.verbose, self.parser.time)
        self.check()
        self.init_registers()
        self.init_stack()

    def _define_arguments(self):
        parser = argparse.ArgumentParser(
                    prog = 'BYOCSAR',
                    description = 'Please refer to the readme for more help')
        parser.add_argument('-f', '--file', type=str, required=True, 
              help="sr file to compile. Please refer to README.")
        parser.add_argument('-v','--verbose', action=argparse.BooleanOptionalAction,
              help='Verbose flag. Prints the console to see the result.')
        parser.add_argument('-t','--time', default=0.5, type=float,
        help='If verbose flag is one, defines the speed between frames, in seconds.', nargs='?')
        self.parser = parser.parse_args()


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
        auth_hex = [hex(i)[2:].zfill(2).upper() for i in range(256)]
        auth_ascii = "?! ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for e, s in enumerate(self.file):
            not_ok = [
                i
                for i in s.split()
                if i not in auth_hex and i.upper() not in auth_ascii
            ]
            if not_ok:
                exception_text = f"The line {e+1} is ill-formed. Here is a list:"
                for n, w in enumerate(not_ok):
                    exception_text += f"\nCharacter {n} is {w}"
                raise Exception(exception_text)

    def init_registers(self):
        nb_reg = len(self.file[0].split())
        self.computer = Computer(nb_reg, self.verbose)
        for i in self.file[0].split():
            if i.upper() in "?!ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                i = hex(ord(i.upper()))[2:]
            self.computer.registers[get_register(i)].action = mapping[i[1]]
            self.computer.registers[get_register(i)].name = name_map[i[1]]

    def init_stack(self):
        for f in self.file[1:]:
            for i in f.split():
                if i.upper() in "?!ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    i = hex(ord(i.upper()))[2:]
                self.computer.stack.add(i)

    def get_computer(self):
        return self.computer

