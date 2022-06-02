from struct import *
from struct import calcsize as cs
from struct import unpack as up


def main(p):
    si = 3
    a = {f"A{i}": None for i in range(1, 4)}
    b = {f'B{i}': None for i in range(1, 7)}
    tmp = list(up('<fiI5b3HHIIH', p[si:si + cs('<fiI5b3HHIIH')]))
    # print(tmp)
    a['A1'] = tmp[0]
    a['A2'] = tmp[1]
    b['B1'] = tmp[2]
    sss = ''
    for i in range(3, 8):
        sss += chr(tmp[i])
    b['B2'] = sss
    # print(b)
    adrs = tmp[8:11]
    # print(adrs)
    b3 = []
    for i in adrs:
        c = {f'C{k}': None for k in range(1, 5)}
        local_tmp = list(up('<dHIIh', p[i:i + cs('<dHIIh')]))
        c['C1'] = local_tmp[0]
        c['C2'] = local_tmp[1]
        aa = local_tmp[2:4]
        c['C3'] = list(up(f'<{aa[0]}H', p[aa[1]:aa[1] + cs(f'<{aa[0]}H')]))
        c['C4'] = local_tmp[4]
        b3.append(c)
    b['B3'] = b3
    b['B4'] = tmp[11]
    mn = tmp[-3]
    local_list = list(up('<Bhihfhfq', p[mn:mn + cs('<Bhihfhfq')]))
    d = {f'D{k}': local_list[k-1] for k in range(1, 9)}
    b['B5'] = d
    mn = tmp[-1]
    b['B6'] = list(up(f'<{tmp[-2]}i', p[mn:mn + cs(f'<{tmp[-2]}i')]))
    a['A3'] = b
    return a


print(main(( b'LBI\xaa\x9b\x91><\x82\xbd)\r\xf9[doiuah*\x00B\x00Z\x00\xdf\xe4n\x00\x00\x00'
             b'\x04\x00\x00\x00\x89\x00g\xcc\xcc-\xb0Ee*H\xc2\xdc?7j\x02\x00\x00\x00'
             b'&\x00\x00\x00\xd7\x0f\x9dK?Sp\xde\x878q\x9c\xe1\xbf:\xc9\x02\x00\x00\x00'
             b'>\x00\x00\x00\x9c\xeb|\xcd\x8734N\x9eXr\x86\xe2\xbf\xec\xaa\x02\x00\x00\x00'
             b'V\x00\x00\x00\xaa\x10\xa5\xc2T\x97,\xd2"\xff\xfbZ\x0b\xb9\xbc\xf1'
             b'\xac\xf3\xd0x\xbf\x96e\n\xe8\xe9s\x0f4\xf4\x0b|c\xbc\x0e^E\xb0K\xb2'
             b'\x19O\x16\xbd\xb7')))
# print(main(( b'LBI@\x91\xf4>Gl?\xbaK\xb6\x89\xd9elxbe*\x00B\x00Z\x00\x9f1n\x00\x00\x00'
#              b'\x08\x00\x00\x00\x89\x00\x02\x1frYTg\x8d|\xb6\xe3\xd1?T\x82\x02\x00\x00\x00'
#              b'&\x00\x00\x00[\xb8Kz\xd4\xfef\xc76\xce.\x9f\xe8?\tu\x02\x00\x00\x00'
#              b'>\x00\x00\x00\x06K\xdcrg\x00\x18\xa3\x89\xd9y\xd1\xe0\xbf\xb0\xd0'
#              b'\x02\x00\x00\x00V\x00\x00\x00,\xf0\xee7W\xc8\xdd:\xf8\xae\xf5\x1f'
#              b'\xe6\x00\xbf\x18W\x9e\xf4b?\xa3o\xd2\x1a\x05x\xf4\xee\x96\x1a\x0e1;\x7fW'
#              b'\xa2\xbeO\x04r\x8c\xa8\x0cc9\x00\x14{\xd1\x06\xcbD\xa0\x03\xbc \xa3RH\x00')))