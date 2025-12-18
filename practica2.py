#1
count = 0
summa = 0
with open("39762.txt","r") as f:
	n = f.readlines()
	n = [int(el) for el in n]
	for i in range(len(n)-1):
		el = n[i]
		el1 = n[i+1]
		result = el+el1
		if (el*el1)%15 == 0 and result % 7 == 0:
			count += 1
			if summa < result:
				summa = result
print(count, summa)

#2
with open("68279.txt", "r") as f:
	n = f.readlines()
	n = [int(el) for el in n]
	count_el = 0
	max_el = 0
	for i in n:
		if str(i)[-3:] == "562":
			if i > max_el:
				max_el = i
	print(max_el)
	for i in range(len(n)-3):
		el1 = n[i]
		el2 = n[i+1]
		el3 = n[i+2]
		el4 = n[i+3]
		s = [el1, el2, el3, el4]
		count5 = 0
		notcount5 = 0
		divby3 = 0
		divby7 = 0
		summa = 0
		for j in s:
			if len(str(j)) == 5:
				count5 += 1
			else:
				notcount5 += 1

			if j % 3 == 0:
				divby3 += 1
			elif j % 7 == 0:
				divby7 += 1

			if sum(s) > max_el and sum(s) < max_el*2 and count5 >= 1 and notcount5 >= 2 and divby3 < divby7:
				count_el += 1
				best_el_sum = sum(s)
				
print(count_el, best_el_sum)

#3
with open("40992.txt", "r") as f:
	n = f.readlines()
	n = [int(el) for el in n]
	summa = 0
	countby3 = 0
	countbyel = 0
	bestelsum = 0
	for j in n:
		if j % 2 == 1:
			countby3 += 1
			summa += j
	summa /= countby3
	for j in range(len(n)-1):
		el = n[j]
		el1 = n[j+1]
		s = [el, el1]
		divby5 = False
		sumcheck = False
		for d in s:
			if d % 5 == 0:
				divby5 = True
			if d < summa:
				sumcheck = True
		if divby5 == True and sumcheck == True:
			countbyel += 1
			if sum(s) > bestelsum:
				bestelsum = sum(s)
print(countbyel, bestelsum)