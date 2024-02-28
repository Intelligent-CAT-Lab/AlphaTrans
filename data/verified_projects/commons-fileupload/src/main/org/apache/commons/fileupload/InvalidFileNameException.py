# Imports Begin
# Imports End


class InvalidFileNameException(RuntimeException):

    # Class Fields Begin
    __serialVersionUID: int = 7922042602454350470
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def getName(self) -> str:

        return self.__name

    def __init__(self, pName: str, pMessage: str) -> None:

        super().__init__(pMessage)
        self.name = pName

    # Class Methods End
