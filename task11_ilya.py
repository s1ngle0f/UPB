from struct import *


def main(file):
    start_index = 3
    a = {f'A{i}': None for i in range(1, 4)}
    b = {f'B{i}': None for i in range(1, 8)}
    bytes = '>qI' + 'IHI'*7 + 'qHHhIBBBBB'
    tmp = unpack(bytes, file[start_index:start_index + calcsize(bytes)])
    # print(tmp)
    b['B1'] = tmp[0]
    c = {f'C{i}': None for i in range(1, 5)}
    bytes = '>BIIQd'
    tmp_local = unpack(bytes, file[tmp[1]:tmp[1] + calcsize(bytes)])
    # print(tmp_local)
    c['C1'] = tmp_local[0]
    bytes = '>' + 'b'*tmp_local[1]
    c2 = unpack(bytes, file[tmp_local[2]:tmp_local[2]+calcsize(bytes)])
    str = ''
    for i in c2:
        str += chr(i)
    c['C2'] = str
    c['C3'] = tmp_local[3]
    c['C4'] = tmp_local[4]
    b['B2'] = c
    b3 = []
    for i in range(2, 22, 3):
        d = {f'D{i}': None for i in range(1, 4)}
        d['D1'] = tmp[i]
        d['D2'] = tmp[i+1]
        d['D3'] = tmp[i+2]
        b3.append(d)
    b['B3'] = b3
    b['B4'] = tmp[-10]
    e = {f'E{i}': None for i in range(1, 6)}
    bytes = '>IBBfQB'
    tmp_local = unpack(bytes, file[tmp[-9]:tmp[-9] + calcsize(bytes)])
    e['E1'] = tmp_local[0]
    e['E2'] = [tmp_local[1], tmp_local[2]]
    e['E3'] = tmp_local[3]
    e['E4'] = tmp_local[4]
    e['E5'] = tmp_local[5]
    b['B5'] = e
    b['B6'] = tmp[-8]
    b['B7'] = tmp[-7]
    # print(b)
    a['A1'] = b
    a['A2'] = tmp[-6]
    a3 = []
    for i in range(-5, 0):
        a3.append(tmp[i])
    a['A3'] = a3
    return a


bytes = (b'IIVJT\xa6|}\x02\x02\xf3\x00\x00\x00q\x9d\x11\xb4\xe9R\xbe\xd5\x1a\x14'
 b'\x8d\xe8\x02\xacF\xb1\xa9\xe0 \xca\xfdo\x83\xa7\xbe\xe6|2\xe5k'
 b'\xfc\x8b\x1b\x8f\xbb6\x93\xb0\xb3\x1f\x9d\xabe\xa7\x8b\xae\x981\xd3\xde'
 b'\x1f\xa39\xa8_\xdfS\x02\xc7\xde\xca\xef\xf0\xb1T\xbdQ\xfc\xc8}\x15\xf2]_'
 b'\xfa\xfa\xa9A\n\x00\x8a\n\xe3\xc9\x1dP/\xa0\x972\x80k\n\neblff&\x00\x00'
 b'\x00\x05\x00\x00\x00l\x81y\xd2\x13\x92\\@\x94?\xe1\x15\xc5\x0b"'
 b'\x06\xa4\xe7\xee\xdb\xdc\x177?t86g\x8e\xd4hg\xc6\xfc\xb7X')
print(main(bytes))
# bytes = (b'YNXN\xf5\xb6\x82m0\x00\x00\x00\x12\xcc\xe37\xa2Y\xa2f\x952Vv\xea\x15\xfa/'
#          b'\xf7\xa3\x01\xcbi\xa9\x97\x02\xf8f:\x03\xd7&\xa1zM\xab\xea\xd5X\x81\xed\xa6'
#          b'\xae\xaa\x7f\x11?\xdc\x93l?4Ai?=|i\xd8\x8d5\xe6\x1a\xb4\x11f\xdfC\xca\xad'
#          b'$">\xe0L\xe5=q\xd6%\xbe\xed\xf8P\x86\x9cm\x8d\xff\x0f5Y4\xa6\xd8\x86\x13d'
#          b'\xbd\x0e\xa4%?|\xbb\x02?\xeb\xd80\xfe\x9c\x02<\xff\xb79\xdf\x9d\xb2\xe4\x8b'
#          b'\x12#\x9cz\xd8?')
# print(main(bytes))