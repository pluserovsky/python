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
	
def main():
	
	D = int(input())
	j = 0
	while j < D:
		data = input().split()
		przedszk(int(data[0]),int(data[1]))
		j=j+1

main()