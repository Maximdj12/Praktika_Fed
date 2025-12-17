#1
"""n = int(input())
fibo = [0, 1]
for i in range(n-2):
    new_el = fibo[0] + fibo[1]
    fibo[0] = fibo[1]
    fibo[1] = new_el
    print(fibo)"""
    
#2
"""n = int(input())
fibo = [0, 1, 1]
for i in range(n):
    new_el = fibo[0] + fibo[1] + fibo[2]
    fibo[0] = fibo[1]
    fibo[1] = fibo[2]
    fibo[2] = new_el
    print(new_el, fibo)
"""

#3
coins = [
    [0,1,1,1,1,1],
    [0,0,0,0,0,1],
    [0,40,70,0,0,1],
    [100,0,0,0,0,1]
    ]
s = []
for i in range(len(coins)):
    s2 = []
    for j in range(len(coins[i])):
        direc = "_"
        if j == 0 and i == 0:
            direc = "0"
            s2.append(direc)
            continue
        elif i == 0 and j != 0:
            coins[i][j] += coins[i][j-1]
            direc = "<"
        elif i != 0 and j == 0:
            coins[i][j] += coins[i-1][j]
            direc = "^"
        else:
            original = coins[i][j]
            coins[i][j] += max(coins[i-1][j], coins[i][j-1])
            if original <= coins[i][j-1] or coins[i][j]-coins[i][j-1] == original:
                direc = "^"
            elif original <= coins[i-1][j] or coins[i][j]-coins[i-1][j] == original:
                direc = "<"
            else:
                direc = "<"
        s2.append(direc)
    s.append(s2)
    print(coins[i])
print(coins[-1][-1])
for b in s:
    print(b)