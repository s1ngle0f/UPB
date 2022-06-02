from struct import unpack


def main(file):
    a_adr = 0
    for byte in file:
        a_adr += 1
        # print(hex(byte))
        if byte == 0x4e and a_adr != 2:
            break

    a = {f'A{i}': None for i in range(1, 5)}
    d = {f'D{i}': None for i in range(1, 4)}
    for id, val in enumerate(file[a_adr:a_adr + 44]):
        print(id, hex(val))
    temp = unpack('<iLiQL5l', file[a_adr:a_adr + 44])
    for i in temp:
        print(hex(i))
    a['A1'], b_adr, a['A3'] = temp[:3]
    d['D1'] = temp[3]
    d['D2'] = temp[4]
    d['D3'] = list(temp[5:])

    b = {f'B{i}': None for i in range(1, 4)}
    temp = unpack('<ib3fb8BIb3fb8BIb3fb8BId', file[b_adr:b_adr + 90])
    print(temp)
    b['B1'], *c_arr, b['B3'] = temp
    b['B2'] = []
    b['B2'] = []
    for i in range(3):
        temp = c_arr[i*14:(i+1)*14]
        b['B2'].append({'C1': temp[0], 'C2': list(temp[1:4]),
                        'C3': temp[4], 'C4': list(temp[5:13]), 'C5': temp[13]})
    a['A2'] = b
    a['A4'] = d
    return a


bytes = (b'YNXNw?\r.0\x00\x00\x00\xc2\x90\xa7(\x7f\x9c\x1a\x99\xbf<\x1fm\xf7$\xaa\x95'
         b'\xa0p\x87IzA\xdf\x1c\xf3\x1e\x9e:\x94F5T?\xba$*\x1c\xb5,<\xfb\x83$\xb1'
         b'\xbe\xe2z1\xbee\xf6\x0c\xbf\x86\x11\xbfR\x8a\xc4$\xb5@\xce`e\x86\xecnvH\xbfu'
         b'\x13\xc3>\xf1\x1a\x19?\xc8\x931M\x9b\xc9\x1cCoD\xbar&8N\xe2\xf2>\xef\nw?)q@'
         b'?,;\xb3\xebc\xa7\xc3\xa7\xbe\xf2\x1a\x07\xe1\x8c}T&\xec\xb3\xd3?')
print(main(bytes))
bytes = (b'YNXN\xf5\xb6\x82m0\x00\x00\x00\x12\xcc\xe37\xa2Y\xa2f\x952Vv\xea\x15\xfa/'
         b'\xf7\xa3\x01\xcbi\xa9\x97\x02\xf8f:\x03\xd7&\xa1zM\xab\xea\xd5X\x81\xed\xa6'
         b'\xae\xaa\x7f\x11?\xdc\x93l?4Ai?=|i\xd8\x8d5\xe6\x1a\xb4\x11f\xdfC\xca\xad'
         b'$">\xe0L\xe5=q\xd6%\xbe\xed\xf8P\x86\x9cm\x8d\xff\x0f5Y4\xa6\xd8\x86\x13d'
         b'\xbd\x0e\xa4%?|\xbb\x02?\xeb\xd80\xfe\x9c\x02<\xff\xb79\xdf\x9d\xb2\xe4\x8b'
         b'\x12#\x9cz\xd8?')
print(main(bytes))
