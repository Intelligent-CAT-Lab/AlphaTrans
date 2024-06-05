class TypeBean:

    def __init__(self) -> None:
        self.__sByte = None
        self.__sShort = None
        self.__sInteger = None
        self.__sLong = None
        self.__sFloat = None
        self.__sDouble = None
        self.__sDate = None
        self.__sCreditCard = None

    
    def getByte(self) -> str:
        return self.__sByte
    

    def setByte(self, sByte) -> None:
        self.__sByte = sByte

    
    def getShort(self) -> str:
        return self.__sShort
    
    
    def setShort(self, sShort) -> None:
        self.__sShort = sShort
    
    
    def getInteger(self) -> str:
        return self.__sInteger

    
    def setInteger(self, sInteger) -> None:
        self.__sInteger = sInteger
    
    
    def getLong(self) -> str:
        return self.__sLong
    
    
    def setLong(self, sLong) -> None:
        self.__sLong = sLong

    
    def getFloat(self) -> str:
        return self.__sFloat
    

    def setFloat(self, sFloat) -> None:
        self.__sFloat = sFloat

    
    def getDouble(self) -> str:
        return self.__sDouble

    
    def setDouble(self, sDouble) -> None:
        self.__sDouble = sDouble

    
    def getDate(self) -> str:
        return self.__sDate


    def setDate(self, sDate) -> None:
        self.__sDate = sDate

    
    def getCreditCard(self) -> str:
        return self.__sCreditCard

    
    def setCreditCard(self, sCreditCard) -> None:
        self.__sCreditCard = sCreditCard
