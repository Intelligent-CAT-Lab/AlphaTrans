from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVParser import *
import os
import typing
from typing import *
import enum
import numbers
import io

# Imports End


class CSVRecord:

    # Class Fields Begin
    __serialVersionUID: int = None
    __characterPosition: int = None
    __comment: str = None
    __recordNumber: int = None
    __values: typing.List[typing.List[str]] = None
    __parser: CSVParser = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def iterator(self) -> typing.Iterator[str]:
        pass

    def values(self) -> typing.List[typing.List[str]]:
        pass

    def toMap(self) -> typing.Dict[str, str]:
        pass

    def toList(self) -> typing.List[str]:
        pass

    def stream(self) -> typing.Iterable[str]:
        pass

    def size(self) -> int:
        pass

    def putIn(self, map_: typing.Any) -> typing.Any:
        pass

    def isSet1(self, name: str) -> bool:
        pass

    def isSet0(self, index: int) -> bool:
        pass

    def isMapped(self, name: str) -> bool:
        pass

    def isConsistent(self) -> bool:
        pass

    def hasComment(self) -> bool:
        pass

    def getRecordNumber(self) -> int:
        pass

    def getParser(self) -> CSVParser:
        pass

    def getComment(self) -> str:
        pass

    def getCharacterPosition(self) -> int:
        pass

    def get2(self, name: str) -> str:
        pass

    def get1(self, i: int) -> str:
        pass

    def get0(self, e: enum.Enum) -> str:
        pass

    def __getHeaderMapRaw(self) -> typing.Dict[str, int]:
        pass

    def __init__(
        self,
        parser: CSVParser,
        values: typing.List[typing.List[str]],
        comment: str,
        recordNumber: int,
        characterPosition: int,
    ) -> None:
        pass

    # Class Methods End
