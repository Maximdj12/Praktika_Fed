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

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue  # Starting point
        elif i == 0 and j != 0:
            coins[i][j] += coins[i][j-1]
        elif i != 0 and j == 0:
            coins[i][j] += coins[i-1][j]
        else:
            coins[i][j] += max(coins[i-1][j], coins[i][j-1])

print("Maximum coins:", coins[-1][-1])

directions = []
for i in range(len(coins)):
    dir_row = []
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            dir_row.append("S")
        elif i == 0 and j != 0:
            dir_row.append("←")
        elif i != 0 and j == 0:
            dir_row.append("↑")
        else:
            if coins[i-1][j] > coins[i][j-1]:
                dir_row.append("↑")
            else:
                dir_row.append("←")
    directions.append(dir_row)

path = []
i, j = len(coins)-1, len(coins[0])-1
path.append((i, j))

while i > 0 or j > 0:
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    else:
        if coins[i-1][j] > coins[i][j-1]:
            i -= 1
        else:
            j -= 1
    path.append((i, j))

path.reverse()
for i in range(len(coins)):
    for j in range(len(coins[i])):
        if (i, j) in path:
            print(f"({coins[i][j]})", end="\t")
        else:
            print(f" {coins[i][j]} ", end="\t")
    print("\n")
print("END")
