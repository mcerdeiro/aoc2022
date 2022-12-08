import collections
import itertools
from os.path import exists

p1 = 0
p2 = 0
file = 'in.in'

if not exists(file):
    file = '2022/08/' + file

lines = open(file).read().splitlines()

X = 0
Y = 0

M = dict()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        M[(x,y)] = int(lines[y][x])
        X = max(X, int(x)+1)
        Y = max(Y, int(y)+1)

def isVisible(M, x,y):
    dist = 1
    seenfrom = 0

    # X to right
    seen = True
    count1 = 0
    h = M[(x,y)]
    for x1 in range(x+1, X):
        if seen == True:
            count1 += 1
        if M[(x1,y)] >= h:
            seen = False

    if seen == True:
        seenfrom += 1
    dist *= count1

    #  Y down
    seen = True
    count2 = 0
    for y1 in range(y+1, Y):
        if seen == True:
            count2 += 1
        if M[(x,y1)] >= h:
            seen = False

    if seen == True:
        seenfrom += 1
    dist *= count2

    # Y up
    seen = True
    count3 = 0
    for y1 in range(y-1, -1, -1):
        if seen == True:
            count3 += 1
        if M[(x,y1)] >= h:
            seen = False

    if seen == True:
        seenfrom += 1
    dist *= count3

    # X left
    seen = True
    count4 = 0
    for x1 in range(x-1, -1, -1):
        if seen == True:
            count4 += 1
        if M[(x1,y)] >= h:
            seen = False

    if seen == True:
        seenfrom += 1
    dist *= count4

    # if (x,y) == (78, 47):
    #     print(count1, count2, count3, count4)

    return seenfrom > 0, dist

for y in range(Y):
    for x in range(X):
        #  checking xy
        v1,v2 = isVisible(M, x,y)
        p1 += v1
        p2 = max(p2, v2)

print('Part1:', p1)
print('Part2:', p2)
