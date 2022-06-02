import math as m


def main(y):
    if y < -32:
        return y**5+44*(17*y**2-y/68-90)**3
    if y >= -32 and y < 60:
        return 25*(84*y-1)**7
    if y >= 60 and y < 100:
        return 65*y**5
    if y >= 100:
        return 42*m.log10(21*y)**7+54*y**3
