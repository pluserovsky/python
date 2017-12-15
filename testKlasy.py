class Facade:
	__prvAttribute="print __prvAttribute"
	__prvToPrvDef="print __prvToPrvDef"
	pubAttribute = "print pubAttribute"
	goPub="goPub1"
	def getPrvByPublicDef(self):
		print self.__prvAttribute
		goPub="goPub"
		print goPub
	def __prvDef__(self):
#		self.goPub=self.__prvToPrvDef
		return self.goPub
	def PrvToPubReturn(self):
		self.__prvDef__()
class Params(Facade):
	def printFacadeAttrbs(self):
		print Facade.pubAttribute
		print Facade.goPub
def test():
#	obj = Facade()
#	obj.getPrvByPublicDef() goPub
#	print obj.PrvToPubReturn() # None
#	print obj.pubAttribute
#	del obj
	par = Params()
	par.printFacadeAttrbs()
	del par
test()

