import collections
import itertools
from os.path import exists

p1 = None
p2 = None
file = 'in.in'
if not exists(file):
    file = '2022/06/' + file

lines = open(file).read().splitlines()

for i in range(len(lines[0])):
    sub4 = lines[0][i:i+4]
    sub14 = lines[0][i:i+14]
    if p1 == None and len(set(sub4)) == 4:
        p1 = i + 4
    if len(set(sub14)) == 14:
        p2 = i + 14
        break

print('Part1:', p1)
print('Part2:', p2)
