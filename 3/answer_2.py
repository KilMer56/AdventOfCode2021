# Advent of code Year 2021 Star 6
# Author : Killian Mer

with open("input.txt", "r") as fp:
    input = fp.read().splitlines()

def get_metric(i, elements, isOxygen):
    if len(elements) == 1: # End result if only 1 element
        return int(elements[0], 2)

    a = []
    b = []

    for j in range(len(elements)):
        if int(elements[j][i]) == 1:
            a.append(elements[j])
        else:
            b.append(elements[j])
    
    i += 1

    if i == 1: # If it is the beginning
        if len(a) >= len(b):
            return get_metric(i, a, True) * get_metric(i, b, False)
        else :
            return get_metric(i, b, True) * get_metric(i, a, False)

    if (len(a) == len(b) and isOxygen) or ((len(a) >= len(b)) == isOxygen): # If counts are equal or different
        return get_metric(i, a, isOxygen)
    else:
        return get_metric(i, b, isOxygen)


res = get_metric(0, input, None)

print("Result : " + str(res))