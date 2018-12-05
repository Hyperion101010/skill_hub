import os
from operator import itemgetter

test = int(input())
while test != 0:
    data = []
    person = []
    n, k = list(map(int, input().split()))
    for i in n:
        l, r = list(map(int, input().split()))
        dummy = dict()
        dummy['index'] = l
        dummy['last'] = r
        data.append(dummy)
    sorted(data, key='index')
    for i in range(k):
        person.append(int(input()))
    for i in range(k):
        j = 0
        for j in range(data):
            if person[i] < data[j].get('index'):
                break
        if j != 0:
            if j <= len(data) - 1:
                if data[j - 1].get('last') > person[k]:
                    print (0)
                elif data[j - 1].get('last') < person[k]:
                    print (-1)
                else:
                    print (data[j].get('index') - person[k])
        else:
            if data[0].get('index') < person[k]:
                print (0)
            elif data[0].get('last') > person[k]:
                print (-1)
            else:
                print (data[0].get('index') - person[k])
    test -= 1
