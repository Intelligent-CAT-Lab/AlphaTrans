from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.FileItem import *
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from src.main.org.apache.commons.fileupload.FileUploadException import *
from src.main.org.apache.commons.fileupload.ParameterParser import *
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.RequestContext import *
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *


class FileUploadIOException:

    __cause: FileUploadException = None

    serialVersionUID: int = -7047616958165584154

    def getCause(self) -> BaseException:
        return self.__cause

    def __init__(self, pCause: FileUploadException) -> None:
        self.__cause = pCause


class IOFileUploadException(FileUploadException):

    __cause: typing.Union[IOError, OSError] = None

    serialVersionUID: int = 1749796615868477269

    def getCause(self) -> BaseException:
        return self.__cause

    def __init__(self, pMsg: str, pException: typing.Union[IOError, OSError]) -> None:
        super().__init__(pMsg, pException)
        self.__cause = pException


class FileItemStreamImpl:

    __headers: FileItemHeaders = None

    __opened: bool = False

    def setHeaders(self, pHeaders: FileItemHeaders) -> None:
        self.__headers = pHeaders

    def getHeaders(self) -> FileItemHeaders:
        return self.__headers


class FileItemIteratorImpl:

    __eof: bool = False

    __itemValid: bool = False

    __skipPreamble: bool = False

    __currentFieldName: str = ""

    __currentItem: FileItemStreamImpl = None

    def __getContentLength(self, pHeaders: FileItemHeaders) -> int:
        try:
            return int(pHeaders.getHeader("Content-Length"))
        except Exception:
            return -1


class SizeException(FileUploadException, ABC):

    __permitted: int = 0

    __actual: int = 0

    __serialVersionUID: int = -8776225574705254126

    def getPermittedSize(self) -> int:
        return self.__permitted

    def getActualSize(self) -> int:
        return self.__actual

    def __init__(self, message: str, actual: int, permitted: int) -> None:
        super().__init__(message, None)
        self.__actual = actual
        self.__permitted = permitted


class InvalidContentTypeException(FileUploadException):

    serialVersionUID: int = -9073026332015646668

    def __init__(self, msg: str, cause: BaseException) -> None:
        super().__init__(msg)
        self.__cause = cause


class UnknownSizeException(FileUploadException):

    serialVersionUID: int = 7062279004812015273

    def __init__(self, message: str) -> None:
        super().__init__(message, None)


class SizeLimitExceededException(SizeException):

    serialVersionUID: int = -2474893167098052828

    @staticmethod
    def SizeLimitExceededException1(message: str) -> SizeLimitExceededException:
        return SizeLimitExceededException(message, 0, 0)

    @staticmethod
    def SizeLimitExceededException0() -> SizeLimitExceededException:
        return SizeLimitExceededException(None, 0, 0)

    def __init__(self, message: str, actual: int, permitted: int) -> None:
        super().__init__(message, actual, permitted)


class FileSizeLimitExceededException(SizeException):

    __fieldName: str = ""

    __fileName: str = ""

    serialVersionUID: int = 8150776562029630058

    def setFieldName(self, pFieldName: str) -> None:
        self.__fieldName = pFieldName

    def getFieldName(self) -> str:
        return self.__fieldName

    def setFileName(self, pFileName: str) -> None:
        self.__fileName = pFileName

    def getFileName(self) -> str:
        return self.__fileName

    def __init__(self, message: str, actual: int, permitted: int) -> None:
        super().__init__(message, actual, permitted)


