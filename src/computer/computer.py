from computer.register import Register
from computer.stack import Stack
from computer.functions import mapping, noop
import sys

class Computer:
    def __init__(self):
        previous = None
        self.registers = []
        for i in range(16):
            register = Register(noop, previous)
            previous = register
            self.registers.append(register)
        self.toskip = 0
        self.toprint = ""
        self.stack = Stack()


    def read(self, val):
        for v in val.split(" "):
            if v=="SP":
                self.stack.add(v)
            else:
                self.stack.add(int(v, 16))
        while len(self.stack.stack):
            self.r1.get(self.stack.read())
            if self.r9.value !=0:
                self.r9.consume()
        print(self.toprint)

    def pushR7(self, val):
        if val>0:
            i = 0
            while val >0:
                self.stack.add(self.stack.stack[i])
                i+=1
                val-=1
        elif val < 0:
            i = len(self.stack.stack) -1
            while val < 0:
                val+=1
                self.stack.add(self.stack.stack[i])
                if (i<0):
                    i = len(self.stack.stack) -1

    def execute(self, val):
        for e, r in enumerate(self.registers[1:]):
            if self.toskip != 0:
                self.toskip -= 1
            else:
                print(f"\nR{16-e} executes {r.value}", file=sys.stderr)
                r.consume()

    def pretty_print(self):
        for e,r in enumerate(self.registers):
            print(f"R{16-e}:{r.value}",file=sys.stderr)
