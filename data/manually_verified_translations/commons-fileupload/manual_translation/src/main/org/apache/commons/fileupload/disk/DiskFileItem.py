from __future__ import annotations
import re
import uuid
import pathlib
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from src.main.org.apache.commons.fileupload.ParameterParser import *
from src.main.org.apache.commons.fileupload.util.Streams import *


class DiskFileItem:

    DEFAULT_CHARSET: str = "ISO-8859-1"
    __defaultCharset: str = "ISO-8859-1"
    __headers: FileItemHeaders = None

    __tempFile: pathlib.Path = None

    __cachedContent: typing.List[int] = None

    __repository: pathlib.Path = None

    __sizeThreshold: int = 0

    __size: int = -1
    __fileName: str = ""

    __isFormField: bool = False

    __contentType: str = ""

    __fieldName: str = ""

    __COUNTER: int = 0
    __UID: str = uuid.uuid4().hex.replace("-", "_")

    def setDefaultCharset(self, charset: str) -> None:
        self.__defaultCharset = charset

    def getDefaultCharset(self) -> str:
        return self.__defaultCharset

    def setHeaders(self, pHeaders: FileItemHeaders) -> None:
        self.__headers = pHeaders

    def getHeaders(self) -> FileItemHeaders:
        return self.__headers

    def _getTempFile(self) -> pathlib.Path:

        if self.__tempFile is None:
            tempDir = self.__repository
            if tempDir is None:
                tempDir = pathlib.Path(
                    os.getenv("TMPDIR")
                    or os.getenv("TMP")
                    or os.getenv("TEMP")
                    or "/tmp"
                )

            tempFileName = f"upload_{self.__UID}_{self.__getUniqueId()}.tmp"

            self.__tempFile = tempDir / tempFileName

        return self.__tempFile

    def setFormField(self, state: bool) -> None:
        self.__isFormField = state

    def isFormField(self) -> bool:
        return self.isFormField

    def setFieldName(self, fieldName: str) -> None:
        self.__fieldName = fieldName

    def getFieldName(self) -> str:
        return self.__fieldName

    def getName(self) -> str:

        return Streams.checkFileName(self.__fileName)

    def getCharSet(self) -> str:
        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse1(self.getContentType(), ";")
        return params.get("charset")

    def getContentType(self) -> str:
        return self.__contentType

    def __init__(
        self,
        fieldName: str,
        contentType: str,
        isFormField: bool,
        fileName: str,
        sizeThreshold: int,
        repository: pathlib.Path,
    ) -> None:

        self.__fieldName = fieldName
        self.__contentType = contentType
        self.__isFormField = isFormField
        self.__fileName = fileName
        self.__sizeThreshold = sizeThreshold
        self.__repository = repository

    @staticmethod
    def __getUniqueId() -> str:

        limit = 100000000
        current = DiskFileItem.__COUNTER
        DiskFileItem.__COUNTER += 1
        id = str(current)

        if current < limit:
            id = ("00000000" + id)[-8:]
        return id
