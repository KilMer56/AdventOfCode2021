# Advent of code Year 2021 Star 4
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.read().splitlines()

horizontal = 0
aim = 0
depth = 0

for i in range(len(input)):
    dir, unit = input[i].split()
    
    if dir == "forward":
        horizontal += int(unit)
        depth += aim*int(unit)
    elif dir == "up":
        aim -= int(unit)
    elif dir == "down":
        aim += int(unit)
    else:
        print("Unknown direction")

res = horizontal * depth

print("Result : " + str(res))