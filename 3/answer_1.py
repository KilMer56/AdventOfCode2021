# Advent of code Year 2021 Star 5
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.read().splitlines()

gamma = ""
epsilon = ""

length = len(input)

for i in range(len(input[0])):
    count = 0

    for j in range(length):
        count += int(input[j][i])
    
    if count > int(length/2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


res = int(gamma, 2) * int(epsilon, 2)

print("Result : " + str(res))