# \[Binaryfuck](https://github.com/SatansSon/Binaryfuck)

Yet another Brainfuck derivative, but slightly more creative

The name of this language is \[Binaryfuck](https://github.com/SatansSon/Binaryfuck), not Binaryfuck, and should be titled appropriately.

This version/derivative adds in 6 new commands to brainfuck, as well as two command line flags, and *a second tape*. Those commands are:

    & - Bitwise AND
    | - Bitwise OR
    ^ - Bitwise XOR
    ~ - Bitwise NOT
    % - Copy the value under the tape head to the second stack
    @ - Swap the values of the tapes, preserving order
    
The flags are:

	-d - Output debug information after each command
	-t - Output both tapes, with trailing zeros stripped, at the end of the program
