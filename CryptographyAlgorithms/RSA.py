# Ilyas Salimov, 2018
# Implemented on Python 3.5.2
# My understanding of this algorithm.

def isPrime(n):
	from math import sqrt 
	i = 2 
	while i <= sqrt(n): 
		if n % i == 0:
			return False
		i += 1
	return True 

def creation_keys():	
	from random import randint 
	p, q, e = 10, 10, 4
	while not isPrime(p):
		p = randint(500, 700)
	while not isPrime(q):
		q = randint(500, 700)
	n, f, d = p * q, (p - 1) * (q - 1), 0
	while (not isPrime(e)) or (e > f) or (f % e == 0): 
		e += 1 
	while (d * e) % f != 1:
		d += 1 
	return (e, n), (d, n)

def encoding():
	global textString, openKey, cipherList 
	cipherList = [] 
	e, n = openKey
	for letter in textString:
		cipherList.append(ord(letter) ** e % n) 

def decoding():
	global cipherList, closeKey, textString 
	textString = "" 
	d, n = closeKey
	for item in cipherList:
		textString += chr(int(item) ** d % n) 

def demonstrationMode():
	global textString, openKey, closeKey, cipherList
	import timeit
	print("\n » Demonstration mode activated! « (~˘▾˘)~")
	try: 
		textString = str(input("[+] Enter your textString - "))
		checking = textString[0]
	except:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit 
	openKey, closeKey = creation_keys()
	print("[~] Your open key - [{},{}].".format(openKey[0], openKey[1])) 
	print("[~] Your close key - [{},{}].".format(closeKey[0], closeKey[1]))
	encoding_performance = "%.5f" % timeit.timeit(encoding, number = 1)
	print("\n »» The result of encoding by RSA algorithm. ««") 
	print(cipherList) 
	textString = ""
	decoding_performance = "%.5f" % timeit.timeit(decoding, number = 1)
	print("\n »» The result of decoding by RSA algorithm. ««") 
	print(textString)
	print("\n[~] RSA algorithm encoding performance - {} sec.".format(encoding_performance)) 
	print("[~] RSA algorithm decoding performance - {} sec.".format(decoding_performance)) 

def encodingMode():
	global textString, openKey, cipherList 
	import timeit
	print("\n » Encoding mode activated! « (~˘▾˘)~") 
	try: 
		textString = str(input("[+] Enter your textString - "))
		checking = textString[0]
	except:
		print("[x] Invalid input! For example: \"hello\".")
		raise SystemExit 
	print(" • 0. Random open key.\n • 1. Your open key(for experienced).") 
	key = int(input("[?] Select open key method - "))
	if key == 0: 
		openKey, closeKey = creation_keys()
		print("[~] Your open key - [{},{}].".format(openKey[0], openKey[1])) 
		print("[~] Your close key - [{},{}].".format(closeKey[0], closeKey[1]))
	elif key == 1: 
		openKey = tuple(map(int, str(input("[+] Enter your open key - ")).split(",")))
	encoding_performance = "%.5f" % timeit.timeit(encoding, number = 1)
	print("\n »» The result of encoding by RSA algorithm. ««") 
	print(cipherList) 
	print("\n[~] RSA algorithm encoding performance - {} sec.".format(encoding_performance)) 

def decodingMode():
	global textString, closeKey, cipherList
	import timeit
	print("\n » Decoding mode activated! « (~˘▾˘)~") 
	try: 
		cipherList = input("[+] Enter your cipher list - ") 
		if cipherList[0] == "[":
			cipherList = list(map(int, cipherList[1:len(cipherList) - 1].split(","))) 
		else:
			cipherList = list(map(int, cipherList.split(","))) 
	except:
		print("[x] Invalid input! For example: \"[1, 2, 3, 4, 5]\".")
		raise SystemExit 
	closeKey = input("[+] Enter your close key - ") 
	if closeKey[0] == "[":
		closeKey = tuple(map(int, closeKey[1: len(closeKey) - 1].split(","))) 
	else:
		closeKey = tuple(map(int, closeKey.split(",")))
	decoding_performance = "%.5f" % timeit.timeit(decoding, number = 1)
	print("\n »» The result of decoding by RSA algorithm. ««") 
	print(textString)
	print("\n[~] RSA algorithm decoding performance - {} sec.".format(decoding_performance)) 

def main():
	print("\t\t[x] Rivest–Shamir–Adleman cryptography algorithm. [x]") 
	print(" • 0. Demonstration mode.\n • 1. Encoding mode.\n • 2. Decoding mode.") 
	try: 
		mode = int(input("[?] Select program mode - "))
	except:
		print("[x] Invalid input! For example: \"0, 1, 2\".")
		raise SystemExit 
	if mode == 0:
		demonstrationMode() 
	elif mode == 1:
		encodingMode()
	elif mode == 2:
		decodingMode()
	else:
		print("[x] Invalid input! You can only select: \"0, 1, 2\".")
		raise SystemExit 

openKey, closeKey, textString, cipherList = (), (), "", [] 
main()