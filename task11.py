from struct import *


def main(package):
    start_index = 4
    a = {f"A{i}": None for i in range(1, 5)}
    b = {f'B{i}': None for i in range(1, 3)}
    tmp = unpack('<HHhIHIH', package[start_index:start_index + 18])
    b1 = list(unpack(f'<{tmp[0]}H', package[tmp[1]:tmp[1] + tmp[0]*2]))
    b['B1'] = b1
    b['B2'] = tmp[2]
    a['A1'] = b
    a['A2'] = tmp[3]
    a3 = []
    for i in range(tmp[4]):
        help_var = calcsize('<BbIH')
        c_local = list(unpack('<' + 'BbIH', package[tmp[5] + help_var * i:tmp[5]+help_var * (i + 1)]))
        c = {f'C{k}': None for k in range(1, 4)}
        c['C1'] = c_local[0]
        c['C2'] = c_local[1]
        c3 = list(unpack('<' + c_local[2] * 'h', package[c_local[3]:c_local[3] + 2 * c_local[2]]))
        c['C3'] = c3
        a3.append(c)
    a['A3'] = a3
    a4 = {f'D{k}': None for k in range(1, 5)}
    d = list(unpack('<df8HHI', package[tmp[-1]:tmp[-1] + calcsize('<df8HHI')]))
    a4['D1'] = d[0]
    a4['D2'] = d[1]
    a4['D3'] = d[2:10]
    a4['D4'] = list(unpack(f'<{d[-2]}q',
                           package[d[-1]:d[-1] + calcsize(f'<{d[-2]}q')]))
    a['A4'] = a4
    return a

print(main(( b"TLK-\x04\x00\x16\x00vXF'\x19\x13\x02\x000\x00\x00\x00`\x00QxM\xa6\xbf\xa5"
             b'\x89\xd4\x0c\x1eaI\x99\x14\x16\x1a\xc3Lt\xe52\x91\xddy\xff\xcb<\xe5\x05\x00'
             b'\x00\x00\x1e\x00c\xf4\x04\x00\x00\x00(\x005bg\xdaX\x08\xf5!H^\xcdVf\xf1\x08P'
             b'\x8b&GyX\x17\x05\xc9y\xcb\x1e>\x93\xd8*\xa900\xe2v!\x95\xba?S@5?'
             b'\x18\xf2\xcc\xaa\xf6\x81\xd4\xfasv\x19\xcb/x\x9c>\x04\x00@\x00\x00\x00')))