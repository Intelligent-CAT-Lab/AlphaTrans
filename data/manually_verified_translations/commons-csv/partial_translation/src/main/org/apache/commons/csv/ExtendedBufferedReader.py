from __future__ import annotations
import re
import io
import numbers
import typing
from typing import *
import os
from src.main.org.apache.commons.csv.Constants import *


class ExtendedBufferedReader(io.BufferedReader):

    __closed: bool = False

    __position: int = 0

    __eolCounter: int = 0

    __lastChar: int = Constants.UNDEFINED

    def readLine(self) -> str:

        if self.lookAhead0() == Constants.END_OF_STREAM:
            return None
        buffer = ""
        while True:
            current = self.read0()
            if current == ord(Constants.CR):
                next = self.lookAhead0()
                if next == ord(Constants.LF):
                    self.read0()
            if (
                current == Constants.END_OF_STREAM
                or current == ord(Constants.LF)
                or current == ord(Constants.CR)
            ):
                break
            buffer += chr(current)
        return buffer

    def close(self) -> None:
        self.__closed = True
        self.__lastChar = Constants.END_OF_STREAM
        super().close()

    def read1(self, buf: typing.List[str], offset: int, length: int) -> int:

        if length == 0:
            return 0

        len = super().read(buf, offset, length)

        if len > 0:

            for i in range(offset, offset + len):
                ch = buf[i]
                if ch == Constants.LF:
                    if Constants.CR != (buf[i - 1] if i > offset else self.__lastChar):
                        self.__eolCounter += 1
                elif ch == Constants.CR:
                    self.__eolCounter += 1

            self.__lastChar = buf[offset + len - 1]

        elif len == -1:
            self.__lastChar = Constants.END_OF_STREAM

        self.__position += len
        return len

    def read0(self) -> int:

        current = super().read()
        if (
            current == ord(Constants.CR)
            or (current == ord(Constants.LF) and self.__lastChar != ord(Constants.CR))
            or (
                current == Constants.END_OF_STREAM
                and self.__lastChar != ord(Constants.CR)
                and self.__lastChar != ord(Constants.LF)
                and self.__lastChar != Constants.END_OF_STREAM
            )
        ):
            self.__eolCounter += 1
        self.__lastChar = current
        self.__position += 1
        return self.__lastChar

    def isClosed(self) -> bool:
        return self.__closed

    def lookAhead2(self, n: int) -> typing.List[str]:

        buf = [""] * n
        self.mark(n)
        self.read(buf, 0, n)
        self.reset()

        return buf

    def lookAhead1(self, buf: typing.List[str]) -> typing.List[str]:

        n = len(buf)
        self.mark(n)
        self.read(buf, 0, n)
        self.reset()

        return buf

    def lookAhead0(self) -> int:

        self.mark(1)
        c = self.read(1)
        self.reset()

        return ord(c)

    def getPosition(self) -> int:
        return self.__position

    def getLastChar(self) -> int:
        return self.__lastChar

    def getCurrentLineNumber(self) -> int:

        if (
            self.__lastChar == Constants.CR
            or self.__lastChar == Constants.LF
            or self.__lastChar == Constants.UNDEFINED
            or self.__lastChar == Constants.END_OF_STREAM
        ):
            return self.__eolCounter  # counter is accurate
        else:
            return (
                self.__eolCounter + 1
            )  # Allow for counter being incremented only at EOL

    def __init__(
        self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader]
    ) -> None:
        super().__init__(reader)
