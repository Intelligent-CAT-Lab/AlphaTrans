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

    __lastChar: int = UNDEFINED

    def readLine(self) -> str:
        if self.lookAhead0() == END_OF_STREAM:
            return None
        buffer = StringBuilder()
        while True:
            current = self.read0()
            if current == CR:
                next = self.lookAhead0()
                if next == LF:
                    self.read0()
            if current == END_OF_STREAM or current == LF or current == CR:
                break
            buffer.append(chr(current))
        return buffer.toString()

    def close(self) -> None:
        self.__closed = True
        self.__lastChar = END_OF_STREAM
        super().close()

    def read1(self, buf: typing.List[str], offset: int, length: int) -> int:
        if length == 0:
            return 0

        len = super().read(buf, offset, length)

        if len > 0:

            for i in range(offset, offset + len):
                ch = buf[i]
                if ch == LF:
                    if CR != (buf[i - 1] if i > offset else self.__lastChar):
                        self.__eolCounter += 1
                elif ch == CR:
                    self.__eolCounter += 1

            self.__lastChar = buf[offset + len - 1]

        elif len == -1:
            self.__lastChar = END_OF_STREAM

        self.__position += len
        return len

    def read0(self) -> int:
        current = super().read()
        if (
            current == CR
            or current == LF
            and self.__lastChar != CR
            or current == END_OF_STREAM
            and self.__lastChar != CR
            and self.__lastChar != LF
            and self.__lastChar != END_OF_STREAM
        ):
            self.__eolCounter += 1
        self.__lastChar = current
        self.__position += 1
        return self.__lastChar

    def isClosed(self) -> bool:
        return self.__closed

    def lookAhead2(self, n: int) -> typing.List[str]:
        buf = ["" for i in range(n)]
        return self.lookAhead1(buf)

    def lookAhead1(self, buf: typing.List[str]) -> typing.List[str]:
        n = len(buf)
        super().mark(n)
        super().read(buf, 0, n)
        super().reset()

        return buf

    def lookAhead0(self) -> int:
        self.mark(1)
        c = self.read()
        self.reset()
        return c

    def getPosition(self) -> int:
        return self.__position

    def getLastChar(self) -> int:
        return self.__lastChar

    def getCurrentLineNumber(self) -> int:
        if (
            self.__lastChar == CR
            or self.__lastChar == LF
            or self.__lastChar == UNDEFINED
            or self.__lastChar == END_OF_STREAM
        ):
            return self.__eolCounter
        return self.__eolCounter + 1

    def __init__(
        self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader]
    ) -> None:
        super().__init__(reader)
