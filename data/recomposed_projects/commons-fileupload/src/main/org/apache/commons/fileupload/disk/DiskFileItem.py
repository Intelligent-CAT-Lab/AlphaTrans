# Imports Begin
from src.main.org.apache.commons.fileupload.util.Streams import *
from src.main.org.apache.commons.fileupload.ParameterParser import *
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import typing
from typing import *
import pathlib

# Imports End


class DiskFileItem:

    # Class Fields Begin
    __headers: FileItemHeaders = None
    __defaultCharset: str = ""  # LLM could not translate field
    DEFAULT_CHARSET: str = ""  # LLM could not translate field
    __UID: str = str(uuid.uuid4()).replace("-", "_")
    __COUNTER: int = 0
    __fieldName: str = None
    __contentType: str = None
    __isFormField: bool = None
    __fileName: str = None
    __size: int = ""  # LLM could not translate field
    __sizeThreshold: int = None
    __repository: pathlib.Path = None
    __cachedContent: typing.List[int] = None
    __tempFile: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
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
            temp_dir = self.__repository
            if temp_dir is None:
                temp_dir = pathlib.Path(os.getenv("java.io.tmpdir"))
            temp_file_name = f"upload_{self.__UID}_{self.__getUniqueId()}.tmp"
            self.__tempFile = temp_dir / temp_file_name
        return self.__tempFile

    def setFormField(self, state: bool) -> None:

        self.__isFormField = state

    def isFormField(self) -> bool:

        return self.__isFormField

    def setFieldName(self, fieldName: str) -> None:

        self.__fieldName = fieldName

    def getFieldName(self) -> str:

        return self.__fieldName

    def getName(self) -> str:

        return self.checkFileName(self.__fileName)

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

        pass  # LLM could not translate method body

    # Class Methods End
