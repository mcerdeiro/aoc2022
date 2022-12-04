import collections
import itertools
from os.path import exists


file = 'in.in'
if not exists(file):
    file = '2022/04/' + file

p1 = 0
p2 = 0

lines = open(file).read().splitlines()

for line in lines:
    a,b = line.split(',')
    s1,e1 = [int(x) for x in a.split('-')]
    s2,e2 = [int(x) for x in b.split('-')]

    if s2 <= s1 <= e2 and s2 <= e1 <= e2 or \
        s1 <= s2 <= e1 and s1 <= e2 <= e1:
            p1 += 1

    if  s2 <= s1 <= e2 or \
        s2 <= e1 <= e2 or \
        s1 <= s2 <= e1 or \
        s1 <= e2 <= e1:
            p2 += 1

print('Part1:', p1)
print('Part2:', p2)