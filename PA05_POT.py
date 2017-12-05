# liczba jednosci potegowania
import math

def pow(a,b):
	wynik = a
	i = 1
	while i<b:
		wynik*=a
		i=i+1
	liczJ = wynik%10 
	print(liczJ)
	
def main():
	
	D = int(input())
	j = 0
	while j < D:
		a = int(input())
		b = int(input())
		pow(a,b)
		j=j+1

main()