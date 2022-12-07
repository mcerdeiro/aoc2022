import collections
import itertools
from os.path import exists

p1 = 0

file = 'in.in'
if not exists(file):
    file = '2022/07/' + file

lines = open(file).read().splitlines()

ROOT = []
i = 0
running = False
location = []

# parse the input
while i < len(lines):
    if '$ ' in lines[i]:
        cmds = lines[i].split()
        assert(cmds[0] == '$')
        if cmds[1] == 'cd':
            if cmds[2] == '/':
                location = []
            elif cmds[2] == '..':
                location.pop()
            else:
                location.append(cmds[2])
        elif cmds[1] == 'ls':
            pass
            contains = dict()
            running = True
    else:
        assert(running == True)
        sizeType, name = lines[i].split()
        if 'dir' != sizeType:
            sizeType = int(sizeType)
        contains[name] = sizeType
        if len(location) > 0:
            path = '/' + '/'.join(location) + '/' + name
        else:
            path = '/' + name
        if sizeType == 'dir':
            ROOT.append((path + '/', 0))
        else:
            ROOT.append((path, int(sizeType)))

    i += 1

#  calculate the size and update the nodes
for i, v in enumerate(ROOT):
    if v[1] == 0:
        size = 0
        for v2 in ROOT:
            if v2 == v:
                continue
            if v2[0].startswith(v[0]) and not v2[0].endswith('/'):
                size += v2[1]
        ROOT[i] = (v[0], size)


totalusedspace = 0
for d in ROOT:
    if d[0].endswith('/'):
        if d[1] <= 100000:
            p1 += d[1]
    else:
        totalusedspace += d[1]

print('Part1:', p1)
# print(ROOT)

goal = 30000000-(70000000-totalusedspace)
current = 100000000000
for d in ROOT:
    if d[0].endswith('/'):
       if d[1] > goal and d[1] < current:
             current = d[1]

print('Part2:', current)

