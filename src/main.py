import sys
from sbparser import Parser

file  = sys.argv[1]
parse = Parser(file)
comp = parse.get_computer()
comp.pretty_print()