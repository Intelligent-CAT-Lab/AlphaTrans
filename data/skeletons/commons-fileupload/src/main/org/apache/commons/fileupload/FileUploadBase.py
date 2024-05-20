from __future__ import annotations

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
import io
from abc import ABC

# Imports End


class FileUploadIOException:

    # Class Fields Begin
    __serialVersionUID: int = None
    __cause: FileUploadException = None
    # Class Fields End

    # Class Methods Begin
    def getCause(self) -> BaseException:
        pass

    def __init__(self, pCause: FileUploadException) -> None:
        pass

    # Class Methods End


class IOFileUploadException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __cause: typing.Union[IOError, OSError] = None
    # Class Fields End

    # Class Methods Begin
    def getCause(self) -> BaseException:
        pass

    def __init__(self, pMsg: str, pException: typing.Union[IOError, OSError]) -> None:
        pass

    # Class Methods End


class FileItemStreamImpl:

    # Class Fields Begin
    __opened: bool = None
    __headers: FileItemHeaders = None
    # Class Fields End

    # Class Methods Begin
    def setHeaders(self, pHeaders: FileItemHeaders) -> None:
        pass

    def getHeaders(self) -> FileItemHeaders:
        pass

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
        pass

    # Class Methods End


class SizeException(FileUploadException, ABC):

    # Class Fields Begin
    __serialVersionUID: int = None
    __actual: int = None
    __permitted: int = None
    # Class Fields End

    # Class Methods Begin
    def getPermittedSize(self) -> int:
        pass

    def getActualSize(self) -> int:
        pass

    def __init__(self, message: str, actual: int, permitted: int) -> None:
        pass

    # Class Methods End


class InvalidContentTypeException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, msg: str, cause: BaseException) -> None:
        pass

    # Class Methods End


class UnknownSizeException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:
        pass

    # Class Methods End


class SizeLimitExceededException(SizeException):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def SizeLimitExceededException1(message: str) -> SizeLimitExceededException:
        pass

    @staticmethod
    def SizeLimitExceededException0() -> SizeLimitExceededException:
        pass

    def __init__(self, message: str, actual: int, permitted: int) -> None:
        pass

    # Class Methods End


class FileSizeLimitExceededException(SizeException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __fileName: str = None
    __fieldName: str = None
    # Class Fields End

    # Class Methods Begin
    def setFieldName(self, pFieldName: str) -> None:
        pass

    def getFieldName(self) -> str:
        pass

    def setFileName(self, pFileName: str) -> None:
        pass

    def getFileName(self) -> str:
        pass

    def __init__(self, message: str, actual: int, permitted: int) -> None:
        pass

    # Class Methods End


class FileUploadBase(ABC):

    # Class Fields Begin
    MAX_HEADER_SIZE: int = None
    __sizeMax: int = None
    __fileSizeMax: int = None
    __fileCountMax: int = None
    __headerEncoding: str = None
    __listener: ProgressListener = None
    CONTENT_TYPE: str = None
    CONTENT_DISPOSITION: str = None
    CONTENT_LENGTH: str = None
    FORM_DATA: str = None
    ATTACHMENT: str = None
    MULTIPART: str = None
    MULTIPART_FORM_DATA: str = None
    MULTIPART_MIXED: str = None
    # Class Fields End

    # Class Methods Begin
    def _getHeader(self, headers: typing.Dict[str, str], name: str) -> str:
        pass

    def _parseHeaders(self, headerPart: str) -> typing.Dict[str, str]:
        pass

    def _createItem(
        self, headers: typing.Dict[str, str], isFormField: bool
    ) -> FileItem:
        pass

    def _getFieldName2(self, headers: typing.Dict[str, str]) -> str:
        pass

    def _getFileName0(self, headers: typing.Dict[str, str]) -> str:
        pass

    def setProgressListener(self, pListener: ProgressListener) -> None:
        pass

    def getProgressListener(self) -> ProgressListener:
        pass

    def _newFileItemHeaders(self) -> FileItemHeadersImpl:
        pass

    def _getParsedHeaders(self, headerPart: str) -> FileItemHeaders:
        pass

    def _getFieldName0(self, headers: FileItemHeaders) -> str:
        pass

    def _getFileName1(self, headers: FileItemHeaders) -> str:
        pass

    def _getBoundary(self, contentType: str) -> typing.List[int]:
        pass

    def setHeaderEncoding(self, encoding: str) -> None:
        pass

    def getHeaderEncoding(self) -> str:
        pass

    def setFileCountMax(self, fileCountMax: int) -> None:
        pass

    def getFileCountMax(self) -> int:
        pass

    def setFileSizeMax(self, fileSizeMax: int) -> None:
        pass

    def getFileSizeMax(self) -> int:
        pass

    def setSizeMax(self, sizeMax: int) -> None:
        pass

    def getSizeMax(self) -> int:
        pass

    @staticmethod
    def isMultipartContent(ctx: RequestContext) -> bool:
        pass

    def __parseHeaderLine(self, headers: FileItemHeadersImpl, header: str) -> None:
        pass

    def __parseEndOfLine(self, headerPart: str, end: int) -> int:
        pass

    def __getFieldName1(self, pContentDisposition: str) -> str:
        pass

    def __getFileName2(self, pContentDisposition: str) -> str:
        pass

    def setFileItemFactory(self, factory: FileItemFactory) -> None:
        pass

    def getFileItemFactory(self) -> FileItemFactory:
        pass

    # Class Methods End
