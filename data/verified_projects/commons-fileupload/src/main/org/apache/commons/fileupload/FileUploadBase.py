import pytest

# Imports Begin
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *
from src.main.org.apache.commons.fileupload.RequestContext import *
from src.main.org.apache.commons.fileupload.ProgressListener import *
from src.main.org.apache.commons.fileupload.ParameterParser import *
from src.main.org.apache.commons.fileupload.FileUploadException import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileItem import *
import os
import typing
from typing import *
from abc import ABC

# Imports End


class FileUploadBase(ABC):

    # Class Fields Begin
    MAX_HEADER_SIZE: int = 1024
    __sizeMax: int = ""  # LLM could not translate field
    __fileSizeMax: int = -1
    __fileCountMax: int = ""  # LLM could not translate field
    __headerEncoding: str = None
    __listener: ProgressListener = None
    CONTENT_TYPE: str = "Content-type"
    CONTENT_DISPOSITION: str = "Content-disposition"
    CONTENT_LENGTH: str = "Content-length"
    FORM_DATA: str = "form-data"
    ATTACHMENT: str = "attachment"
    MULTIPART: str = "multipart/"
    MULTIPART_FORM_DATA: str = "multipart/form-data"
    MULTIPART_MIXED: str = "multipart/mixed"
    # Class Fields End

    # Class Methods Begin
    def _getHeader(self, headers: typing.Dict[str, str], name: str) -> str:

        return headers.get(name.lower())

    def _parseHeaders(self, headerPart: str) -> typing.Dict[str, str]:

        headers = self._getParsedHeaders(headerPart)
        result = {}
        for headerName in headers.getHeaderNames():
            headerValue = ",".join(headers.getHeaders(headerName))
            result[headerName] = headerValue
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

        headers = self._newFileItemHeaders()
        start = 0
        while start < len(headerPart):
            end = self.__parseEndOfLine(headerPart, start)
            if start == end:
                break
            header = headerPart[start:end]
            start = end + 2
            while start < len(headerPart):
                non_ws = start
                while non_ws < len(headerPart):
                    c = headerPart[non_ws]
                    if c not in " \t":
                        break
                    non_ws += 1
                if non_ws == start:
                    break
                end = self.__parseEndOfLine(headerPart, non_ws)
                header += " " + headerPart[non_ws:end]
                start = end + 2
            self.__parseHeaderLine(headers, header)
        return headers

    def _getFieldName0(self, headers: FileItemHeaders) -> str:

        return self.__getFieldName1(headers.getHeader(self.CONTENT_DISPOSITION))

    def _getFileName1(self, headers: FileItemHeaders) -> str:

        return self.__getFileName2(headers.getHeader(self.CONTENT_DISPOSITION))

    def _getBoundary(self, contentType: str) -> typing.List[int]:

        parser = ParameterParser()
        parser.setLowerCaseNames(True)
        params = parser.parse0(contentType, [";", ","])
        boundaryStr = params.get("boundary")
        if boundaryStr is None:
            return None
        try:
            boundary = boundaryStr.encode("ISO-8859-1")
        except UnicodeEncodeError:
            boundary = boundaryStr.encode()
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

        pass  # LLM could not translate method body

    def __parseHeaderLine(self, headers: FileItemHeadersImpl, header: str) -> None:

        colon_offset = header.find(":")
        if colon_offset == -1:
            return
        header_name = header[:colon_offset].strip()
        header_value = header[header.find(":") + 1 :].strip()
        headers.addHeader(header_name, header_value)

    def __parseEndOfLine(self, headerPart: str, end: int) -> int:

        index = end
        while True:
            offset = headerPart.find("\r", index)
            if offset == -1 or offset + 1 >= len(headerPart):
                raise IllegalStateException(
                    "Expected headers to be terminated by an empty line."
                )
            if headerPart[offset + 1] == "\n":
                return offset
            index = offset + 1

    def __getFieldName1(self, pContentDisposition: str) -> str:

        fieldName = None
        if pContentDisposition and pContentDisposition.lower().startswith(
            self.FORM_DATA
        ):
            parser = ParameterParser()
            parser.setLowerCaseNames(True)
            params = parser.parse1(pContentDisposition, ";")
            fieldName = params.get("name")
            if fieldName:
                fieldName = fieldName.strip()
        return fieldName

    def __getFileName2(self, pContentDisposition: str) -> str:

        fileName = None
        if pContentDisposition is not None:
            cdl = pContentDisposition.lower()
            if cdl.startswith(self.FORM_DATA) or cdl.startswith(self.ATTACHMENT):
                parser = ParameterParser()
                parser.setLowerCaseNames(True)
                params = parser.parse1(pContentDisposition, ";")
                if "filename" in params:
                    fileName = params["filename"]
                    if fileName is not None:
                        fileName = fileName.strip()
                    else:
                        fileName = ""
        return fileName

    def setFileItemFactory(self, factory: FileItemFactory) -> None:

        self.fileItemFactory = factory

    def getFileItemFactory(self) -> FileItemFactory:

        return self._fileItemFactory

    # Class Methods End


