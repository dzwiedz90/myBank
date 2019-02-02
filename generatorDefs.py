import random

#PESEL generator
def peselGenerator():
	results = []
	for x in range(11):
		results.append(random.randrange(0,9))
		if (results[0] == 0):
			results.append(random.randrange(0,9))
		results = list(map(str, results))
	res = ''.join(results)
	return res

#Account number generator
def accountNumberGenerator():
	results = []
	for x in range(6):
		results.append(random.randrange(0,9))
		results = list(map(str, results))
	res = ''.join(results)
	return res