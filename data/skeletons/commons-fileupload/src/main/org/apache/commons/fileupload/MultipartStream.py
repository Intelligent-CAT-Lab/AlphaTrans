from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.util.Closeable import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
from src.main.org.apache.commons.fileupload.FileUploadBase import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class ItemInputStream:

    # Class Fields Begin
    __total: int = None
    __pad: int = None
    __pos: int = None
    __closed: bool = None
    __BYTE_POSITIVE_OFFSET: int = None
    # Class Fields End

    # Class Methods Begin
    def isClosed(self) -> bool:
        pass

    def skip(self, bytes_: int) -> int:
        pass

    def read(self) -> int:
        pass

    def available(self) -> int:
        pass

    def close1(self, pCloseUnderlying: bool) -> None:
        pass

    def close0(self) -> None:
        pass

    def read1(self, b: typing.List[int], off: int, len_: int) -> int:
        pass

    def read0(self) -> int:
        pass

    def getBytesRead(self) -> int:
        pass

    def __makeAvailable(self) -> int:
        pass

    def __findSeparator(self) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class IllegalBoundaryException:

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:
        pass

    # Class Methods End


class MalformedStreamException:

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:
        pass

    # Class Methods End


class ProgressNotifier:

    # Class Fields Begin
    __listener: ProgressListener = None
    __contentLength: int = None
    __bytesRead: int = None
    __items: int = None
    # Class Fields End

    # Class Methods Begin
    def __notifyListener(self) -> None:
        pass

    def noteItem(self) -> None:
        pass

    def noteBytesRead(self, pBytes: int) -> None:
        pass

    def __init__(self, pListener: ProgressListener, pContentLength: int) -> None:
        pass

    # Class Methods End


class MultipartStream:

    # Class Fields Begin
    CR: int = None
    LF: int = None
    DASH: int = None
    HEADER_PART_SIZE_MAX: int = None
    _DEFAULT_BUFSIZE: int = None
    _HEADER_SEPARATOR: typing.List[int] = None
    _FIELD_SEPARATOR: typing.List[int] = None
    _STREAM_TERMINATOR: typing.List[int] = None
    _BOUNDARY_PREFIX: typing.List[int] = None
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
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
    ) -> MultipartStream:
        pass

    @staticmethod
    def MultipartStream1(
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        bufSize: int,
    ) -> MultipartStream:
        pass

    @staticmethod
    def MultipartStream0() -> MultipartStream:
        pass

    def _findSeparator(self) -> int:
        pass

    def _findByte(self, value: int, pos: int) -> int:
        pass

    @staticmethod
    def arrayequals(a: typing.List[int], b: typing.List[int], count: int) -> bool:
        pass

    def readHeaders(self) -> str:
        pass

    def setBoundary(self, boundary: typing.List[int]) -> None:
        pass

    def readBoundary(self) -> bool:
        pass

    def readByte(self) -> int:
        pass

    def setHeaderEncoding(self, encoding: str) -> None:
        pass

    def getHeaderEncoding(self) -> str:
        pass

    @staticmethod
    def MultipartStream2(
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        pNotifier: ProgressNotifier,
    ) -> MultipartStream:
        pass

    def __init__(
        self,
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        boundary: typing.List[int],
        bufSize: int,
        pNotifier: ProgressNotifier,
    ) -> None:
        pass

    def __computeBoundaryTable(self) -> None:
        pass

    def newInputStream(self) -> ItemInputStream:
        pass

    # Class Methods End