class FileUploadIOException(OSError):

    # Class Fields Begin
    __serialVersionUID: int = -7047616958165584154
    __cause: FileUploadException = None
    # Class Fields End

    # Class Methods Begin
    def getCause(self) -> BaseException:

        return self.__cause

    def __init__(self, pCause: FileUploadException) -> None:

        self.cause = pCause

    # Class Methods End


class IOFileUploadException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = 1749796615868477269
    __cause: typing.Union[IOError, OSError] = None
    # Class Fields End

    # Class Methods Begin
    def getCause(self) -> BaseException:

        return self.__cause

    def __init__(self, pMsg: str, pException: typing.Union[IOError, OSError]) -> None:

        super().__init__(pMsg, None)
        self.__cause = pException

    # Class Methods End
        
class SizeException(FileUploadException, ABC):

    # Class Fields Begin
    __serialVersionUID: int = -8776225574705254126
    __actual: int = None
    __permitted: int = None
    # Class Fields End

    # Class Methods Begin
    def getPermittedSize(self) -> int:

        return self.__permitted

    def getActualSize(self) -> int:

        return self.__actual

    def __init__(self, message: str, actual: int, permitted: int) -> None:

        super().__init__(message, None)
        self.__actual = actual
        self.__permitted = permitted

    # Class Methods End


class SizeLimitExceededException(SizeException):

    # Class Fields Begin
    __serialVersionUID: int = -2474893167098052828
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def SizeLimitExceededException1(message: str) -> "SizeLimitExceededException":

        return SizeLimitExceededException(message, 0, 0)

    @staticmethod
    def SizeLimitExceededException0() -> "SizeLimitExceededException":

        pass  # LLM could not translate method body

    def __init__(self, message: str, actual: int, permitted: int) -> None:

        super().__init__(message, actual, permitted)

    # Class Methods End


class FileItemStreamImpl:

    # Class Fields Begin
    __opened: bool = None
    __headers: FileItemHeaders = None
    # Class Fields End

    # Class Methods Begin
    def setHeaders(self, pHeaders: FileItemHeaders) -> None:

        self.__headers = pHeaders

    def getHeaders(self) -> FileItemHeaders:

        return self.__headers

    # Class Methods End


class FileItemIteratorImpl:

    # Class Fields Begin
    __currentItem: FileItemStreamImpl = None
    __currentFieldName: str = None
    __skipPreamble: bool = None
    __itemValid: bool = None
    __eof: bool = None
    # Class Fields End

    # Class Methods Begin
    def __getContentLength(self, pHeaders: FileItemHeaders) -> int:

        try:
            return int(pHeaders.getHeader(CONTENT_LENGTH))
        except Exception as e:
            return -1

    # Class Methods End


class FileSizeLimitExceededException(SizeException):

    # Class Fields Begin
    __serialVersionUID: int = 8150776562029630058
    __fileName: str = None
    __fieldName: str = None
    # Class Fields End

    # Class Methods Begin
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

    # Class Methods End


class InvalidContentTypeException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = -9073026332015646668
    # Class Fields End

    # Class Methods Begin
    def __init__(self, msg: str, cause: BaseException) -> None:

        super().__init__(msg, cause)

    # Class Methods End


class UnknownSizeException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = 7062279004812015273
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:

        super().__init__(message, None)

    # Class Methods End
