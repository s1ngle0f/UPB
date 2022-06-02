

def make_binary(n):
    return bin(n)


def main(n):
    a = n & 0xffff
    b = n & 0x1ff0000
    c = n & 0b11111110000000000000000000000000
    a = a << 16
    b = b >> 9
    c = c >> 25
    return a | b | c

# tmp = 0x4b6bc3f5
tmp = 0xa7ad4244
# tmp = 1265353717
print(main(tmp))
print(make_binary(tmp))
# print(type(main(tmp)), main(tmp), len(main(tmp)))