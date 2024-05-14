# Imports Begin
from src.main.org.apache.commons.csv.Constants import *
import typing
import numbers

# Imports End


class ExtendedBufferedReader(BufferedReader):

    # Class Fields Begin
    __lastChar: int = None
    __eolCounter: int = None
    __position: int = None
    __closed: bool = None
    # Class Fields End

    # Class Methods Begin
    def readLine(self) -> str:
        pass

    def close(self) -> None:
        pass

    def read1(self, buf: typing.List[str], offset: int, length: int) -> int:
        pass

    def read0(self) -> int:
        pass

    def isClosed(self) -> bool:
        pass

    def lookAhead2(self, n: int) -> typing.List[str]:
        pass

    def lookAhead1(self, buf: typing.List[str]) -> typing.List[str]:
        pass

    def lookAhead0(self) -> int:
        pass

    def getPosition(self) -> int:
        pass

    def getLastChar(self) -> int:
        pass

    def getCurrentLineNumber(self) -> int:
        pass

    def __init__(
        self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader]
    ) -> None:
        pass

    # Class Methods End
