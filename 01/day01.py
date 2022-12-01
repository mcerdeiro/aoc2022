import collections
import itertools
from os.path import exists

file = 'in.in'
if not exists(file):
    file = '2022/01/' + file
lines = open(file).read().splitlines()

E = []
elve = []
for line in lines:
    if line == '':
        E.append(sum(elve))
        elve = []
        continue
    elve.append(int(line))

E = sorted(E)
print('Part1:', max(E))
print('Part2:', sum(E[-3:]))