class FileUploadBase(ABC):

    MAX_HEADER_SIZE: int = 1024
    MULTIPART_MIXED: str = "multipart/mixed"
    MULTIPART_FORM_DATA: str = "multipart/form-data"
    MULTIPART: str = "multipart/"
    ATTACHMENT: str = "attachment"
    FORM_DATA: str = "form-data"
    CONTENT_LENGTH: str = "Content-length"
    CONTENT_DISPOSITION: str = "Content-disposition"
    CONTENT_TYPE: str = "Content-type"
    __listener: ProgressListener = None

    __headerEncoding: str = ""

    __fileCountMax: int = -1
    __fileSizeMax: int = -1
    __sizeMax: int = -1

    def _getHeader(self, headers: typing.Dict[str, str], name: str) -> str:
        return headers.get(name.lower())

    def _parseHeaders(self, headerPart: str) -> typing.Dict[str, str]:
        headers = self._getParsedHeaders(headerPart)
        result = {}
        for headerName in headers.getHeaderNames():
            headerValue = StringBuilder(headers.getHeaders(headerName).next())
            for header in headers.getHeaders(headerName):
                headerValue.append(",").append(header)
            result[headerName] = headerValue.toString()
        return result

    def _createItem(
        self, headers: typing.Dict[str, str], isFormField: bool
    ) -> FileItem:
        return self.getFileItemFactory().createItem(
            self._getFieldName2(headers),
            self._getHeader(headers, self.CONTENT_TYPE),
            isFormField,
            self._getFileName0(headers),
        )

    def _getFieldName2(self, headers: typing.Dict[str, str]) -> str:
        return self.__getFieldName1(self._getHeader(headers, self.CONTENT_DISPOSITION))

    def _getFileName0(self, headers: typing.Dict[str, str]) -> str:
        return self.__getFileName2(self._getHeader(headers, self.CONTENT_DISPOSITION))

    def setProgressListener(self, pListener: ProgressListener) -> None:
        self.__listener = pListener

    def getProgressListener(self) -> ProgressListener:
        return self.__listener

    def _newFileItemHeaders(self) -> FileItemHeadersImpl:
        return FileItemHeadersImpl()

    def _getParsedHeaders(self, headerPart: str) -> FileItemHeaders:
        len_ = len(headerPart)
        headers = self._newFileItemHeaders()
        start = 0
        while True:
            end = self.__parseEndOfLine(headerPart, start)
            if start == end:
                break
            header = StringBuilder(headerPart[start:end])
            start = end + 2
            while start < len_:
                non_ws = start
                while non_ws < len_:
                    c = headerPart[non_ws]
                    if c != " " and c != "\t":
                        break
                    non_ws += 1
                if non_ws == start:
                    break
                end = self.__parseEndOfLine(headerPart, non_ws)
                header.append(" ").append(headerPart[non_ws:end])
                start = end + 2
            self.__parseHeaderLine(headers, header.toString())
        return headers

    def _getFieldName0(self, headers: FileItemHeaders) -> str:
        return self.__getFieldName1(headers.getHeader(self.CONTENT_DISPOSITION))

    def _getFileName1(self, headers: FileItemHeaders) -> str:
        return self.__getFileName2(headers.getHeader(self.CONTENT_DISPOSITION))

    def _getBoundary(self, contentType: str) -> typing.List[int]:
        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse0(contentType, [b";", b","])
        boundaryStr = params.get("boundary")
        if boundaryStr is None:
            return None
        boundary: typing.List[int]
        try:
            boundary = boundaryStr.encode("ISO-8859-1")
        except UnicodeEncodeError:
            boundary = (
                boundaryStr.encode()
            )  # Intentionally falls back to default charset
        return boundary

    def setHeaderEncoding(self, encoding: str) -> None:
        self.__headerEncoding = encoding

    def getHeaderEncoding(self) -> str:
        return self.__headerEncoding

    def setFileCountMax(self, fileCountMax: int) -> None:
        self.__fileCountMax = fileCountMax

    def getFileCountMax(self) -> int:
        return self.__fileCountMax

    def setFileSizeMax(self, fileSizeMax: int) -> None:
        self.__fileSizeMax = fileSizeMax

    def getFileSizeMax(self) -> int:
        return self.__fileSizeMax

    def setSizeMax(self, sizeMax: int) -> None:
        self.__sizeMax = sizeMax

    def getSizeMax(self) -> int:
        return self.__sizeMax

    @staticmethod
    def isMultipartContent(ctx: RequestContext) -> bool:
        contentType = ctx.getContentType()
        if contentType is None:
            return False
        if contentType.lower().startswith(FileUploadBase.MULTIPART):
            return True
        return False

    def __parseHeaderLine(self, headers: FileItemHeadersImpl, header: str) -> None:
        colon_offset = header.index(":")
        if colon_offset == -1:
            return
        header_name = header[0:colon_offset].strip()
        header_value = header[header.index(":") + 1 :].strip()
        headers.addHeader(header_name, header_value)

    def __parseEndOfLine(self, headerPart: str, end: int) -> int:
        index = end
        while True:
            offset = headerPart.find("\r", index)
            if offset == -1 or offset + 1 >= len(headerPart):
                raise RuntimeError(
                    "Expected headers to be terminated by an empty line."
                )
            if headerPart[offset + 1] == "\n":
                return offset
            index = offset + 1

    def __getFieldName1(self, pContentDisposition: str) -> str:
        fieldName: str = None
        if pContentDisposition is not None and pContentDisposition.lower().startswith(
            self.FORM_DATA
        ):
            parser: ParameterParser = ParameterParser()
            parser.setLowerCaseNames(True)
            params: typing.Dict[str, str] = parser.parse1(pContentDisposition, ";")
            fieldName = params.get("name")
            if fieldName is not None:
                fieldName = fieldName.strip()
        return fieldName

    def __getFileName2(self, pContentDisposition: str) -> str:
        fileName: str = None
        if pContentDisposition is not None:
            cdl: str = pContentDisposition.lower()
            if cdl.startswith(self.FORM_DATA) or cdl.startswith(self.ATTACHMENT):
                parser: ParameterParser = ParameterParser()
                parser.setLowerCaseNames(True)
                params: typing.Dict[str, str] = parser.parse1(pContentDisposition, ";")
                if params.containsKey("filename"):
                    fileName = params.get("filename")
                    if fileName is not None:
                        fileName = fileName.strip()
                    else:
                        fileName = ""
        return fileName

    def setFileItemFactory(self, factory: FileItemFactory) -> None:
        self.fileItemFactory = factory

    def getFileItemFactory(self) -> FileItemFactory:
        return self.fileItemFactory
