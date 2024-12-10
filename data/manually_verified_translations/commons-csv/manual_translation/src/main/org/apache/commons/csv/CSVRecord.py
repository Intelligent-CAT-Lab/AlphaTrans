from __future__ import annotations
import re
import io
import numbers
import enum
import typing
from typing import *
import os
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.Constants import *


class CSVRecord:

    __parser: CSVParser = None

    __values: typing.List[typing.List[str]] = None

    __recordNumber: int = 0

    __comment: str = ""

    __characterPosition: int = 0

    __serialVersionUID: int = 1

    def __iter__(self) -> typing.Iterator[str]:
        return self.iterator()
    
    def toString(self) -> str:
        return "CSVRecord [comment='{}', recordNumber={}, values={}]".format(
            self.__comment, self.__recordNumber, self.__values
        )

    def iterator(self) -> typing.Iterator[str]:
        return iter(self.toList())

    def values(self) -> typing.List[typing.List[str]]:
        return self.__values

    def toMap(self) -> typing.Dict[str, str]:

        return self.putIn({})

    def toList(self) -> typing.List[str]:
        return list(self.stream())

    def stream(self) -> typing.Iterable[str]:
        return iter(self.__values)

    def size(self) -> int:
        return len(self.__values)

    def putIn(self, map_: typing.Any) -> typing.Any:

        if self.__getHeaderMapRaw() is None:
            return map_

        for key, value in self.__getHeaderMapRaw().items():
            if value < len(self.__values):
                map_[key] = self.__values[value]

        return map_

    def isSet1(self, name: str) -> bool:
        return self.isMapped(name) and self.__getHeaderMapRaw()[name] < len(
            self.__values
        )

    def isSet0(self, index: int) -> bool:
        return 0 <= index < len(self.__values)

    def isMapped(self, name: str) -> bool:
        headerMap = self.__getHeaderMapRaw()
        return headerMap is not None and name in headerMap

    def isConsistent(self) -> bool:
        headerMap = self.__getHeaderMapRaw()
        return headerMap is None or len(headerMap) == len(self.__values)

    def hasComment(self) -> bool:
        return self.__comment is not None

    def getRecordNumber(self) -> int:
        return self.__recordNumber

    def getParser(self) -> CSVParser:
        return self.__parser

    def getComment(self) -> str:
        return self.__comment

    def getCharacterPosition(self) -> int:
        return self.__characterPosition

    def get2(self, name: str) -> str:

        header_map = self.__getHeaderMapRaw()
        if header_map is None:
            raise RuntimeError(
                "No header mapping was specified, the record values can't be accessed by name"
            )
        index = header_map.get(name)
        if index is None:
            raise ValueError(
                f"Mapping for {name} not found, expected one of {header_map.keys()}"
            )
        try:
            return self.__values[index][0]
        except IndexError:
            raise ValueError(
                f"Index for header '{name}' is {index} but CSVRecord only has {len(self.__values)} values!"
            )

    def get1(self, i: int) -> str:
        return self.__values[i]

    def get0(self, e: enum.Enum) -> str:

        if e is None:
            return self.get2(None)
        else:
            return self.get2(e.name)

    def __getHeaderMapRaw(self) -> typing.Dict[str, int]:
        return self.__parser.getHeaderMapRaw() if self.__parser is not None else None

    def __init__(
        self,
        parser: CSVParser,
        values: typing.List[typing.List[str]],
        comment: str,
        recordNumber: int,
        characterPosition: int,
    ) -> None:

        self.__parser = parser
        self.__values = values if values is not None else Constants.EMPTY_STRING_ARRAY
        self.__recordNumber = recordNumber
        self.__comment = comment
        self.__characterPosition = characterPosition
