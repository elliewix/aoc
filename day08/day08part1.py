import numpy as np

def change(p):
    if p == 0:
        return 1
    else:
        return 0

screen = np.zeros((3, 7))


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

rectAB(screen, 3, 2)
rotate_col(screen, 1, 1)
rotate_row(screen, 0, 4)
rotate_col(screen, 1, 1)
print_screen(screen)
print(count_ons(screen))
