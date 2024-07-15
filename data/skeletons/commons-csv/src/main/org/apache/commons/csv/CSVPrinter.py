from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.IOUtils import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.CSVFormat import *
import os
import typing
from typing import *
import io
from io import IOBase

# Imports End


class CSVPrinter(io.BufferedIOBase):

    # Class Fields Begin
    __appendable: typing.Union[typing.List, io.TextIOBase] = None
    __format: CSVFormat = None
    __newRecord: bool = None
    # Class Fields End

    # Class Methods Begin
    def flush(self) -> None:
        pass

    def close(self) -> None:
        pass

    def printRecords1(self, values: typing.List[typing.Any]) -> None:
        pass

    def printRecords0(self, values: typing.Iterable[typing.Any]) -> None:
        pass

    def printRecord2(self, values: typing.Iterable[typing.Any]) -> None:
        pass

    def printRecord1(self, values: typing.List[typing.Any]) -> None:
        pass

    def printRecord0(self, values: typing.Iterable[typing.Any]) -> None:
        pass

    def println(self) -> None:
        pass

    def printComment(self, comment: str) -> None:
        pass

    def print_(self, value: typing.Any) -> None:
        pass

    def getOut(self) -> typing.Union[typing.List, io.TextIOBase]:
        pass

    def close1(self, flush: bool) -> None:
        pass

    def close0(self) -> None:
        pass

    def __init__(
        self, appendable: typing.Union[typing.List, io.TextIOBase], format_: CSVFormat
    ) -> None:
        pass

    def __printRecordObject(self, value: typing.Any) -> None:
        pass

    # Class Methods End
