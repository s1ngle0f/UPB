# | || auto usmaxe <= [onso_882 . abiinis_643 . anxe];||, ||auto maedla
# <= [anre . anus . eses_805 ];||,|| auto tibebi_499 <= [ erri . usedle
# ]; ||, || auto usinus <= [bema . main_509 . orer]; ||,|
import re


def main(s):
    s = s.replace('\n', '')
    s = s[1:-1]
    a = s.split('||')
    a = a[1:-1]
    a_names = []
    a_contents = []
    dct = {}
    for i in a:
        if i.find(',') == -1:
            tmp = i.replace('auto', '').replace(' ', '').replace(';', '')
            a_names.append(tmp[0:tmp.find('<')])
            a_contents.append(i[i.find('[')+1:i.find(']')]
                              .replace(' ', '').split('.'))
    for key in range(len(a_names)):
        dct[a_names[key]] = a_contents[key]
    return dct

# def main(s):
#     pattern = r"decl `(\w+) ?==> ?'(\w+)"
#     parsed_s = re.findall(pattern, s.replace('\n', ' '))
#     return {key: value for value, key in parsed_s}


# dct = {}
# dct['new'] = 123
# print(dct)

dct = main( "| || auto usmaxe <= [onso_882 . abiinis_643 . anxe];||, ||auto maedla"
            " <= [anre . anus . eses_805 ];||,|| auto tibebi_499 <= [ erri . usedle"
            " ]; ||, || auto usinus <= [bema . main_509 . orer]; ||,|")
dct = main( '||| auto ainenin<= [orbi . inedre . bien ]; ||, || auto cearis_776<=\n[islabe . edsoxe_432 . dianbe_117 ]; ||, |')
print(dct)
# print(dct, type(dct))
# print('{', end='')
# for key, val in dct:
#     print(key, val)