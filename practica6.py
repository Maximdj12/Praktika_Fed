digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def translate(inp, base):
    result = ''
    numbers = int(inp)
    while numbers:
        result += digit[numbers % base]
        numbers //= base
    return result[::-1]

# 1
for x in digit:
	num1_str = '123' + x + '5'
	num2_str = '1' + x + '233'
	num1 = int(num1_str, 15)
	num2 = int(num2_str, 15)
	total = num1 + num2
	if total % 14 == 0:
		print(total // 14, translate(total // 14, 15))
		break

# 2
# for p in range(16,37):
# 	num1_str = 'AB267D1'
# 	num2_str = 'F024A89'
# 	num1 = int(num1_str, p)
# 	num2 = int(num2_str, p)
# 	total = num1+num2
# 	if total % (p - 1) == 0:
# 		print(total // p, p)
# 		break

# 3
for x in range(1,9):
	num1_str = str(x) + 'B09'
	num2_str = str(x) + '8E8'
	num1 = int(num1_str, 17)
	num2 = int(num2_str, 15)
	total = num1 + num2
	if total % 155 == 0:
		print(total // 155, x)


#4
end = False
for y in range(1,9):
	if end: break
	for x in range(1, 9):
		strx = str(x)
		stry = str(y)
		num1_str = stry + '04' + strx + '5'
		num2_str = '253' + str(x%7) + str(y%7)
		num1 = int(num1_str, 11)
		num2 = int(num2_str, 8)
		total = num1 = num2
		if total % 117 == 0:
			print(total // 117, x, y)
			end = True
			break