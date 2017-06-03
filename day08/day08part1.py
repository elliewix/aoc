import numpy as np
import re
def change(p):
    if p == 0:
        return 1
    else:
        return 0

screen = np.zeros((6, 50))


def rectAB(screen, a, b):
    # print(screen[:a, :b])
    screen[:b, :a] = 1
    # print(screen)
    return screen

def rotate_col(screen, c, n):
    screen[:, c] = np.roll(screen[:, c], n)

def rotate_row(screen, r, n):
    screen[r] = np.roll(screen[r], n)

def count_ons(screen):
    return(sum(sum(screen)))

def print_screen(screen):
    new = ""
    for row in screen:
        new += "".join([str(int(i)).replace("0", ".").replace("1", "#") for i in row])
        new += "\n"
    print(new)

def read_command(screen, line):
    if line.startswith("rect"):
        x, y = re.findall(r'(\d+)x(\d+)', line)[0]
        rectAB(screen, int(x), int(y))
    elif line.startswith("rotate column"):
        col, n = re.findall(r'(\d+) by (\d+)', line)[0]
        rotate_col(screen, int(col), int(n))
    elif line.startswith("rotate row"):
        col, n = re.findall(r'(\d+) by (\d+)', line)[0]
        rotate_row(screen, int(col), int(n))
    else:
        print("I dunno", line)


# rectAB(screen, 3, 2)
# rotate_col(screen, 1, 1)
# rotate_row(screen, 0, 4)
# rotate_col(screen, 1, 1)
# print_screen(screen)
# print(count_ons(screen))

with open('input.txt', 'rt') as fin:
    data = [r.strip() for r in fin.readlines()]

for d in data:
    read_command(screen, d)
    print_screen(screen)

print(count_ons(screen))
