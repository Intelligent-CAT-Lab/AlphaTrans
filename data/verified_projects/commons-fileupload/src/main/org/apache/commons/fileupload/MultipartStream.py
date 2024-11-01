import pytest

# Imports Begin
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.util.Closeable import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
from src.main.org.apache.commons.fileupload.FileUploadBase import *
import os
import typing
from typing import *
import io

# Imports End

class ProgressNotifier:

    # Class Fields Begin
    __listener: ProgressListener = None
    __contentLength: int = None
    __bytesRead: int = None
    __items: int = None
    # Class Fields End

    # Class Methods Begin
    def __notifyListener(self) -> None:

        if self.__listener is not None:
            self.__listener.update(self.__bytesRead, self.__contentLength, self.__items)

    def noteItem(self) -> None:

        self.__items += 1
        self.__notifyListener()

    def noteBytesRead(self, pBytes: int) -> None:

        self.__bytesRead += pBytes
        self.__notifyListener()

    def __init__(self, pListener: ProgressListener, pContentLength: int) -> None:

        self.__listener = pListener
        self.__contentLength = pContentLength

    # Class Methods End


class ItemInputStream(Closeable, io.BytesIO):

    # Class Fields Begin
    __total: int = None
    __pad: int = None
    __pos: int = None
    __closed: bool = None
    __BYTE_POSITIVE_OFFSET: int = 256
    # Class Fields End

    # Class Methods Begin
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
        self.head += res
        return res

    def read(self) -> int:

        return self.read0()

    def available(self) -> int:

        if self.__pos == -1:
            return self.tail - self.head - self.__pad
        return self.__pos - self.head

    def close1(self, pCloseUnderlying: bool) -> None:

        if self.closed:
            return
        if pCloseUnderlying:
            self.closed = True
            self.input.close()
        else:
            while True:
                av = self.available()
                if av == 0:
                    av = self.__makeAvailable()
                    if av == 0:
                        break
                self.skip(av)
        self.closed = True

    def close0(self) -> None:

        self.close1(False)

    def read1(self, b: typing.List[int], off: int, len: int) -> int:

        if self.closed:
            raise FileItemStream.ItemSkippedException()
        if len == 0:
            return 0
        res = self.available()
        if res == 0:
            res = self.__makeAvailable()
            if res == 0:
                return -1
        res = min(res, len)
        b[off : off + res] = self.buffer[self.head : self.head + res]
        self.head += res
        self.total += res
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
        self.__total += self.tail - self.head - self.__pad
        self.buffer = self.buffer[: self.__pad]
        self.head = 0
        self.tail = self.__pad
        while True:
            bytes_read = self.input.read(
                self.buffer, self.tail, self.bufSize - self.tail
            )
            if bytes_read == -1:
                raise MalformedStreamException("Stream ended unexpectedly")
            if self.notifier:
                self.notifier.noteBytesRead(bytes_read)
            self.tail += bytes_read
            self.__findSeparator()
            av = self.available()
            if av > 0 or self.__pos != -1:
                return av

    def __findSeparator(self) -> None:

        self.__pos = self._findSeparator()
        if self.__pos == -1:
            if self.tail - self.head > self.__keepRegion:
                self.__pad = self.__keepRegion
            else:
                self.__pad = self.tail - self.head

    def __init__(self) -> None:

        self.__findSeparator()

    # Class Methods End

