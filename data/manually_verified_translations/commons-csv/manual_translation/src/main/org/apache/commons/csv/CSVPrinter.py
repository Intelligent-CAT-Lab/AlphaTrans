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
                self.print_(t)
            except IOError as e:
                raise e
        self.println()

    def printRecord1(self, values: typing.List[typing.Any]) -> None:

        self.printRecord0(values)

    def printRecord0(self, values: typing.Iterable[typing.Any]) -> None:

        for value in values:
            self.print_(value)
        self.println()

    def println(self) -> None:

        self.__format.println(self.__appendable)
        self.__newRecord = True

    def printComment(self, comment: str) -> None:

        if comment is None or not self.__format.isCommentMarkerSet():
            return
        if not self.__newRecord:
            self.println()
        if isinstance(self.__appendable, List):
            self.__appendable.append(self.__format.getCommentMarker())
            self.__appendable.append(Constants.SP)
        elif isinstance(self.__appendable, str):
            if self.__format.getCommentMarker() != None:
                self.__appendable += str(self.__format.getCommentMarker())
            self.__appendable += Constants.SP
        else:
            self.__appendable.write(self.__format.getCommentMarker())
            self.__appendable.write(Constants.SP)
        skipNextIteration = False
        for i in range(len(comment)):
            if skipNextIteration:
                skipNextIteration = False
                continue
            c = comment[i]
            if c == Constants.CR:
                if i + 1 < len(comment) and comment[i + 1] == Constants.LF:
                    skipNextIteration = True
            if c == Constants.LF or c == Constants.CR:
                self.println()
                if isinstance(self.__appendable, List):
                    self.__appendable.append(self.__format.getCommentMarker())
                    self.__appendable.append(Constants.SP)
                elif isinstance(self.__appendable, str):
                    if self.__format.getCommentMarker() != None:
                        self.__appendable += str(self.__format.getCommentMarker())
                    self.__appendable += Constants.SP
                else:
                    self.__appendable.write(self.__format.getCommentMarker())
                    self.__appendable.write(Constants.SP)
            if not (c == Constants.LF or c == Constants.CR):
                if isinstance(self.__appendable, List):
                    self.__appendable.append(c)
                elif isinstance(self.__appendable, str):
                    self.__appendable += c
                else:
                    self.__appendable.write(c)
        self.println()

    def print_(self, value: typing.Any) -> None:

        self.__format.print2(value, self.__appendable, self.__newRecord)
        self.__newRecord = False

    def getOut(self) -> typing.Union[typing.List, io.TextIOBase]:
        return self.__appendable

    def close1(self, flush: bool) -> None:
        if flush or self.__format.getAutoFlush():
            self.flush()
        if isinstance(self.__appendable, IOBase):
            self.__appendable.close()

    def close0(self) -> None:
        self.close1(False)

    def __init__(
        self, appendable: typing.Union[typing.List, io.TextIOBase], format_: CSVFormat
    ) -> None:

        if appendable is None or format_ is None:
            raise ValueError("appendable and format cannot be None")

        self.__appendable = appendable
        self.__format = format_.copy()

        header_comments = self.__format.getHeaderComments()
        if header_comments is not None:
            for line in header_comments:
                self.printComment(line)

        if (
            self.__format.getHeader() is not None
            and not self.__format.getSkipHeaderRecord()
        ):
            self.printRecord1(self.__format.getHeader())

    def __printRecordObject(self, value: typing.Any) -> None:

        if isinstance(value, list):
            self.printRecord1(value)
        elif isinstance(value, Iterable):
            self.printRecord0(value)
        else:
            self.printRecord1([value])
