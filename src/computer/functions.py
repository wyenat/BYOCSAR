def get_register(value):
    return int("0x" + value[0], 16) - 1


def get_value(value):
    return int("0x" + value[1], 16) % 8


def exec(value: str, computer):
    if int(str(value), 16) != 0:
        computer.execute()


def add(value: str, computer):
    computer.registers[get_register(value)].value = "{:02X}".format(
        int(computer.registers[get_register(value)].value, 16)
        + int(get_value(value), 16)
    )


def mult(value: str, computer):
    computer.registers[get_register(value)].value *= get_value(value)


def prin(value: str, computer):
    computer.toprint += chr(int(value, 16))


def inv(value: str, computer):
    pass


def inpu(value: str, computer):
    pass


def pushN(value: str, computer):
    pass


def rev(value: str, computer):
    if value:
        computer.stack.reverse()


def skip(value: str, computer):
    computer.toskip = value


def mod(value: str, computer):
    computer.registers[get_register(value)].value %= get_value(value)


def div(value: str, computer):
    computer.registers[get_register(value)].value = computer.registers[
        get_register(value)
    ].value // get_value(value)


def noop(value: str, computer):
    pass


def copyS(value: str, computer):
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
