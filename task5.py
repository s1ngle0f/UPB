import math


def main(z, y):
    sum = 0
    for i in range(1, len(z)+1):
        sum += (18*z[math.ceil(i/4)]**3+1+y[len(z)-math.ceil(i/4)]**2)**6
        # sum += (18 * math.ceil(z[i] / 4) ** 3 + 1 + y[len(z) - math.ceil(i / 4)] ** 2) ** 6
    return sum*94
print(main([-0.39, 0.78],
[0.41, -0.61]))