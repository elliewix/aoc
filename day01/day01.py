import turtle

#   N
# W   E
#   S

with open('data.txt', 'rt') as fin:
	steps_raw = fin.read()

steps = steps_raw.split(", ")

directions = {"N": {"L": "W", "R": "E"},
			  "E": {"L": "N", "R": "S"},
			  "S": {"L": "E", "R": "W"},
			  "W": {"L": "S", "R": "N"}}

current_direction = "N"
current_position = {"x": 0, "y": 0}
#
# N: plus to Y
# S: minus to Y
# E: plus to X
# W: minus to X

# import turtle               # allows us to use the turtles library
# wn = turtle.Screen()        # creates a graphics window
# t = turtle.Turtle()
# t.penup()
# t.setpos(-200, -200)
# t.pendown()
# wn.screensize(200,200)

seen = []

seen_twice = []
for step in steps:
	# print(seen)
	turn = step[0]
	# if turn == "L":
	# 	t.left(90)
	# elif turn == "R":
	# 	t.right(90)
    #
	new_direction = directions[current_direction][turn]
	print(step, current_direction, new_direction)
	current_direction = new_direction
	num = int(step[1:])


	# t.forward(num * 2)
	for step in range(1, num + 1):
		if current_direction == "N":
			current_position["y"] += 1
		elif current_direction == "S":
			current_position["y"] -= 1
		elif current_direction == "E":
			current_position["x"] += 1
		elif current_direction == "W":
			current_position["x"] -= 1

		pos = (current_position["x"], current_position["y"])
		if pos in seen:
			print("Saw this again!", pos)
			seen_twice.append(pos)
		else:
			seen.append(pos)



# turtle.done()

print(current_position)

print(seen_twice[0])



# calculate the distance betwee 0,0 and current position

distance = abs(current_position["x"] - 0) + abs(current_position["y"] - 0)

first_seen_twice_dist = abs(seen_twice[0][0] - 0) + abs(seen_twice[0][1] - 0)

print(distance)
print(first_seen_twice_dist)


