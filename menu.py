
# silnia
import math
import os
def silnia(n):
	wynik = 1
	i = 1
	while i<=n:
		wynik*=i
		i=i+1
	liczD = int(wynik/10)
	liczJ = wynik - liczD*10 
	print(liczD,liczJ)
	
def FCTRL():
	D = int(input())
	i = 0
	while i < D:
		n = int(input())
		silnia(n)
		i=i+1



# skracanie stringa

def flamaste(napis):
	dl = len(napis)
	i = 0
	ct = 1
	while i<dl:
		ct = 1
		if i+2<dl:
			while napis[i] == napis[i+1]:
				ct += 1
				i += 1
		print(napis[i],ct)
		i += 1
		
		
	
def FLAM():
	
	D = int(input())
	j = 0
	while j < D:
		napis = (input())
		flamaste(napis)
		j=j+1



# liczba jednosci potegowania

def pow(a,b):
	wynik = a
	i = 1
	while i<b:
		wynik*=a
		i=i+1
	liczJ = wynik%10 
	print(liczJ)
	
def PA05_POT():
	
	D = int(input())
	j = 0
	while j < D:
		a = int(input())
		b = int(input())
		pow(a,b)
		j=j+1



# liczba jednosci potegowania
import math

def przedszk(a,b):
	il = a*b
	while a !=b:
		if a>b:
			a=a-b
		else:
			b=b-a	
	nww=int(il/a)
	print(nww)
	
def PRZDSZ():
	
	D = int(input())
	j = 0
	while j < D:
		data = input().split()
		przedszk(int(data[0]),int(data[1]))
		j=j+1

# program sprawdzajacy czy liczba jest pierwsza

def ifPrime(y):
	t = 1
	x = int(math.sqrt(y))

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
		print('NIE') 
	else:
		print('TAK')

def clear():
	os.system("cls")

def main():
	while True:
		clear()
		print("1. Liczby pierwsze")
		print("2. Dwie cyfry silni")
		print("3. Potegowanie")
		print("4. Flamaster")
		print("5. Przedszkolanka")
		print("6. Proste dodawanie")
		print("0. Zakoncz")
		print("\n")
		id = int(input("Podaj numer zadania:"))
		if id == 1: PRIME_T()
		elif id == 4: FLAM()
		elif id == 2: FCTRL()
		elif id == 3: PA05_POT()
		elif id == 5: PRZDSZ()
		elif id == 0: exit()
		else: main()
		b = input("kontynuuj...")
	
main()
