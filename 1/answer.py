# Advent of code Year 2021 Star 1
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.readlines()

res = 0

for i, elem in enumerate(input):
    if i > 0 and int(input[i-1]) < int(input[i]):
        res += 1

print("Result : " + str(res))

for i in range(0,1):
    print(i)