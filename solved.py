import sys
input = sys.stdin.readline

P, M = map(int, input().split())
rooms = dict()

for i in range(P):
    l, name = input().rstrip().split()
    flag = 0

    for i in rooms.keys():
        if i-10 <= int(l) <= i+10 and len(rooms[i]) < M:
            rooms[i].append(l+' '+name)
            flag = 1
            break
    if not flag:
        rooms[int(l)] = [l+' '+name]

for i in rooms.keys():
    rooms[i].sort(key = lambda x: x.split()[1:])
    if len(rooms[i]) == M:
        print('Started!')
    else:
        print('Waiting!')
    for j in rooms[i]:
        print(j)