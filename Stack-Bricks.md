# Stack-Bricks computer

## Rules


While building a computer, John accidently created a 16-bits stack based computer that works like this:
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
For instance, to assign exec to R2 and print to R1, you can enter: `2012`
The initialization must come in a single line.

## Examples
### Easy print machine
To print "HELLO WORLD!":

#### Code

`20 12`
`01 48 01 45 01 4C 01 4C 01 4F 01 20 01 57 01 47 01 52 01 4C 01 44 01 21`

#### Explanations
`20 12`
R2 : Exec
R1 : Print
`01 48 01 45 ...`
R2 takes 01
R1 takes 48
R2 has a non-0 value, executes all registers
R1 has 48, the ASCII value for "H"
All registers have been executed and consumed.

R2 takes 01
R1 takes 45
R2 has a non-0 value, executes all registers
R1 has 45, the ASCII value for "E"
...


### Slightly more complex but more efficient print machine

#### Code
`50 47 3C 27 12`
`01 01 04 01 48 45 4C 4C 4F 20 57 47 52 4C 44 21 01 01 04 01`

#### Explanation
`50 47 3C 27 12`
R5: Exec
R4: Inv
R3: CopyS
R2: Inv
R1: Print

| R5  | R4  | R3  | R2  | R1  | Stack                                                    | Note                                       |
| --- | --- | --- | --- | --- | -------------------------------------------------------- | ------------------------------------------ |
| 01  | 01  | 04  | 01  | 48  | 45 4C 4C 4F 20 57 47 52 4C 44 21 01 01 04 01             | read the stack                             |
|     | 01  | 04  | 01  | 48  | 45 4C 4C 4F 20 57 47 52 4C 44 21 01 01 04 01             | Executes R5                                |
|     |     | 04  | 01  | 48  | 01 04 01 01 21 44 4c 52 47 57 20 4f 4c 4c 45             | Invert Stack                               |
|     |     |     | 01  | 48  | 01 04 01 01 21 44 4c 52 47 57 20 4f 4c 4c 45 01 04 01 01 | Copy the 04 bottom to the top of the stack |
|     |     |     |     | 48  | 01 01 04 01 45 4C 4C 4F 20 57 47 52 4C 44 21 01 01 04 01 | Invert Stack                               |
|     |     |     |     |     | 01 01 04 01 45 4C 4C 4F 20 57 47 52 4C 44 21 01 01 04 01 | Print 48="H"                               |
| 01  | 01  | 04  | 01  | 45  | 4C 4C 4F 20 57 47 52 4C 44 21 01 01 04 01                | read the stack                             |
...
|    |    |    |    | 21 | 01 01 04 01 |  |
|    |    |    |    |    | 01 01 04 01 | print 21="!" |
|    | 01  | 01 |04 |  01 |            | read the stack |
|    | 01  | 01 |04 |  01 |            | No exec and no more stack to read : end of program |
