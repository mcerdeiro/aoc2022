import collections
import itertools
from os.path import exists


file = 'in.in'
if not exists(file):
    file = '2022/05/' + file

lines = open(file).read().splitlines()

empty = None
moves = []
cranes1 = []
cranes2 = []

for i in range(9):
    cranes1.append([])
    cranes2.append([])

for line in lines:
    if line == '':
        empty = True
        continue
    if empty == None:
        if '[' in line:
            cols = []
            for i in range(0, 9):
                cols.append(line[i*4+1])
            for i,c in enumerate(cols):
                if c != ' ':
                    cranes1[i].append(c)
                    cranes2[i].append(c)

        else:
             continue
    else:
        all = line.split(' ')
        x = int(all[1])
        fr = int(all[3])
        to = int(all[5])

        tmp = []
        for i in range(x):
            tomove = cranes1[fr-1].pop(0)
            cranes1[to-1].insert(0, tomove)
            tmp.append(cranes2[fr-1].pop(0))
        tmp = tmp[::-1]

        for i in range(x):
            cranes2[to-1].insert(0, tmp.pop(0))

print('Part1:', ''.join([x[0] for x in cranes1]))
print('Part2:', ''.join([x[0] for x in cranes2]))
