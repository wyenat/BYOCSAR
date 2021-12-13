"""
Stack computer

While building a computer, John accidently created a 16-bits stack based computer that works like this: 
- Every input is an hexa
- The Exec register execs the stack if it has anything not 00
- The Stack is executed in a FIFE (First in first executed maner), meaning R9-->R8-->...-->R1
- When executed, a register "consumes" its number, and if it produces any it adds it in the stack
- The user has 2 possible inputs : either he pushes a number between 00 and FF, or he pushes SP, a special value that means : push the top of the stack (consumes SP only)
- Numbers starting with F are considered negatives, so range is of each register is [-FF:EF]
- Numbers can overflow : register will ignore any bits outside of the 16 authorized : FF + 01 = 00 
There a 8 registers stacked together, that work like this:
R9  [Exec  ]
R8  [Skip the next R8 registers]
R7  [Push R7 instructions to stack, starting from beginning of the pile if positive, from end of the pile and wrapping if negative]
R6  [print R6 as ASCII]
R5  [Mul R5]
R4  [push to stack]
R3  [Add R2 ]
R2  [push to stack]
R1  [Reverse Buffered stack]

So the simplest way to "print 1+1" on this computer is 
01 04 00 00 00 00 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00

Because : 
Registers :                                      Stack
                   R9 R8 R7 R6 R5 R4 R3 R2 R1  | Buffered stack
Read           :                           01  | 04 00 00 00 00 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :                        01 04  | 00 00 00 00 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :                     01 04 00  | 00 00 00 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :                  01 04 00 00  | 00 00 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :               01 04 00 00 00  | 00 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :            01 04 00 00 00 00  | 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :         01 04 00 00 00 00 01  | 01 01 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :      01 04 00 00 00 00 01 01  | 00  01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
Read           :   01 04 00 00 00 00 01 01 00  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 
R9 executes 01 :      04 00 00 00 00 01 01 00  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00             --> not 0 so execute the whole stack
R8 executes 04 :         00 00 00 00 01 01 00  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00             --> skip the next 4 registers
R7 is skipped  :            00 00 00 01 01 00  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
R6 is skipped  :               00 00 01 01 00  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
R5 is skipped  :                  00 01 01 00  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
R4 is skipped  :                     01 01 00  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00
R3 executes 01 :                        02 01  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00             --> R2 is changed to 01+01=02
R2 executes 02 :                           01  | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 02          --> Push R2 to the stack
R1 executes 00 :                               | 01 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 02          --> 0 so do nothing
Read           :                           01  | 04 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 02
Read           :                        01 04  | 00 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 02
Read           :                     01 04 00  | 00 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 02
Read           :                  01 04 00 00  | 00 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 02
Read           :               01 04 00 00 00  | 00 SP 30 00 01 00 SP 00 00 00 00 00 00 00 02
Read           :            01 04 00 00 00 00  | SP 30 00 01 00 SP 00 00 00 00 00 00 00 02
Read SP        :         01 04 00 00 00 00 02  | 30 00 01 00 SP 00 00 00 00 00 00 00 02
Read           :      01 04 00 00 00 00 02 30  | 00 01 00 SP 00 00 00 00 00 00 00 02
Read           :   01 04 00 00 00 00 02 30 00  | 01 00 SP 00 00 00 00 00 00 00 02
R9 executes 01 :      04 00 00 00 00 02 30 00  | 01 00 SP 00 00 00 00 00 00 00 02
R8 executes 04 :         00 00 00 00 02 30 00  | 01 00 SP 00 00 00 00 00 00 00 02            --> skip the next 4 registers
...
R3 executes 02 :                        32 00  | 01 00 SP 00 00 00 00 00 00 00 02           
R2 executes 32 :                           00  | 01 00 SP 00 00 00 00 00 00 00 02 32
R1 executes 00 :                               | 01 00 SP 00 00 00 00 00 00 00 02 32
Read           :                           01  | 00 SP 00 00 00 00 00 00 00 02 32
Read           :                        01 00  | SP 00 00 00 00 00 00 02 32
Read SP        :                     01 00 32  | 00 00 00 00 00 00 00 02 32
Read           :                  01 00 32 00  | 00 00 00 00 00 02 32
Read           :               01 00 32 00 00  | 00 00 00 00 02 32
Read           :            01 00 32 00 00 00  | 00 00 00 02 32
Read           :         01 00 32 00 00 00 00  | 00 00 02 32
Read           :      01 00 32 00 00 00 00 00  | 00 02 32
Read           :   01 00 32 00 00 00 00 00 00  | 02 32
R9 executes 01 :      00 02 00 00 00 00 00 00  |                                          --> not 0 so execute the whole stack
R8 executes 00 :         02 00 00 00 00 00 00  |                                          --> skip the next 0 registers
R7 executes 32 :            00 00 00 00 00 00  |                                          --> print 32 ---> ASCII FOR 2
...
R1 executes 0  :                               | 02 32 00 00                       


As you can see, print 1+1 is 010400000000010100010400000000SP30000100SP0000000000000000, which is 56 characters long.
A faster method consists in using both R1 and R7 directories, for instance :
01 00 06 
"""

import sys
from time import sleep

class Register: 
    def __init__(self, action, next):
        self.value = 0
        self.action = action
        self.next = next

    def consume(self):
        self.action(self.value)
        self.value = 0
    
    def get(self, val):
        if self.next != None:
            self.next.get(self.value)
        self.value = val

class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self, val):
        self.stack.append(val)

    def reverse(self):
        self.stack = self.stack[::-1]
    
    def read(self):
        s = self.stack.pop(0)
        if s=="SP":
            return self.stack[-1]
        return s

class Computer:
    def __init__(self):
        self.r9 = Register(self.execute, None)
        self.r8 = Register(self.skip, self.r9)
        self.r7 = Register(self.pushR7, self.r8)
        self.r6 = Register(self.print, self.r7)
        self.r5 = Register(self.mult, self.r6)
        self.r4 = Register(self.push, self.r5)
        self.r3 = Register(self.add, self.r4)
        self.r2 = Register(self.push, self.r3)
        self.r1 = Register(self.rev, self.r2)
        self.registers = [self.r9,self.r8,self.r7,self.r6,self.r5,self.r4,self.r3,self.r2,self.r1]
        self.toskip = 0
        self.toprint = ""
        self.stack = Stack()

    def skip(self, val):
        self.toskip = val

    def print(self, val):
        self.toprint += chr(val)

    def mult(self, val):
        self.r4.value *= val

    def add(self, val):
        self.r2.value += val

    def push(self, val):
        self.stack.add(val)

    def rev(self, val):
        if val:
            self.stack.reverse()

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
                print(f"\nR{8-e} executes {r.value}", file=sys.stderr)
                self.print_current_state()
                r.consume()

    def print_current_state(self):
        p = "R9  R8  R7  R6  R5  R4  R3  R2  R1\n"
        for r in self.registers:
            p+= f"{hex(r.value)} "
        print(p, file=sys.stderr)

        print(f"Stack: {self.stack.stack}", file=sys.stderr)

c = Computer()
c.read("01 04 00 00 00 00 01 01 00 01 04 00 00 00 00 SP 30 00 01 00 00 SP 00 00 00 00 00")
c.print_current_state()
