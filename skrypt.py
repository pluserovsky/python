import os
hostname='google.pl'
answer=os.system("ping -c 1 " +hostname)
if answer == 0:
	print(hostname + ' is UP')
else:
	print(hostname + ' is DOWN')
