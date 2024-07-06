from __future__ import annotations
import copy
import re
from io import IOBase
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.IOUtils import *


class CSVPrinter(io.BufferedIOBase):

    __newRecord: bool = True
    __format: CSVFormat = None

    __appendable: typing.Union[typing.List, io.TextIOBase] = None

    def flush(self) -> None:
        if isinstance(self.__appendable, io.TextIOBase):
            self.__appendable.flush()

    def close(self) -> None:
        self.close1(True)

    def printRecords1(self, values: typing.List[typing.Any]) -> None:
        self.printRecords0(values)

    def printRecords0(self, values: typing.Iterable[typing.Any]) -> None:
        for value in values:
            self.__printRecordObject(value)

    def printRecord2(self, values: typing.Iterable[typing.Any]) -> None:
        for t in values:
            try:
                self.print(t)
            except Exception as e:
                IOUtils.rethrow(e)
        self.println()

    def printRecord1(self, values: typing.List[typing.Any]) -> None:
        self.printRecord0(values)

    def printRecord0(self, values: typing.Iterable[typing.Any]) -> None:
        for value in values:
            self.print(value)
        self.println()

    def println(self) -> None:
        if self.__format.getTrailingDelimiter():
            self.__format.__append1(
                self.__format.getDelimiterString(), self.__appendable
            )
        if self.__format.__recordSeparator != None:
            self.__format.__append1(self.__format.__recordSeparator, self.__appendable)

    def printComment(self, comment: str) -> None:
        if comment == None or not self.__format.isCommentMarkerSet():
            return
        if not self.__newRecord:
            self.println()
        self.__format.__append1(self.__format.getCommentMarker(), self.__appendable)
        self.__format.__append1(SP, self.__appendable)
        for i in range(len(comment)):
            c = comment[i]
            if c == CR:
                if i + 1 < len(comment) and comment[i + 1] == LF:
                    i += 1
            elif c == LF:
                self.println()
                self.__format.__append1(
                    self.__format.getCommentMarker(), self.__appendable
                )
                self.__format.__append1(SP, self.__appendable)
            else:
                self.__format.__append1(c, self.__appendable)
        self.println()

    def print(self, value: typing.Any) -> None:
        self.__format.print2(value, self.__appendable, self.__newRecord)
        self.__newRecord = False

    def getOut(self) -> typing.Union[typing.List, io.TextIOBase]:
        return self.__appendable

    def close1(self, flush: bool) -> None:
        if flush or self.__format.getAutoFlush():
            self.flush()
        if isinstance(self.__appendable, io.TextIOBase):
            self.__appendable.close()

    def close0(self) -> None:
        self.close1(False)

    def __init__(
        self, appendable: typing.Union[typing.List, io.TextIOBase], format: CSVFormat
    ) -> None:
        if appendable is None:
            raise ValueError("appendable")
        if format is None:
            raise ValueError("format")
        self.__appendable = appendable
        self.__format = format.copy()
        headerComments = format.getHeaderComments()
        if headerComments is not None:
            for line in headerComments:
                self.printComment(line)
        if format.getHeader() is not None and not format.getSkipHeaderRecord():
            self.printRecord1(format.getHeader())

    def __printRecordObject(self, value: typing.Any) -> None:
        if isinstance(value, list):
            self.printRecord1(value)
        elif isinstance(value, Iterable):
            self.printRecord0(value)
        else:
            self.printRecord1(value)
