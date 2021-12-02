# Advent of code Year 2021 Star 3
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.readlines()

horizontal = 0
depth = 0

for i in range(len(input)):
    dir, unit = input[i].split()
    
    if dir == "forward":
        horizontal += int(unit)
    elif dir == "up":
        depth -= int(unit)
    elif dir == "down":
        depth += int(unit)
    else:
        print("Unknown direction")

res = horizontal * depth

print("Result : " + str(res))