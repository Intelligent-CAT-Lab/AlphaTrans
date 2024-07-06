from __future__ import annotations
import copy
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.FileUploadBase import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
from src.main.org.apache.commons.fileupload.util.Closeable import *
from src.main.org.apache.commons.fileupload.ProgressListener import *


class ItemInputStream:

    __BYTE_POSITIVE_OFFSET: int = 256
    __closed: bool = False

    __pos: int = 0

    __pad: int = 0

    __total: int = 0

    def isClosed(self) -> bool:
        return self.__closed

    def skip(self, bytes: int) -> int:
        if self.__closed:
            raise FileItemStream.ItemSkippedException()
        av = self.available()
        if av == 0:
            av = self.__makeAvailable()
            if av == 0:
                return 0
        res = min(av, bytes)
        self.__head += res
        return res

    def read(self) -> int:
        return self.read0()

    def available(self) -> int:
        if self.__pos == -1:
            return self.__tail - self.__head - self.__pad
        return self.__pos - self.__head

    def close1(self, pCloseUnderlying: bool) -> None:
        if self.__closed:
            return
        if pCloseUnderlying:
            self.__closed = True
            self.input.close()
        else:
            while True:
                av = self.available()
                if av == 0:
                    av = self.__makeAvailable()
                    if av == 0:
                        break
                self.skip(av)
        self.__closed = True

    def close0(self) -> None:
        self.close1(False)

    def read1(self, b: typing.List[int], off: int, len: int) -> int:
        if self.__closed:
            raise FileItemStream.ItemSkippedException()
        if len == 0:
            return 0
        res = self.available()
        if res == 0:
            res = self.__makeAvailable()
            if res == 0:
                return -1
        res = min(res, len)
        System.arraycopy(buffer, head, b, off, res)
        head += res
        self.__total += res
        return res

    def read0(self) -> int:
        if self.__closed:
            raise FileItemStream.ItemSkippedException()
        if self.available() == 0 and self.__makeAvailable() == 0:
            return -1
        self.__total += 1
        b = self.buffer[self.head]
        self.head += 1
        if b >= 0:
            return b
        return b + self.__BYTE_POSITIVE_OFFSET

    def getBytesRead(self) -> int:
        return self.__total

    def __makeAvailable(self) -> int:
        if self.__pos != -1:
            return 0

        self.__total += self.__tail - self.__head - self.__pad
        System.arraycopy(
            self.__buffer, self.__tail - self.__pad, self.__buffer, 0, self.__pad
        )

        self.__head = 0
        self.__tail = self.__pad

        for _ in range(0, 1):
            bytesRead = self.__input.read(
                self.__buffer, self.__tail, self.__bufSize - self.__tail
            )
            if bytesRead == -1:
                msg = "Stream ended unexpectedly"
                raise MalformedStreamException(msg)
            if self.__notifier != None:
                self.__notifier.noteBytesRead(bytesRead)
            self.__tail += bytesRead

            self.__findSeparator()
            av = self.available()

            if av > 0 or self.__pos != -1:
                return av

    def __findSeparator(self) -> None:
        self.__pos = MultipartStream._findSeparator()
        if self.__pos == -1:
            if (
                MultipartStream.__tail - MultipartStream.__head
                > MultipartStream.__keepRegion
            ):
                self.__pad = MultipartStream.__keepRegion
            else:
                self.__pad = MultipartStream.__tail - MultipartStream.__head

    def __init__(self) -> None:
        self.__findSeparator()


class IllegalBoundaryException:

    __serialVersionUID: int = -161533165102632918

    def __init__(self, message: str) -> None:
        super().__init__(message)


class MalformedStreamException:

    serialVersionUID: int = 6466926458059796677

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ProgressNotifier:

    __items: int = 0

    __bytesRead: int = 0

    __contentLength: int = 0

    __listener: ProgressListener = None

    def __notifyListener(self) -> None:
        if self.__listener != None:
            self.__listener.update(self.__bytesRead, self.__contentLength, self.__items)

    def noteItem(self) -> None:
        self.__items += 1
        self.__notifyListener()

    def noteBytesRead(self, pBytes: int) -> None:
        self.__bytesRead += pBytes
        self.__notifyListener()

    def __init__(self, pListener: ProgressListener, pContentLength: int) -> None:
        self.__contentLength = pContentLength
        self.__listener = pListener


