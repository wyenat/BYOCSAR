def get_register(value):
    return int("0x" + value[0], 16) - 1


def get_value(value):
    return int("0x" + value[1], 16) % 8


def exec(value, computer):
    if value:
        computer.execute()


def add(value, computer):
    computer.registers[get_register(value)].value += get_value(value)


def mult(value, computer):
    computer.registers[get_register(value)].value *= get_value(value)


def prin(value, computer):
    computer.toprint += chr(value)


def inv(value, computer):
    pass


def inpu(value, computer):
    pass


def pushN(value, computer):
    pass


def rev(value, computer):
    if value:
        computer.stack.reverse()


def skip(value, computer):
    computer.toskip = value


def mod(value, computer):
    computer.registers[get_register(value)].value %= get_value(value)


def div(value, computer):
    computer.registers[get_register(value)].value = computer.registers[
        get_register(value)
    ].value // get_value(value)


def noop(value, computer):
    pass


def copyS(value, computer):
    pass


mapping = {
    "0": exec,
    "1": add,
    "2": mult,
    "3": prin,
    "4": inv,
    "5": inpu,
    "6": pushN,
    "7": rev,
    "8": skip,
    "9": mod,
    "A": div,
    "B": noop,
    "C": copyS,
}

name_map = {
    "0": "exec",
    "1": "add",
    "2": "mult",
    "3": "prin",
    "4": "inv",
    "5": "inpu",
    "6": "push",
    "7": "rev",
    "8": "skip",
    "9": "mod",
    "A": "div",
    "B": "noop",
    "C": "copy",
}
