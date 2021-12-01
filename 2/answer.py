# Advent of code Year 2021 Star 2
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.readlines()

sums = []

for i, elem in enumerate(input):
    if i+3 <= len(input):
        sums.append(int(elem))

    for j in range(0, min(i,2)):
        k = i-1-j

        if k < len(sums):
            sums[k] += int(elem)

res = 0

for i, elem in enumerate(sums):
    if i > 0 and sums[i-1] < sums[i]:
        res += 1

print("Result : " + str(res))