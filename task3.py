import math


def main(n, m, z):
    sum = 0
    for c in range(1, m+1):
        for k in range(1, n + 1):
            sum += 33*c - 63*(18*c)**7 - (74*z+k**2+43)**2
    return sum
