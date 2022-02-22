def get_register(value):
    return int("0x" + value[0], 16) - 1


def get_value(value):
    return int("0x" + value[1], 16) % 8


def exec(value: str, computer):
    if int(str(value), 16) != 0:
        computer.execute()


def add(value: str, computer):
    change_place = get_register(value)
    if change_place == -1:
        computer.stack.stack[-1] = "{:02X}".format(
            int(str(computer.stack.stack[-1]), 16) + get_value(value)
        )
    else:
        computer.registers[get_register(value)].value = "{:02X}".format(
            int(str(computer.registers[get_register(value)].value), 16)
            + get_value(value)
        )


def mult(value: str, computer):
    change_place = get_register(value)
    if change_place == -1:
        computer.stack.stack[-1] = "{:02X}".format(
            int(str(computer.stack.stack[-1]), 16) * get_value(value)
        )
    else:
        computer.registers[get_register(value)].value = "{:02X}".format(
            int(str(computer.registers[get_register(value)].value), 16)
            * get_value(value)
        )


def mod(value: str, computer):
    change_place = get_register(value)
    if change_place == -1:
        computer.stack.stack[-1] = "{:02X}".format(
            int(str(computer.stack.stack[-1]), 16) % get_value(value)
        )
    else:
        computer.registers[get_register(value)].value = "{:02X}".format(
            int(str(computer.registers[get_register(value)].value), 16)
            % get_value(value)
        )


def div(value: str, computer):
    change_place = get_register(value)
    if change_place == -1:
        computer.stack.stack[-1] = "{:02X}".format(
            int(str(computer.stack.stack[-1]), 16) // get_value(value)
        )
    else:
        computer.registers[get_register(value)].value = "{:02X}".format(
            int(str(computer.registers[get_register(value)].value), 16)
            // get_value(value)
        )


def prin(value: str, computer):
    computer.toprint += chr(int(value, 16))


def inpu(value: str, computer):
    pass


def pushN(value: str, computer):
    change_place = get_register(value)
    change_rep = get_value(value)
    if change_place == -1:
        change_val = computer.stack.stack[0:change_rep]
    else:
        change_val = [computer.registers[change_place].value for _ in range(change_rep)]
    for v in change_val:
        computer.stack.add(v)


def rev(value: str, computer):
    if value:
        computer.stack.reverse()


def skip(value: str, computer):
    computer.toskip = value


def copyS(value: str, computer):
    computer.stack.stack += computer.stack.stack[: int(value, 16)]


mapping = {
    "0": exec,
    "1": add,
    "2": mult,
    "3": prin,
    "5": inpu,
    "6": pushN,
    "7": rev,
    "8": skip,
    "9": mod,
    "A": div,
}

name_map = {
    "0": "exec",
    "1": "add",
    "2": "mult",
    "3": "prin",
    "5": "inpu",
    "6": "push",
    "7": "rev",
    "8": "skip",
    "9": "mod",
    "A": "div",
}
