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

    __values: typing.List[str] = None

    __recordNumber: int = 0

    __comment: str = ""

    __characterPosition: int = 0

    __serialVersionUID: int = 1

    def toString(self) -> str:
        return (
            "CSVRecord [comment='"
            + self.__comment
            + "', recordNumber="
            + str(self.__recordNumber)
            + ", values="
            + str(self.__values)
            + "]"
        )

    def iterator(self) -> typing.Iterator[str]:
        return self.toList().iterator()

    def values(self) -> typing.List[str]:
        return self.__values

    def toMap(self) -> typing.Dict[str, str]:
        return self.putIn(typing.Dict[str, str](self.__values))

    def toList(self) -> typing.List[str]:
        return list(self.stream())

    def stream(self) -> typing.Iterable[str]:
        return self.__values

    def size(self) -> int:
        return len(self.__values)

    def putIn(self, map: typing.Any) -> typing.Any:
        if self.__getHeaderMapRaw() == None:
            return map
        self.__getHeaderMapRaw().forEach(
            lambda key, value: (
                map.put(key, self.__values[value])
                if value < len(self.__values)
                else None
            )
        )
        return map

    def isSet1(self, name: str) -> bool:
        return self.isMapped(name) and self.__getHeaderMapRaw().get(name) < len(
            self.__values
        )

    def isSet0(self, index: int) -> bool:
        return 0 <= index and index < len(self.__values)

    def isMapped(self, name: str) -> bool:
        headerMap = self.__getHeaderMapRaw()
        return headerMap is not None and name in headerMap

    def isConsistent(self) -> bool:
        headerMap = self.__getHeaderMapRaw()
        return headerMap == None or headerMap.size() == self.__values.size()

    def hasComment(self) -> bool:
        return self.__comment != None

    def getRecordNumber(self) -> int:
        return self.__recordNumber

    def getParser(self) -> CSVParser:
        return self.__parser

    def getComment(self) -> str:
        return self.__comment

    def getCharacterPosition(self) -> int:
        return self.__characterPosition

    def get2(self, name: str) -> str:
        headerMap = self.__getHeaderMapRaw()
        if headerMap == None:
            raise RuntimeError(
                "No header mapping was specified, the record values can't be accessed by name"
            )
        index = headerMap.get(name)
        if index == None:
            raise ValueError(
                String.format(
                    "Mapping for %s not found, expected one of %s",
                    name,
                    headerMap.keySet(),
                )
            )
        try:
            return self.__values[index]
        except ArrayIndexOutOfBoundsException as e:
            raise ValueError(
                String.format(
                    "Index for header '%s' is %d but CSVRecord only has %d values!",
                    name,
                    index,
                    Integer.valueOf(len(self.__values)),
                )
            )

    def get1(self, i: int) -> str:
        return self.__values[i]

    def get0(self, e: enum.Enum) -> str:
        return self.get2(e.name if e is not None else None)

    def __getHeaderMapRaw(self) -> typing.Dict[str, int]:
        return self.__parser.getHeaderMapRaw() if self.__parser is not None else None

    def __init__(
        self,
        parser: CSVParser,
        values: typing.List[str],
        comment: str,
        recordNumber: int,
        characterPosition: int,
    ) -> None:
        self.__recordNumber = recordNumber
        self.__values = values if values is not None else Constants.EMPTY_STRING_ARRAY
        self.__parser = parser
        self.__comment = comment
        self.__characterPosition = characterPosition
