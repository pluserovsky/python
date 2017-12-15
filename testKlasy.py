class Facade:
	__prvAttribute="print __prvAttribute"
	pubAttribute = "print pubAttribute"
	def getPrvByPublicDef(self):
		print self.__prvAttribute
def test():
	obj = Facade()
	obj.getPrvByPublicDef()
	print obj.pubAttribute
	del obj
test()

