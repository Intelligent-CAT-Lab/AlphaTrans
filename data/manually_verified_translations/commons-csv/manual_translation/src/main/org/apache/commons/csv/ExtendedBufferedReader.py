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

        data = [chr(b) for b in super().read(length)]
        if not data:
            len_ = -1
        else:
            buf[offset:offset + len(data)] = data
            len_ = len(data)

        if len_ > 0:

            for i in range(offset, offset + len_):
                ch = buf[i]
                if ch == Constants.LF:
                    if Constants.CR != (buf[i - 1] if i > offset else self.__lastChar):
                        self.__eolCounter += 1
                elif ch == Constants.CR:
                    self.__eolCounter += 1

            self.__lastChar = ord(buf[offset + len_ - 1])

        elif len_ == -1:
            self.__lastChar = Constants.END_OF_STREAM

        self.__position += len_
        return len_

    def read0(self) -> int:

        current = super().read(1)
        current = ord(current) if current else -1

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

        buf = [''] * n
        return self.lookAhead1(buf)

    def lookAhead1(self, buf: typing.List[str]) -> typing.List[str]:

        n = len(buf)
        mark = super().tell()
        super().seek(mark)
        temp_buf = super().read(n)
        buf[:] = [chr(byte) for byte in temp_buf] if temp_buf else buf
        super().seek(mark)
        return buf

    def lookAhead0(self) -> int:

        mark = super().tell()
        super().seek(mark)
        c = super().read(1)
        super().seek(mark)
        return ord(c) if c else -1

    def getPosition(self) -> int:
        return self.__position

    def getLastChar(self) -> int:
        return self.__lastChar

    def getCurrentLineNumber(self) -> int:

        if (
            self.__lastChar == ord(Constants.CR)
            or self.__lastChar == ord(Constants.LF)
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
        if isinstance(reader, io.StringIO):
            reader = io.BytesIO(reader.getvalue().replace("\r\n", "\n").encode('utf-8'))
        super().__init__(reader)


class StringIOWrapper:
    def __init__(self, stringIO: io.StringIO) -> None:
        self.__stringIO = stringIO
        self.__closed = False
        self.__position = 0
        self.__eolCounter = 0
        self.__lastChar = Constants.UNDEFINED

    def readLine(self) -> str:
        if self.lookAhead0() == Constants.END_OF_STREAM:
            return None
        buffer = ""
        while True:
            current = self.read0()
            if current == ord(Constants.CR):
                nextChar = self.lookAhead0()
                if nextChar == ord(Constants.LF):
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
        self.__stringIO.close()

    def read1(self, buf: typing.List[str], offset: int, length: int) -> int:
        if length == 0:
            return 0

        data = self.__stringIO.read(length)
        if not data:
            len_ = -1
        else:
            buf[offset:offset + len(data)] = list(data)
            len_ = len(data)

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
        current = self.__stringIO.read(1)
        current = ord(current) if current else -1

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
        buf = [''] * n
        return self.lookAhead1(buf)

    def lookAhead1(self, buf: typing.List[str]) -> typing.List[str]:
        n = len(buf)
        currentPosition = self.__stringIO.tell()
        tempBuf = self.__stringIO.read(n)
        buf[:] = [chr(ord(byte)) for byte in tempBuf] if tempBuf else buf
        self.__stringIO.seek(currentPosition)
        return buf

    def lookAhead0(self) -> int:
        currentPosition = self.__stringIO.tell()
        c = self.__stringIO.read(1)
        self.__stringIO.seek(currentPosition)
        return ord(c) if c else -1

    def getPosition(self) -> int:
        return self.__position

    def getLastChar(self) -> int:
        return self.__lastChar

    def getCurrentLineNumber(self) -> int:
        if (
            self.__lastChar == ord(Constants.CR)
            or self.__lastChar == ord(Constants.LF)
            or self.__lastChar == Constants.UNDEFINED
            or self.__lastChar == Constants.END_OF_STREAM
        ):
            return self.__eolCounter
        else:
            return self.__eolCounter + 1