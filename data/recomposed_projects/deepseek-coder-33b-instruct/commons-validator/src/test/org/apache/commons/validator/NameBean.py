class NameBean:

    def __init__(self) -> None:

        self._firstName = None

        self._middleName = None

        self._lastName = None

    
    def getFirstName(self) -> str:
        return self._firstName
    

    def setFirstName(self, firstName) -> None:
        self._firstName = firstName

    
    def getMiddleName(self) -> str:
        return self._middleName
    

    def setMiddleName(self, middleName) -> None:
        self._middleName = middleName

    
    def getLastName(self) -> str:
        return self._lastName
    

    def setLastName(self, lastName) -> None:
        self._lastName = lastName
