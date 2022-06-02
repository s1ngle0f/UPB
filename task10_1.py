import numpy as np

def find_in_array(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1


def get_column(table, index):
    new_arr = []
    for row in table:
        new_arr.append(row[index])
    return new_arr


def transpose(table):
    new_table = []
    for i in range(len(table[0])):
        new_table.append(get_column(table, i))
    return new_table


def sort_by_column(table, id):
    new_table = []
    dct = {}
    for index, val in enumerate(table):
        dct[val[id]] = val
    dct = dict(sorted(dct.items(), key=lambda x: x[0]))
    print(dct)
    for key in dct:
        new_table.append(dct[key])
    return new_table

def split_column(column, char):
    new_arr0 = []
    for i in column:
        new_arr0.append(str(i).split(char))
    new_arr1 = []
    for i in range(len(new_arr0[0])):
        new_arr1.append(get_column(new_arr0, i))
    return new_arr1


def delete_column(table, index):
    new_table = []
    for row in table:
        new_row = []
        for index_element in range(len(row)):
            if index_element != index:
                new_row.append(row[index_element])
        new_table.append(new_row)
    return new_table


def add_column(table, index, column):
    new_table = []
    for row in range(len(table)):
        new_row = table[row][0:index]
        new_row.append(column[row])
        new_row += table[row][index:]
        new_table.append(new_row)
    return new_table


def delete_None(table):
    for col in range(len(table[0])):
        column = get_column(table, col)
        for i in column:
            if i is not None:
                break
            if i == column[-1]:
                return delete_column(table, col)


def check_columns(table):
    delete_ids = []
    for i in range(len(table[0])):
        for j in range(i + 1, len(table[0])):
            if get_column(table, i) == get_column(table, j):
                delete_ids.append(j)
    new_table = []
    for row in table:
        new_row = []
        for index_element in range(len(row)):
            if find_in_array(delete_ids, index_element) == -1:
                new_row.append(row[index_element])
        new_table.append(new_row)
    return new_table


def check_rows(table):
    delete_ids = []
    for row in range(len(table)):
        for j in range(row + 1, len(table)):
            if table[row] == table[j]:
                delete_ids.append(j)
    new_table = []
    for row in range(len(table)):
        if find_in_array(delete_ids, row) == -1:
            new_table.append(table[row])
    return new_table


def main(table):
    table = delete_None(table)
    table = check_columns(table)
    table = check_rows(table)
    # print(get_column(table, 1))
    # print(split_column(get_column(table, 1), '&'))
    table = add_column(table, 1, split_column(get_column(table, 1), '&')[0])
    table = add_column(table, 2, split_column(get_column(table, 2), '&')[1])
    table = delete_column(table, 3)
    table = add_column(table, 2, get_column(table, 3))
    table = delete_column(table, 4)
    for row in range(len(table)):
        if table[row][0] == 'Y':
            table[row][0] = 'Да'
        if table[row][0] == 'N':
            table[row][0] = 'Нет'
        table[row][1] = table[row][1][0:table[row][1].find(',')]
        tel = table[row][2][4:7] + '-'
        tel += table[row][2][9:]
        tel = tel[:tel.rfind('-')] + tel[-2:]
        table[row][2] = tel
        str = table[row][3][-2:]
        str += '-' + table[row][3][3:5]
        str += '-' + table[row][3][:2]
        table[row][3] = str
    # table = add_column(table, 1, [1, 1, 1]) #delete
    return table

table =[['N', None, 'Цотко, Л.Б.&23.07.00', 'N', '+7 (385) 282-26-82'],
        ['Y', None, 'Соцуфяк, Д.В.&06.06.99', 'Y', '+7 (505) 730-57-39'],
        ['Y', None, 'Соцуфяк, Д.В.&06.06.99', 'Y', '+7 (505) 730-57-39'],
        ['N', None, 'Мумамук, С.У.&04.02.01', 'N', '+7 (274) 292-94-75']]
# print(delete_column(table, 0))
print(np.array(table))
# print(np.array(transpose(table)))
print(np.array(sort_by_column(table, 2)))



