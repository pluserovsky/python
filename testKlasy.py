class Facade:
	__prvAttribute="print __prvAttribute"
	__prvToPrvDef="print __prvToPrvDef"
	pubAttribute = "print pubAttribute"

	def getPrvByPublicDef(self):
		print self.__prvAttribute
	def __prvDef__(self):
		return __prvToPrvDef
	def PrvToPubReturn(self):
		__prvDef__()
def test():
	obj = Facade()
	obj.getPrvByPublicDef()
	print obj.pubAttribute
	
	obj.PrvToPubReturn()
	del obj
test()

