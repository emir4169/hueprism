# Documentation
In HuePrism, programs are given as 24-bit images. The values of the red (R), green (G), and blue (B) channels for each pixel, ranging from 0 to 255, make up the opcode and parameters for each instruction in the language. Each pixel is its own instruction, and they are executed in left to right.

R: Input 1

G: Input 2

B: Instruction Type

If R or G is zero then it is replaced with a value from the stack

All undefined functions are simply reserved and will add R and G to the stack.

0: noop

2: Add (Input 1) and (Input 2)

3: Subtract (Input 1) from (Input 2)

4: Divide (Input 1) from (Input 2)

5: Multiply (Input 2) from (Input 1)

6: (Input 1) Modulo (Input 2)

7: Outputs (Input 1) as a number.

10: Outputs (Input 1) as a ASCII character.

176: Outputs "HOW DARE YOU CALL THIS VERY SPECIFIC FUNCTION IN YOUR CODE" 10 times.

250: Skip next instruction if Input 1 is zero.

251: move instruction pointer down

252: move instruction pointer up

253: move instruction pointer left

254: move instruction pointer right

255: end program