class MultipartStream:

    # Class Fields Begin
    CR: int = ""  # LLM could not translate field
    LF: int = 0x0A
    DASH: int = ""  # LLM could not translate field
    HEADER_PART_SIZE_MAX: int = 10240
    _DEFAULT_BUFSIZE: int = ""  # LLM could not translate field
    _HEADER_SEPARATOR: bytes = b"\r\n\r\n"
    _FIELD_SEPARATOR: typing.List[int] = ""  # LLM could not translate field
    _STREAM_TERMINATOR: bytes = b"--\n"
    _BOUNDARY_PREFIX: bytes = b"\r\n--"
    __input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    __boundaryLength: int = None
    __keepRegion: int = None
    __boundary: typing.List[int] = None
    __boundaryTable: typing.List[int] = None
    __bufSize: int = None
    __buffer: typing.List[int] = None
    __head: int = None
    __tail: int = None
    __headerEncoding: str = None
    __notifier: ProgressNotifier = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def MultipartStream3(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
    ) -> "MultipartStream":

        pass  # LLM could not translate method body

    @staticmethod
    def MultipartStream1(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        bufSize: int,
    ) -> "MultipartStream":

        pass  # LLM could not translate method body

    @staticmethod
    def MultipartStream0() -> "MultipartStream":

        pass  # LLM could not translate method body

    def _findSeparator(self) -> int:

        buffer_pos = self.__head
        table_pos = 0
        while buffer_pos < self.__tail:
            while (
                table_pos >= 0
                and self.__buffer[buffer_pos] != self.__boundary[table_pos]
            ):
                table_pos = self.__boundaryTable[table_pos]
            buffer_pos += 1
            table_pos += 1
            if table_pos == self.__boundaryLength:
                return buffer_pos - self.__boundaryLength
        return -1

    def _findByte(self, value: int, pos: int) -> int:

        for i in range(pos, self.__tail):
            if self.__buffer[i] == value:
                return i
        return -1

    @staticmethod
    def arrayequals(a: typing.List[int], b: typing.List[int], count: int) -> bool:

        pass  # LLM could not translate method body

    def readHeaders(self) -> str:

        i = 0
        b = 0
        baos = io.BytesIO()
        size = 0
        while i < self._HEADER_SEPARATOR:
            try:
                b = self.readByte()
            except FileUploadIOException as e:
                raise e
            except IOError as e:
                raise MalformedStreamException("Stream ended unexpectedly")
            if size > self.HEADER_PART_SIZE_MAX:
                raise MalformedStreamException(
                    "Header section has more than {} bytes (maybe it is not properly"
                    + " terminated)".format(self.HEADER_PART_SIZE_MAX)
                )
            if b == self._HEADER_SEPARATOR[i]:
                i += 1
            else:
                i = 0
            baos.write(b)
        headers = None
        if self.__headerEncoding is not None:
            try:
                headers = baos.getvalue().decode(self.__headerEncoding)
            except UnicodeError:
                headers = baos.getvalue()
        else:
            headers = baos.getvalue()
        return headers

    def setBoundary(self, boundary: typing.List[int]) -> None:

        if len(boundary) != self.__boundaryLength - len(self._BOUNDARY_PREFIX):
            raise IllegalBoundaryException(
                "The length of a boundary token cannot be changed"
            )
        boundary.copy_to(self.__boundary, self._BOUNDARY_PREFIX.length, len(boundary))
        self.__computeBoundaryTable()

    def readBoundary(self) -> bool:

        marker = bytearray(2)
        next_chunk = False
        self.__head += self.__boundaryLength
        try:
            marker[0] = self.readByte()
            if marker[0] == self.LF:
                return True
            marker[1] = self.readByte()
            if self.arrayequals(marker, self._STREAM_TERMINATOR, 2):
                next_chunk = False
            elif self.arrayequals(marker, self._FIELD_SEPARATOR, 2):
                next_chunk = True
            else:
                raise MalformedStreamException(
                    "Unexpected characters follow a boundary"
                )
        except FileUploadIOException as e:
            raise e
        except IOException as e:
            raise MalformedStreamException("Stream ended unexpectedly")
        return next_chunk

    def readByte(self) -> int:

        if self.__head == self.__tail:
            self.__head = 0
            self.__tail = self.__input.read(self.__buffer, self.__head, self.__bufSize)
            if self.__tail == -1:
                raise IOError("No more data is available")
            if self.__notifier is not None:
                self.__notifier.noteBytesRead(self.__tail)
        return self.__buffer[self.__head]

    def setHeaderEncoding(self, encoding: str) -> None:

        self.__headerEncoding = encoding

    def getHeaderEncoding(self) -> str:

        return self.__headerEncoding

    @staticmethod
    def MultipartStream2(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        pNotifier: ProgressNotifier,
    ) -> "MultipartStream":

        pass  # LLM could not translate method body

    def __init__(
        self,
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        bufSize: int,
        pNotifier: ProgressNotifier,
    ) -> None:

        if boundary is None:
            raise ValueError("boundary may not be None")
        self.boundaryLength = len(boundary) + len(self._BOUNDARY_PREFIX)
        if bufSize < self.boundaryLength + 1:
            raise ValueError(
                "The buffer size specified for the MultipartStream is too small"
            )
        self.input = input
        self.bufSize = max(bufSize, self.boundaryLength * 2)
        self.buffer = bytearray(self.bufSize)
        self.notifier = pNotifier
        self.boundary = bytearray(self.boundaryLength)
        self.boundaryTable = [0] * (self.boundaryLength + 1)
        self.keepRegion = len(self.boundary)
        self.boundary[: len(self._BOUNDARY_PREFIX)] = self._BOUNDARY_PREFIX
        self.boundary[len(self._BOUNDARY_PREFIX) :] = boundary
        self.__computeBoundaryTable()
        self.head = 0
        self.tail = 0

    def __computeBoundaryTable(self) -> None:

        position = 2
        candidate = 0
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

    # Class Methods End


class IllegalBoundaryException(OSError):

    # Class Fields Begin
    __serialVersionUID: int = -161533165102632918
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:

        super().__init__(message)

    # Class Methods End


class MalformedStreamException(OSError):

    # Class Fields Begin
    __serialVersionUID: int = 6466926458059796677
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:

        super().__init__(message)

    # Class Methods End

