from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.Streams import *
from src.main.org.apache.commons.fileupload.ParameterParser import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class DiskFileItem:

    # Class Fields Begin
    __headers: FileItemHeaders = None
    __defaultCharset: str = None
    DEFAULT_CHARSET: str = None
    __UID: str = None
    __COUNTER: int = None
    __fieldName: str = None
    __contentType: str = None
    __isFormField: bool = None
    __fileName: str = None
    __size: int = None
    __sizeThreshold: int = None
    __repository: pathlib.Path = None
    __cachedContent: typing.List[int] = None
    __tempFile: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    def setDefaultCharset(self, charset: str) -> None:
        pass

    def getDefaultCharset(self) -> str:
        pass

    def setHeaders(self, pHeaders: FileItemHeaders) -> None:
        pass

    def getHeaders(self) -> FileItemHeaders:
        pass

    def _getTempFile(self) -> pathlib.Path:
        pass

    def setFormField(self, state: bool) -> None:
        pass

    def isFormField(self) -> bool:
        pass

    def setFieldName(self, fieldName: str) -> None:
        pass

    def getFieldName(self) -> str:
        pass

    def getName(self) -> str:
        pass

    def getCharSet(self) -> str:
        pass

    def getContentType(self) -> str:
        pass

    def __init__(
        self,
        fieldName: str,
        contentType: str,
        isFormField: bool,
        fileName: str,
        sizeThreshold: int,
        repository: pathlib.Path,
    ) -> None:
        pass

    @staticmethod
    def __getUniqueId() -> str:
        pass

    # Class Methods End
