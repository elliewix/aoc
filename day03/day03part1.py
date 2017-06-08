# In a valid triangle, the sum of any two sides must be larger than the remaining side.
# For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25

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


for tri in tris:
    print(tri)
    if is_good_tri(tuple(tri)):
        print("good tri")
    else:
        print("bad tri")
        badtris += 1

print(len(tris) - badtris)
