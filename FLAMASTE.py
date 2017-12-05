# skracanie stringa
import math

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
		
		
	
def main():
	
	D = int(input())
	j = 0
	while j < D:
		napis = (input())
		flamaste(napis)
		j=j+1

main()