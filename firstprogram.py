import logging
class FamilyInformation:

    def __init__(self):

        self._surname = "rajulapati"


    def AddParentInfo(self,FatherName,MotherName):

        self.father = FatherName + self._surname
        self.Mother = MotherName + self._surname
        self.Mother = MotherName + self._surname





obj = FamilyInformation()
obj.AddParentInfo("Subbarao","Prabhavathi devi")
print((obj.father))
print(obj.Mother)
print(obj._surname)
#logging.basicConfig(filename="C:\\Users\\RAJULAPATI\\Desktop\\python docs\\docs-pdf\\outputlog.log",filemode='w',level=logging.DEBUG)
#logging.info("Log message")
logger = logging.getLogger(logging.basicConfig(filename="C:\\Users\\RAJULAPATI\\Desktop\\python docs\\docs-pdf\\outputlog.log",filemode='w',level=logging.DEBUG))
logger.info("log new message")