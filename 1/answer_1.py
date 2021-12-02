# Advent of code Year 2021 Star 1
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.readlines()

res = 0

for i in range(1, len(input)):
    if int(input[i-1]) < int(input[i]):
        res += 1

print("Result : " + str(res))