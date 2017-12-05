import hashlib
def md5Hash(hashTo):
	x = hashlib.md5(hashTo.encode('utf-8'))
	return x.hexdigest()

print(md5Hash(input("Wpisz slowo: ")))