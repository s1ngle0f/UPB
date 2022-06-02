import numpy as np


def check_columns(table):
    ids = []
    correct = 0
    for i in range(table.shape[1]):
        tmp = table[:, i]
        tmp = tmp[tmp != None]
        if len(tmp) == 0:
            # table = np.delete(table, i, 1)
            ids.append(i)
    for id in ids:
        table = np.delete(table, id + correct, 1)
        correct -= 1
    return table


def main(table):
    table = np.array(table)
    print(table[:, 0] == table[:, 3])
    table = check_columns(table)
    new_table = []
    return table

table =[['N', None, 'Цотко, Л.Б.&23.07.00', 'N', '+7 (385) 282-26-82'],
        ['Y', None, 'Соцуфяк, Д.В.&06.06.99', 'Y', '+7 (505) 730-57-39'],
        ['Y', None, 'Соцуфяк, Д.В.&06.06.99', 'Y', '+7 (505) 730-57-39'],
        ['N', None, 'Мумамук, С.У.&04.02.01', 'N', '+7 (274) 292-94-75']]

print(main(table))
