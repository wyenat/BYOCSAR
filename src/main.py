import sys
from parsing.sbparser import Parser

parse = Parser(sys.argv)
comp = parse.get_computer()
comp.read()
