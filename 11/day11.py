import collections
import itertools
from os.path import exists
from functools import reduce

file = 'in.in'
if not exists(file):
    file = '2022/11/' + file

lines = open(file).read().splitlines()

def getInput(lines):
    MS = []
    M = None
    for line in lines:
        if M == None:
            M = dict()
            M['count'] = 0
        if line == '':
            MS.append(M)
            M = dict()
        elif 'Monkey' in line:
            pass
        elif 'Starting items' in line:
            line = line.replace(',','')
            vals = [int(x) for x in line.split()[2:]]
            M['items'] = vals
        elif 'Operation' in line:
            val = line.split('Operation: ')[1]
            M['op'] = val
        elif 'Test: ' in line:
            val = int(line.split()[-1])
            M['test'] = val
        elif 'If true: ' in line:
            val = int(line.split()[-1])
            M['true'] = val
        elif 'If false: ' in line:
            val = int(line.split()[-1])
            M['false'] = val
        else:
            pass

    return MS

def performOperation(va, msg):
    if msg == 'new = old * 19':
        return va * 19
    elif msg == 'new = old + 6':
        return va + 6
    elif msg == 'new = old * old':
        return va * va
    elif msg == 'new = old + 3':
        return va + 3
    elif msg == 'new = old * 2':
        return va * 2
    elif msg == 'new = old + 5':
        return va + 5
    elif msg == 'new = old + 4':
        return va + 4
    elif msg == 'new = old + 8':
        return va + 8
    elif msg == 'new = old * 5':
        return va * 5
    else:
        pass

    print(va, msg)
    assert(0)

def printMon():
    for i, M in enumerate(MS):
        print('Monkey', i, M['items'])

def playRounds(count, MS, p2 = False):
    primes = [M['test'] for M in MS]
    primesmul = reduce(lambda a,b: a*b, primes)
    for _ in range(count):
        for M in MS:
            while len(M['items']) > 0:
                itemvalue = M['items'].pop(0)
                if "count" in M.keys():
                    M['count'] += 1
                else:
                    M['count'] = 1
                itemvalue = performOperation(itemvalue, M['op'])
                if p2 == False:
                    itemvalue //= 3
                else:
                    itemvalue %= primesmul
                if itemvalue % M['test'] == 0:
                    MS[M['true']]['items'].append(itemvalue)
                else:
                    MS[M['false']]['items'].append(itemvalue)

    vals = [x['count'] for x in MS]
    vals.sort()
    return vals[-1]*vals[-2]

MS = getInput(lines)
print('Part1:', playRounds(20, MS))

MS = getInput(lines)
print('Part2:', playRounds(10000, MS, True))
