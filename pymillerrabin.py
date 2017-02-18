def findsd(n):
	d = n - 1
	s = 0
	while d % 2 == 0:
		d >>= 1
		s += 1
	
	return (s, d)

# Is composite?
def MillerRabin(n, a, s, d):
	if pow(a, d, n) == 1:
		return False #might be prime
	for r in range(0, s, 1):
		if pow(a, 2**r*d, n) == n-1:
			return False #might be prime
	return True #definitely not prime

# Is n prime? Works for n < 3317044064679887385961981
def isPrime(n):
	if n == 2:
		return True
	elif n < 2047:
		asl = [2]
	elif n < 1373653:
		asl = [2,3]
	elif n < 9080191:
		asl = [31, 73]
	elif n < 25326001:
		asl = [2, 3, 5]
	elif n < 3215031751:
		asl = [2, 3, 5, 7]
	elif n < 4759123141:
		asl = [2, 7, 61]
	elif n < 1122004669633:
		asl = [2, 13, 23, 1662803]
	elif n < 2152302898747:
		asl = [2, 3, 5, 7, 11]
	elif n < 3474749660383:
		asl = [2, 3, 5, 7, 11, 13]
	elif n < 341550071728321:
		asl = [2, 3, 5, 7, 11, 13, 17]
	elif n < 3825123056546413051:
		asl = [2, 3, 5, 7, 11, 13, 17, 19, 23]
	elif n < 318665857834031151167461:
		asl = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
	elif n < 3317044064679887385961981:
		asl = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
	else:
		raise Exception("n too big. Needs to be < 3317044064679887385961981")
	
	(s, d) = findsd(n)
	
	for a in asl:
		if MillerRabin(n, a, s, d):
			# definitely not prime
			return False
	# definitely prime
	return True

