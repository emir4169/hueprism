from PIL import Image
import sys
instruction_pointer = [0, 0]
pointer_direction = [1, 0]
stack = []
def get_rgb_arrays(img):
    width, height = img.size
    r_array = [[0] * width for _ in range(height)]
    g_array = [[0] * width for _ in range(height)]
    b_array = [[0] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            r_array[y][x], g_array[y][x], b_array[y][x] = img.getpixel((x, y))

    return r_array, g_array, b_array
def process_pixel(r, g, b, ip=instruction_pointer, pd=pointer_direction, stack=stack):
    match (b):
        case 2:
            stack.append((r or stack.pop()) + (g or stack.pop()))
        case 3:
            stack.append((r or stack.pop()) - (g or stack.pop()))
        case 4:
            stack.append((r or stack.pop()) / (g or stack.pop()))
        case 5:
            stack.append((r or stack.pop()) * (g or stack.pop()))
        case 6:
            stack.append((r or stack.pop()) % (g or stack.pop()))
        case 7:
            print(r or stack.pop(), end='')
        case 10:
            print(chr(r or stack.pop()), end='')
        case 250:
            if (r or stack.pop()) == 0:
                ip += (pd*2)
        case 251:
            pd = [0, -1]
        case 252:
            pd = [0, 1]
        case 253:
            pd = [-1, 0]
        case 254:
            pd = [1, 0]
        case 255:
            sys.exit(0)
        case _:
            stack.append(r)
            stack.append(g)
    return [ip + pd, pd]
if len(sys.argv) != 2:
    print("R: Input 1 or Variable Value)")
    print("G: Input 2 or Variable Color)")
    print("B: Instruction Type)")
    print()
    print("2: Add (Input 1) and (Input 2)")
    print("3: Subtract (Input 1) from (Input 2)")
    print("4: Divide (Input 1) from (Input 2)")
    print("5: Multiply (Input 2) from (Input 1)")
    print("6: (Input 1) Modulo (Input 2)")
    print("7: Outputs (Input 1) as a number.")
    print("10: Outputs (Input 1) as a ASCII character.")

    print("251: Skip next instruction if Input 1 is zero.")
    print("252: move instruction pointer down")
    print("253: move instruction pointer up")
    print("254: move instruction pointer left")
    print("255: move instruction pointer right")
    print("255: end program")
    print("Anyway, quitting execution because you didn't give me an image.")
    sys.exit(1)
image_path = sys.argv[1]
r_values, g_values, b_values = get_rgb_arrays((Image.open(image_path)))
for y in range(len(r_values)):
    for x in range(len(r_values[y])):
        instruction_pointer, pointer_direction = process_pixel(r_values[y][x], g_values[y][x], b_values[y][x], instruction_pointer, pointer_direction, stack)