class MultipartStream:

    _DEFAULT_BUFSIZE: int = 4096
    HEADER_PART_SIZE_MAX: int = 10240
    DASH: int = 0x2D
    LF: int = 0x0A
    CR: int = 0x0D
    __notifier: ProgressNotifier = None

    __headerEncoding: str = ""

    __tail: int = 0

    __head: int = 0

    __buffer: typing.List[int] = None

    __bufSize: int = 0

    __boundaryTable: typing.List[int] = None

    __boundary: typing.List[int] = None

    __keepRegion: int = 0

    __boundaryLength: int = 0

    __input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

    _BOUNDARY_PREFIX: typing.List[int] = [CR, LF, DASH, DASH]
    _STREAM_TERMINATOR: typing.List[int] = [DASH, DASH]
    _FIELD_SEPARATOR: typing.List[int] = [CR, LF]
    _HEADER_SEPARATOR: typing.List[int] = [CR, LF, CR, LF]

    @staticmethod
    def MultipartStream3(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
    ) -> MultipartStream:
        return MultipartStream(input, boundary, MultipartStream._DEFAULT_BUFSIZE, None)

    @staticmethod
    def MultipartStream1(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        bufSize: int,
    ) -> MultipartStream:
        return MultipartStream(input, boundary, bufSize, None)

    @staticmethod
    def MultipartStream0() -> MultipartStream:
        return MultipartStream2(None, None, None)

    def _findSeparator(self) -> int:
        bufferPos = self.__head
        tablePos = 0

        while bufferPos < self.__tail:
            while (
                tablePos >= 0 and self.__buffer[bufferPos] != self.__boundary[tablePos]
            ):
                tablePos = self.__boundaryTable[tablePos]
            bufferPos += 1
            tablePos += 1
            if tablePos == self.__boundaryLength:
                return bufferPos - self.__boundaryLength
        return -1

    def _findByte(self, value: int, pos: int) -> int:
        for i in range(pos, self.__tail):
            if self.__buffer[i] == value:
                return i
        return -1

    @staticmethod
    def arrayequals(a: typing.List[int], b: typing.List[int], count: int) -> bool:
        for i in range(count):
            if a[i] != b[i]:
                return False
        return True

    def readHeaders(self) -> str:
        i: int = 0
        b: int = 0
        baos: BytesIO = BytesIO()
        size: int = 0
        while i < len(self._HEADER_SEPARATOR):
            try:
                b = self.readByte()
            except FileUploadIOException as e:
                raise e
            except IOException as e:
                raise MalformedStreamException("Stream ended unexpectedly")
            if size + 1 > self.HEADER_PART_SIZE_MAX:
                raise MalformedStreamException(
                    format(
                        "Header section has more than %s bytes (maybe it is not properly"
                        " terminated)",
                        Integer.valueOf(self.HEADER_PART_SIZE_MAX),
                    )
                )
            if b == self._HEADER_SEPARATOR[i]:
                i += 1
            else:
                i = 0
            baos.write(b)
        headers: str = None
        if self.__headerEncoding is not None:
            try:
                headers = baos.toString(self.__headerEncoding)
            except ValueError as e:
                headers = baos.toString()
        else:
            headers = baos.toString()
        return headers

    def setBoundary(self, boundary: typing.List[int]) -> None:
        if len(boundary) != self.__boundaryLength - len(self._BOUNDARY_PREFIX):
            raise IllegalBoundaryException(
                "The length of a boundary token cannot be changed"
            )
        System.arraycopy(
            boundary, 0, self.__boundary, len(self._BOUNDARY_PREFIX), len(boundary)
        )
        self.__computeBoundaryTable()

    def readBoundary(self) -> bool:
        marker: typing.List[int] = [0, 0]
        nextChunk: bool = False

        self.__head += self.__boundaryLength
        try:
            marker[0] = self.readByte()
            if marker[0] == MultipartStream.LF:
                return True

            marker[1] = self.readByte()
            if MultipartStream.arrayequals(
                marker, MultipartStream._STREAM_TERMINATOR, 2
            ):
                nextChunk = False
            elif MultipartStream.arrayequals(
                marker, MultipartStream._FIELD_SEPARATOR, 2
            ):
                nextChunk = True
            else:
                raise MalformedStreamException(
                    "Unexpected characters follow a boundary"
                )
        except FileUploadIOException as e:
            raise e
        except IOException as e:
            raise MalformedStreamException("Stream ended unexpectedly")
        return nextChunk

    def readByte(self) -> int:

        pass  # LLM could not translate this method

    def setHeaderEncoding(self, encoding: str) -> None:
        self.__headerEncoding = encoding

    def getHeaderEncoding(self) -> str:
        return self.__headerEncoding

    @staticmethod
    def MultipartStream2(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        pNotifier: ProgressNotifier,
    ) -> MultipartStream:
        return MultipartStream(
            input, boundary, MultipartStream._DEFAULT_BUFSIZE, pNotifier
        )

    def __init__(
        self,
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        bufSize: int,
        pNotifier: ProgressNotifier,
    ) -> None:

        pass  # LLM could not translate this method

    def __computeBoundaryTable(self) -> None:
        position: int = 2
        candidate: int = 0

        self.__boundaryTable[0] = -1
        self.__boundaryTable[1] = 0

        while position <= self.__boundaryLength:
            if self.__boundary[position - 1] == self.__boundary[candidate]:
                self.__boundaryTable[position] = candidate + 1
                candidate += 1
                position += 1
            elif candidate > 0:
                candidate = self.__boundaryTable[candidate]
            else:
                self.__boundaryTable[position] = 0
                position += 1

    def newInputStream(self) -> ItemInputStream:
        return ItemInputStream()
