# mooo

n = int(input())
cows = []
volsHeard = [0 for i in range(n)]


for i in range(n):
        cows.append( [int(cow) for cow in input().split()] )
    
else:
    mooest = 0
    for i in range(n):
        hght = cows[i][0]
        volume = cows[i][1]
        a = i-1
        while a != -1:
            if cows[a][0] > hght:
                volsHeard[a] += volume
                print('volLeft', a, volume)
                break
            a -= 1
        a = i+1
        
        while a != n:
            if cows[a][0] > hght:
                volsHeard[a] += volume
                print('volRight', a, volume)
                break
            a += 1
                
        for vol in volsHeard:
            if vol > mooest:
                mooest = vol

    print(mooest)
