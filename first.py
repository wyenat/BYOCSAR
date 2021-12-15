import sys
from time import sleep
from src.computer import Computer


c = Computer()
c.read("01 04 00 00 00 00 01 01 00 01 04 00 00 00 00 SP 30 00 01 00 00 SP 00 00 00 00 00")
c.print_current_state()
