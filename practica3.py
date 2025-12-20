"""import csv

l = []

with open("36031.csv", "r") as f:
    n = list(csv.reader(f))
    for i in range(len(n)-1):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        a = a[-1::-1]
        l.append(a)
    l = l [-1::-1]
    print(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        if i == 0 and j == 0:
            continue 
        elif i == 0 and j != 0:
            l[i][j] += l[i][j-1]
        elif i != 0 and j == 0:
            l[i][j] += l[i-1][j]
        else:
            l[i][j] += max(l[i-1][j], l[i][j-1])

print("Maximum l:", l[-1][-1])

directions = []
for i in range(len(l)):
    dir_row = []
    for j in range(len(l[i])):
        if i == 0 and j == 0:
            dir_row.append("P")
        elif i == 0 and j != 0:
            dir_row.append("←")
        elif i != 0 and j == 0:
            dir_row.append("↑")
        else:
            if l[i-1][j] > l[i][j-1]:
                dir_row.append("↑")
            else:
                dir_row.append("←")
    directions.append(dir_row)
    print(dir_row)
path = []
i, j = len(l)-1, len(l[0])-1
path.append((i, j))

while i > 0 or j > 0:
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    else:
        if l[i-1][j] > l[i][j-1]:
            i -= 1
        else:
            j -= 1
    path.append((i, j))

path.reverse()
for i in range(len(l)):
    for j in range(len(l[i])):
        if (i, j) in path:
            print(f"( {directions[i][j]} ) ", end="\t")
        else:
            print(f" {l[i][j]} ", end="\t")
    print()
print("END")"""

#2
"""import csv

with open("59778.csv", "r") as f:
    count = 0
    l = []
    n = list(csv.reader(f))
    for i in range(len(n)):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
    for i in l:
        numbers =  [int(x) for x in i]
        freq = {}
        for num in numbers:
            freq[num] = freq.get(num, 0) + 1

        has4equal = False
        repeatingnumber = False

        for num, count_freq in freq.items():
            if count_freq == 4:
                has4equal = True
                repeatingnumber = num

        if not has4equal:
            continue

        repeating_numbers = [repeatingnumber] * 4
        uniqueN = [num for num in numbers if num != repeatingnumber]

        if len(set(uniqueN)) != 3:
            continue

        avg_unique = sum(uniqueN) / len(uniqueN)
        sum_repeat = sum(repeating_numbers)
        print(avg_unique, sum_repeat)
        if avg_unique > sum_repeat:
            count += 1
    print(f"number of correct rows: {count}") # 7"""


#3
import csv

numbers = []
with open("29666.csv", 'r') as file:
    read = csv.reader(file, delimiter=';')
    for row in read:
        numbers.extend([float(x.replace(',', '.')) for x in row])
max_sum = numbers[0]
n = len(numbers)

for i in range(n):
    cursum = numbers[i]
    curmax = numbers[i]
    for j in range(i + 1, n):
        if numbers[j] < numbers[j - 1]:
            cursum += numbers[j]
            if cursum > curmax:
                curmax = cursum
        else:
            break

    if curmax > max_sum:
        max_sum = curmax
    else:
print(max_sum)