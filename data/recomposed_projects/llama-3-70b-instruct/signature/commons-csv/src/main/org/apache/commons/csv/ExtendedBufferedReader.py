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
        buffer = StringBuilder()
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
            buffer.append(chr(current))
        return str(buffer)

    def close(self) -> None:
        self.__closed = True
        self.__lastChar = Constants.END_OF_STREAM
        super().close()

    def read1(self, buf: typing.List[str], offset: int, length: int) -> int:
        if length == 0:
            return 0

        len_ = super().read(buf, offset, length)

        if len_ > 0:
            for i in range(offset, offset + len_):
                ch = buf[i]
                if ch == Constants.LF:
                    if Constants.CR != (buf[i - 1] if i > offset else self.__lastChar):
                        self.__eolCounter += 1
                elif ch == Constants.CR:
                    self.__eolCounter += 1
            self.__lastChar = buf[offset + len_ - 1]

        elif len_ == -1:
            self.__lastChar = Constants.END_OF_STREAM

        self.__position += len_
        return len_

    def read0(self) -> int:
        current = super().read()
        if (
            current == ord(Constants.CR)
            or (current == ord(Constants.LF) and self.__lastChar != ord(Constants.CR))
            or current == Constants.END_OF_STREAM
            and self.__lastChar
            not in [ord(Constants.CR), ord(Constants.LF), Constants.END_OF_STREAM]
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
            self.__lastChar == Constants.CR
            or self.__lastChar == ord(Constants.LF)
            or self.__lastChar == Constants.UNDEFINED
            or self.__lastChar == Constants.END_OF_STREAM
        ):
            return self.__eolCounter  # counter is accurate
        return self.__eolCounter + 1  # Allow for counter being incremented only at EOL

    def __init__(
        self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader]
    ) -> None:
        super().__init__(reader)
