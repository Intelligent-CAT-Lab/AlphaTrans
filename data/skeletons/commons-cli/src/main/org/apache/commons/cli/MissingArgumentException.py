# Imports Begin
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Option import *

# Imports End


class MissingArgumentException(ParseException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __option: Option = None
    # Class Fields End

    # Class Methods Begin
    def getOption(self) -> Option:
        pass

    @staticmethod
    def MissingArgumentException1(
        constructorId: int, message: str, option: Option
    ) -> "MissingArgumentException":
        pass

    def __init__(self, constructorId: int, message: str, option: Option) -> None:
        pass

    # Class Methods End
