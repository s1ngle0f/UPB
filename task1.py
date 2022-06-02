import math as m


def main(z, y):
    return (28*z**3 - y**2/80)**3 - (34*(m.asin(y))**3 + m.asin(z**3/18)**4)
