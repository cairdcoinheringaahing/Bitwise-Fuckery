# [Bitwise Fuckery](https://github.com/cairdcoinheringaahing/Bitwise-Fuckery)

Yet another Brainfuck derivative, but slightly more creative


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

In addition to this, the while loops are modified so that the condition depends on the final bit of the tape head.

For example, a parity test would be

    ,[>+<[--]]>.

which can be explained as

    ,            # Take a byte of input;
     [       ]   # While the tape head is even...
      >          #   Move the tape head to the left
       +         #   Increment
        <        #   Move the tape head to the right
         [  ]    #   While the tape head is even...
          --     #     Double decrment (to preserve the bit of the input, and thus the loop)
              >  # Move the tap head to the right
               . # Print as ASCII character