import numpy as np


def sort(data):
    if len(data) > 1:
        Mid = len(data) // 2
        l = data[:Mid]
        r = data[Mid:]
        sort(l)
        sort(r)

        z = 0
        x = 0
        c = 0

        while z < len(l) and x < len(r):
            if l[z][0] < r[x][0]:
                data[c] = l[z]
                z += 1
            else:
                data[c] = r[x]
                x += 1
            c += 1

        while z < len(l):
            data[c] = l[z]
            z += 1
            c += 1

        while x < len(r):
            data[c] = r[x]
            x += 1
            c += 1
        print(data, 'done')
unixdate = [200, 4800, 1458, 6812, 1988, 407, 710,154, 1200, 9200]
price=[90, 15, 25, 60, 450, 20, 120, 45, 37, 64]
array = np.column_stack((unixdate, price))
sort(array)
print(array, 'sorted')