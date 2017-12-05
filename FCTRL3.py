# silnia
import math

def silnia(n):
	wynik = 1
	i = 1
	while i<=n:
		wynik*=i
		i=i+1
	liczD = int(wynik/10)
	liczJ = wynik - liczD*10 
	print(liczD,liczJ)
	
def main():
	D = int(input())
	i = 0
	while i < D:
		n = int(input())
		silnia(n)
		i=i+1

main()