# Imports Begin
# Imports End


class InvalidFileNameException(Exception):

    # Class Fields Begin
    __serialVersionUID: int = 7922042602454350470
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def getName(self) -> str:

        return self.__name

    def __init__(self, pName: str, pMessage: str) -> None:

        super().__init__(pMessage)
        self.__name = pName

    # Class Methods End
