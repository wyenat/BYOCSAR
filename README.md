# BYOCSAR

## About

BYOCSAR stands for
**B**uild **Y**our **O**wn **C**omputer : **S**tack **A**nd **R**egisters
It's basically an n-th way of breaking your skull trying to write easy programs
It is currently under WIP Status.

## Rules

- When executed, a register "consumes" its number, and if it produces any it adds it in the stack, at the top.
- Numbers can overflow : register will ignore any bits outside of the 16 authorized : FF + 01 = 00
- There are a maximum of 15 registers used, labelled from R1 to R15
- Each register can only have one function, and has Noop as default

## Functions

| Name  | Def                                                           | Code  |
| :---: | ------------------------------------------------------------- | :---: |
| Exec  | if not 0, executes the registers                              |   0   |
|  Add  | First 4 bits: Register whos' value will be added. Does NOT    |       |
|       | need to be lower than this register.                          |       |
|       | 0 for the top of the  stack.                                  |       |
|       | Next 4  bits: unsigned value to add                           |       |
| Mult  | First 4 bits: Register whos' value will be multiplied. Does   |   1   |
|       | NOT need to be lower than this register.                      |       |
|       | 0 for the top of the  stack.                                  |       |
|       | Next 4  bits: unsigned value to multiply                      |       |
| Prin  | Prints the ASCII value of the register.                       |   2   |
|  Inv  | Invertes the register and pushes result to the stack          |   3   |
| Push  | Pushes the value to the stack                                 |   4   |
| Inpu  | Stops the execution, wait for input of the user, and pushes   |   5   |
|       | the input to the stack in FIFO order.                         |       |
|       | Expected input are hexa numbers.                              |       |
| PushN | First 4 bits: Index of register to copy-push to the stack     |   6   |
|       | 0 for the top of the  stack, already consumed registered to   |       |
|       | ignore.                                                       |       |
|       | Last  4 bits: Number of time to repeat this operation.        |       |
|  Rev  | Reverses the stack                                            |   7   |
| Skip  | Skip the next value registers, while consuming their value.   |   8   |
|       | If there are not enough registers, will continue into the     |       |
|       | stack.                                                        |       |
|  Mod  | First 4 bits: Register whos' value will be modulo'd           |   9   |
|       | 0 for the top of the  stack.                                  |       |
|       | Next 4 bits: value of the modulo                              |       |
|  Div  | First 4 bits: Register whos' value will be modulo'd           |   A   |
|       | 0 for the top of the  stack.                                  |       |
|       | Next 4 bits: value of the modulo                              |       |
| Noop  | Does not do anything                                          |   B   |
| CopyS | Copies values from the stack, from bottom to top, and pushes. |   C   |

## Configuration

To init the registers, the user should assign functions to them with a Number-Function 16 digits, hexa input
For instance, to assign exec to R2 and print to R1, you can enter: `20 12`
The initialization must come in a single line.

