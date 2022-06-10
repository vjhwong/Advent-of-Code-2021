aoc__day2_file = "AoC/AoC_inputs/aocday2.txt"

with open(aoc__day2_file, "r") as f:
    f_contents = [line.rstrip() for line in f]

commands = [
    tuple([command.split(" ")[0], int(command.split(" ")[1])]) for command in f_contents
]

# Part 1
horizontal_1 = 0
depth_1 = 0

for direction, steps in commands:
    if direction == "forward":
        horizontal_1 += steps
    if direction == "down":
        depth_1 += steps
    if direction == "up":
        depth_1 -= steps

print(horizontal_1)
print(depth_1)
print(horizontal_1 * depth_1)

# Part 2
horizontal_2 = 0
depth_2 = 0
aim = 0

for direction, steps in commands:
    if direction == "down":
        aim += steps
    if direction == "up":
        aim -= steps
    if direction == "forward":
        horizontal_2 += steps
        depth_2 += aim * steps

print(horizontal_2)
print(depth_2)
print(horizontal_2 * depth_2)
