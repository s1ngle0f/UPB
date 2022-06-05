def main(res):
    f = {
        3: {
            'JSX': {
                4: {
                    'PUG': {
                        1: {
                            'ALLOY': 0,
                            'QMAKE': 1,
                            'HCL': {
                                2: {
                                    'STATA': 2,
                                    'ALLOY': 3
                                }
                            }
                        }
                    },
                    'OOC': 4,
                    'MESON': 5,
                }
            },
            'MUF': {
                4: {
                    'PUG': {
                        1: {
                            'ALLOY': {
                                2: {
                                    'STATA': 6,
                                    'ALLOY': 7
                                }
                            },
                            'QMAKE': 8,
                            'HCL': {
                                0: {
                                    'CMAKE': 9,
                                    'SAGE': 10
                                }
                            }
                        }
                    },
                    'OOC': 11,
                    'MESON': 12,
                }
            },
            'IDL': 13
        }
    }

    while isinstance(f, dict):
        index = int(*f)
        f = f[index]
        key = res[index]
        f = f[key]

    return f