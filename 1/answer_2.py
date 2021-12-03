# Advent of code Year 2021 Star 2
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.read().splitlines()

res = 0

for i in range(len(input)-3):
    sum1 = 0
    sum2 = 0

    for j in range(3):
        sum1 += int(input[i+j])
        sum2 += int(input[i+j+1])

    if sum1 < sum2:
        res += 1

print("Result : " + str(res))