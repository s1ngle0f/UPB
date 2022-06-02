import math


def main(n):
    if n == 0:
        return 0.26
    if n == 1:
        return -0.63
    if n >= 2:
        return main(n-2) - math.sin(main(n-1)**2)**2
