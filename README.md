# Documentation
The direction pointer always starts at the upper-left-most pixel, and always starts facing right.

In HuePrism, programs are given as 24-bit images. The values of the red (R), green (G), and blue (B) channels for each pixel, ranging from 0 to 255, make up the opcode and parameters for each instruction in the language. Each pixel is its own instruction.

R: Input 1

G: Input 2

B: Instruction Type

If R or G is zero then it is replaced with a value from the stack if possible.

All undefined functions are simply reserved and will add R and G to the stack.

0: noop

2: Add (Input 1) and (Input 2)

3: Subtract (Input 1) from (Input 2)

4: Divide (Input 1) from (Input 2)

5: Multiply (Input 2) from (Input 1)

6: (Input 1) Modulo (Input 2)

7: Outputs (Input 1) as a number.

10: Outputs (Input 1) as a ASCII character.

247: Gets a input from the user and adds it to the stack. (The input only supports integers.)

248: Duplicates the first item in the stack.

249: Skips next instruction if (Input 1) is zero.

250: Discards the first item in the stack.

251: changes pointer move direction to be to the down

252: changes pointer move direction to be to the up

253: changes pointer move direction to be to the left

254: changes pointer move direction to be to the right

255: end program

i really need to update this more
