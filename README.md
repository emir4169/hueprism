# Documentation
Programs are written as images. Every pixel of an image is an instruction, The instruction type of each pixel is defined by its Blue channel. the image is read from left to right.

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
