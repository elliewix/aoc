
def get_num_from_pos(pos):
    return pad[pos[0]][pos[1]]

def move(direct, pos):
    if direct == "U":
        new = pos[0] - 1
        if new in range(5):
            new_pos = (new, pos[1])
            if get_num_from_pos(new_pos) == False:
                print("cannot move up")
                return pos
        else:
            print("cannot move up")
            return pos
    elif direct == "D":
        new = pos[0] + 1
        if new in range(5):
            new_pos = (new, pos[1])
            print(get_num_from_pos(new_pos))
            if get_num_from_pos(new_pos) == False:
                print("cannot move up")
                return pos
        else:
            print("cannot move down")
            return pos
    elif direct == "L":
        new = pos[1] - 1
        if new in range(5):
            new_pos = (pos[0], new)
            if get_num_from_pos(new_pos) == False:
                print("cannot move up")
                return pos
        else:
            print("cannot move left")
            return pos
    elif direct == "R":
        new = pos[1] + 1
        if new in range(5):
            new_pos = (pos[0], new)
            if get_num_from_pos(new_pos) == False:
                print("cannot move up")
                return pos
        else:
            print("cannot move right")
            return pos
    else:
        print("WTF is", direct)

    return new_pos

# def move_down(pos):
#     new_pos = (pos[0] + 1, pos[1])
#     if -1 in new_pos or 3 in new_pos:
#         print("cannot move down")
#         new_pos = pos
#     return new_pos
#
# def move_up(pos):
#     new_pos = (pos[0] - 1, pos[1])
#     if -1 in new_pos  or 3 in new_pos:
#         print("cannot move up")
#         new_pos = pos
#     return new_pos
#
# def move_left(pos):
#     new_pos = (pos[0], pos[1] - 1)
#     if -1 in new_pos  or 3 in new_pos:
#         print("cannot move left")
#         new_pos = pos
#     return new_pos
#
# def move_right(pos):
#     new_pos = (pos[0], pos[1] + 1)
#
#     if -1 in new_pos  or 3 in new_pos:
#         print("cannot move right")
#         new_pos = pos
#     return new_pos

# pad = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]

pad = [[False, False, 1, False, False],
       [False, 2, 3, 4, False],
       [5, 6, 7, 8, 9],
       [False, "A", "B", "C", False],
       [False, False, "D", False, False]]

with open('datapart2.txt', 'rt') as fin:
    text = fin.readlines()
    directions = [list(r.strip()) for r in text]

current_pos = (2, 0)

print("starting at", get_num_from_pos(current_pos))

numbers = []

for row in directions:
    for direct in row:
        current_pos = move(direct, current_pos)
        print(direct, get_num_from_pos(current_pos))

    final_num = get_num_from_pos(current_pos)
    print("finished!, the final number is", final_num)
    numbers.append(final_num)


print(numbers)


