

def help_func(n, x):
    for i in x:
        pass


def main(x):
    if x[3] == 1969:
        return 13
    elif x[3] == 2015:
        return 12
    else:
        if x[0] == 'C':
            return 4
        elif x[0] == 'AMPL':
            if x[4] == 'D':
                return 0
            elif x[4] == 'CIRRU':
                if x[2] == 1976:
                    return 1
                elif x[2] == 1962:
                    return 2
                elif x[2] == 2014:
                    return 3
        elif x[0] == 'INI':
            if x[2] == 2014:
                return 11
            elif x[2] == 1976:
                if x[1] == 'OPA':
                    return 5
                elif x[1] == 'MEASON':
                    return 6
                elif x[1] == 'SLASH':
                    return 7
            elif x[2] == 1962:
                if x[1] == 'OPA':
                    return 8
                elif x[1] == 'MEASON':
                    return 9
                elif x[1] == 'SLASH':
                    return 10

print(main(['AMPL', 'MESON', 1962, 1969, 'D']))