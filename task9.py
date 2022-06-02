

class Milli:
    hurry_dict = {
        'A': ['B', 0],
        'B': ['E', 2],
        'C': ['D', 3],
        'D': ['G', 5],
        'E': ['E', 7],
        'F': ['G', 8],
        'G': []
    }
    base_dict = {
        'B': ['C', 1],
        'D': ['E', 4],
        'E': ['F', 6],
        'F': ['C', 9],
        'G': []
    }

    def __init__(self):
        self.state = 'A'

    def hurry(self):
        if self.state == 'G':
            raise KeyError()
        tmp = self.hurry_dict[self.state][1]
        self.state = self.hurry_dict[self.state][0]
        # print(tmp)
        return tmp

    def base(self):
        if self.state == 'G':
            raise KeyError()
        tmp = self.base_dict[self.state][1]
        self.state = self.base_dict[self.state][0]
        # print(tmp)
        return tmp


def main():
    return Milli()

o = main()
o.hurry() # 0
o.hurry() # 2
o.hurry() # 7
o.hurry() # 7
o.base() # 6
o.base() # 9
o.hurry() # 3
o.base() # 4
o.base() # 6
o.hurry() # 8
o.hurry() # Error