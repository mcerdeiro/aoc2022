

lines = open('2022/02/in.in').read().splitlines()

def convertElvePlay(ep):
    return {'A': 'R', 'B': 'P', 'C': 'S'}[ep]

def convertMyPlay(mp):
    return {'X': 'R', 'Y': 'P', 'Z': 'S'}[mp]

def play(ep, mp):
    if mp == 'S':
        return {'S': 'DRAW', 'R': 'LOSE', 'P': 'WIN'}[ep]
    elif mp == 'P':
        return {'S': 'LOSE', 'R': 'WIN', 'P': 'DRAW'}[ep]
    elif mp == 'R':
        return {'S': 'WIN', 'R': 'DRAW', 'P': 'LOSE'}[ep]
    else:
        pass

    print(ep, mp)
    assert(0)

def want(m):
    return {'X': 'LOSE', 'Y': 'DRAW', 'Z': 'WIN'}[m]

def win(a):
    return {'S': 'R', 'R': 'P', 'P': 'S'}[a]

def lose(a):
    return {'S': 'P', 'P': 'R', 'R': 'S'}[a]

def draw(a):
    return a

assert(win('S') == 'R')
assert(win('P') == 'S')
assert(win('R') == 'P')

assert(lose('S') == 'P')
assert(lose('R') == 'S')
assert(lose('P') == 'R')

part1 = 0
for line in lines:
    elveplay, myplay = line.split()
    elveplay = convertElvePlay(elveplay)
    myplay = convertMyPlay(myplay)
    part1 += {'LOSE': 0, 'DRAW': 3, 'WIN': 6}[play(elveplay, myplay)]
    part1 += {'R': 1, 'P': 2, 'S': 3}[myplay]

print('Part1', part1)

part2 = 0
for line in lines:
    elveplay, myplay = line.split()
    celveplay = convertElvePlay(elveplay)
    iwant = want(myplay)
    ichoose = {'LOSE': lose(celveplay),
        'DRAW': draw(celveplay),
        'WIN': win(celveplay)}[iwant]
    part2 += {'R': 1, 'P': 2, 'S': 3}[ichoose]
    part2 += {'LOSE': 0, 'DRAW': 3, 'WIN': 6}[iwant]

print('Part2:', part2)