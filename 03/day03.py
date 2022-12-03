import collections
import itertools
from os.path import exists

file = 'in.in'
if not exists(file):
    file = '2022/03/' + file

p1 = 0
p2 = 0

lines = open(file).read().splitlines()

def getPrio(t):
    p = 'abcdefghijklmnopqrstuvwxyz'
    P = p.upper()
    assert(len(p) == 26)
    if t in P:
        return P.index(t) + 27
    if t in p:
        return p.index(t) + 1
    assert(0)

assert(getPrio('a') == 1)
assert(getPrio('z') == 26)
assert(getPrio('A') == 27)
assert(getPrio('Z') == 52)

for line in lines:
    comp1 = line[0:len(line)//2]
    comp2 = line[len(line)//2::]
    itemsboth = set(comp1).intersection(set(comp2))
    for item in itemsboth:
        p1 += getPrio(item)

print('Part1:', p1)

for i in range(0, len(lines), 3):
    elv1 = lines[i]
    elv2 = lines[i+1]
    elv3 = lines[i+2]
    badge = set(elv1).intersection(set(elv2)). intersection(elv3)
    assert(len(badge) == 1)
    p2 += getPrio(badge.pop())


print('Part2:', p2)