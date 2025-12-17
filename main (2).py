#1
def getpos(x, y):
    if x > 8 or y > 8 or x <= 0 or y <= 0:
        return "none"
    summa = x+y
    tile = summa%2
    if tile == 1:
        return "white"
    elif tile == 0:
        return "black"

def horserules(x1, y1, x2, y2):
    distX = abs(x2-x1)
    distY = abs(y2-y1)
    if distX == 2 and distY == 1:
        return True
    elif distY == 2 and distX == 1:
        return True
    else:
        return False
        

kon_x = int(input())
kon_y = int(input())
end_x = int(input())
end_y = int(input())
check1 = getpos(kon_x, kon_y)
check2 = getpos(end_x, end_y)
if check1 and check2 and horserules(kon_x, kon_y, end_x, end_y):
    print("Legal move")
else:
    print("Not legal move")


#2
k = int(input())
n = int(input())
for i in range(k,n+1):
    if i%2 == 0:
        print(i)
        
#3
summa = 0
value = int(input())
while value != 0:
    summa += value
    value = int(input())
print(summa)

#4
factor = 1
N = int(input())

for i in range(1, N+1):
    factor *= i
print(factor)
