
# program sprawdzajacy czy liczba jest pierwsza
import math

def ifPrime(y):
	t = 1
	x = math.sqrt(y)

	divider = 2
	while divider <= x:	
		if y%divider == 0:
			t=0
			
			return t
			break
		divider+=1
	return t		
		

def PRIME_T():
	y = int(input())
	if ifPrime(y) == 0 or y == 1:
		print('NIE') # returny zrobić
	else:
		print('TAK')

PRIME_T()