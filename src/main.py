import sys
from parsing.parser import Parser

parse = Parser(sys.argv)
comp = parse.get_computer()
comp.read()
