

def help_func(key, kwargs):
    if type(kwargs[key]) == tuple:
        return help_func(kwargs[key][0], kwargs[key][1])
    else:
        return kwargs[key]


def main(x):
    return help_func(
        x[3],
        {
            2015: 12,
            1969: 13,
            1985: (
                x[0],
                {
                    "C": 4,
                    "AMPL": (
                        x[4],
                        {"D": 0, "CIRRU": (x[2], {1976: 1, 1962: 2, 2014: 3})},
                    ),
                    "INI": (
                        x[2],
                        {
                            2014: 11,
                            1976: (x[1], {"OPA": 5, "MESON": 6, "SLASH": 7}),
                            1962: (x[1], {"OPA": 8, "MESON": 9, "SLASH": 10}),
                        },
                    ),
                },
            ),
        },
    )

print(main(['AMPL', 'MESON', 1962, 1969, 'D']))
print(main(['INI', 'MESON', 1962, 1985, 'D']))
# print(main([123, 'MESON', 1962, 1985, 'D'])) #Test my strategy
# print(main(['AMPL', 'MESON', 1962, 'func', 'D'])) #Test
# tuple1 = (1, 2)
# cort = {1: tuple1, 2: 2}
# print(type(cort[1]) == tuple)
# print(type(cort))