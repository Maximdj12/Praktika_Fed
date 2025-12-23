# 1
def program(n, result):
	string = n[:1]
	rest = n[1::]
	modif = result
	if len(string) > 0:
		if string == "1":
			modif += 1
		elif string == "2":
			modif += 2
		elif string == "3":
			modif *= 2
		else:
			print("INVALID COMMAND", string)
		print(string, rest, modif)
		return program(rest, modif)
	return modif
print(program("3312",3))

# 2
def program2(n, result):
	string = n[:1]
	rest = n[1::]
	modif = result
	if len(string) > 0:
		if string == "1":
			modif += 1
		elif string == "2":
			modif = (modif*2)+1
		else:
			print("INVALID COMMAND", string)
		print(string, rest, modif)
		return program2(rest, modif)
	return modif
print(program2("211122", 1))

# 3
def program3(n, result):
	string = n[:1]
	rest = n[1::]
	modif = result
	if len(string) > 0:
		if string == "1":
			modif += 1
		elif string == "2":
			modif += 2
		else:
			print("INVALID COMMAND", string)
		print(string, rest, modif)
		return program3(rest, modif)
	return modif
print(program3("212", 7))

# 4
with open("27686.txt", "r") as f:
	symbols = f.read()
	countX = 0
	bestX = 0
	for i in range(len(symbols)):
		if symbols[i] != 'X':
			countX = 0
		else:
			countX += 1
		if countX > bestX:
			bestX = countX
	print(bestX)

# 5
with open("36037.txt", "r") as f:
	symbols = f.read()
	count = 0
	best = 0
	for i in range(len(symbols)-4):
		sp = [symbols[i],symbols[i+1],symbols[i+2],symbols[i+3]]
		if sp[0] == 'X' and sp[1] == 'Z' and sp[2] == 'Z' and sp[3] == "Y":
			count = 0
			i += 4
		else:
			count += 1
		if count > best:
			best = count
	print(best)

# 6
with open("46982.txt", "r") as f:
	symbols = f.read()
	startFound = False
	startI = 0
	endI = 0
	count = 0
	for i in range(len(symbols)):
		sym = symbols[i]
		if sym == 'E':
			if startFound == False:
				startFound = True
				startI = i
			else:
				startFound = False
				endI = i
			checksp = symbols[startI:endI+1]
			Fcheck = False
			Lcheck = False
			if len(checksp) > 12:
				Lcheck = True
			else:
				i = endI
				continue
			for j in checksp:
				if j == 'F':
					Fcheck = True
					i = endI
					break
			if Fcheck == False and Lcheck == True:
				print(checksp)
				i = endI
				count += 1
				startFound = False

	print(count)
