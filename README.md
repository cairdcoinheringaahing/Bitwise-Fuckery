# [Bitwise Fuckery](https://github.com/cairdcoinheringaahing/Bitwise-Fuckery)

Yet another Brainfuck derivative, but slightly more creative


This version/derivative adds in 6 new commands to brainfuck, as well as two command line flags, and *a second tape*. Those commands are:

    & - Bitwise AND
    | - Bitwise OR
    ^ - Bitwise XOR
    ~ - Bitwise NOT
    % - Copy the value under the tape head to the second tape
    @ - Swap the values of the tapes, preserving order
    
The flags are:

	-d - Output debug information after each command
	-t - Output both tapes, with trailing zeros stripped, at the end of the program

In addition to this, the while loops are modified so that the condition depends on the final bit of the tape head.


## Examples

### Hello, World!, 260 bytes

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.%++++++++++++++++++++++++++++++++++++++++++++.------------.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.%.+++.------.--------.^%^&+.+
    
### Parity Test, 5 + 3 = 8 bytes

A good demonstration of the power of bitwise commands

    ,%+&.
    
Uses the `-n` flag to allow for numerical output
    
How it works, with `d` (100) as an example input

    ,     - Take a byte of input; TAPES = [100] [0]
     %    - Swap tapes;           TAPES = [0] [100]
      +   - Increment;            TAPES = [1] [100]
       &  - Bitwise AND;          TAPES = [0] [100]
        . - Output;               OUTPUTS 0
