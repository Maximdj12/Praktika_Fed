#1
# def factorial(n):
# 	if n >= 1:
# 		return n * factorial(n - 1)
# 	return 1

# f = 4
# print(factorial(f))


#2
# def remove_vowel(string):
# 	vowels = list("aeiou")
# 	t = list(string)
# 	result = []
# 	check = False
# 	for s in range(len(t)):
# 		check = False
# 		for vowel in vowels:
# 			if t[s] in vowel:
# 				check = True
# 		if check == False:
# 			result.append(t[s])
# 	if check == True:
# 		return remove_vowel(result)
# 	return result

# print(*remove_vowel("taeeioustttt"), sep = "")

#3
def fun(sp):
    l = []
    if len(sp) > 2:
        for q in range(len(sp)):
                if sp[q] == 1:
                    l.append(sp[q]) #dobav1
                    continue
                zas = sp[q]-l[q-1] 	# 7 - 1 = 6
                					# 21-6 = 15
                					# 35-15 = 20
                l.append(zas) 		#dobav 6 : 1,6
                              		#dobav 15: 1,6,15,20
                if zas == 1:
                    break
        print(sp)
        return fun(l)
    return sp 
spis = [1,7,21,35,35,21,7,1]
print(fun(spis))
