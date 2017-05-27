# In a valid triangle, the sum of any two sides must be larger than the remaining side.
# For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25

import itertools

with open('triangles.txt', 'rt') as fin:
    tris = [list(map(int, l.split())) for l in fin.readlines()]

badtris = 0

def is_good_tri(tri):
    a, b, c = tri
    if (a + b) <= c:
        return False
    elif (a + c) <= b:
        return False
    elif (b + c) <= a:
        return False
    else:
        return True

start_slices = list(range(0, len(tris), 3))
end_slices = start_slices[1:] + [len(tris)]

slices = list(zip(start_slices, end_slices))

alltris = []

for start, stop in slices:
    chunk = tris[start:stop]
    tri1 = [r[0] for r in chunk]
    tri2 = [r[1] for r in chunk]
    tri3 = [r[2] for r in chunk]
    alltris += [tri1, tri2, tri3]


print(alltris)


for tri in alltris:
    # print(tri)
    if is_good_tri(tuple(tri)):
        print("good tri")
    else:
        print("bad tri")
        badtris += 1

print(len(tris) - badtris)
