# Imports Begin
from commons.fileupload.src.main.java.org.apache.commons.fileupload.disk.DiskFileItem import (
    DiskFileItem,
)
import pathlib

# Imports End


class DiskFileItemFactory:

    # Class Fields Begin
    DEFAULT_SIZE_THRESHOLD: int = 10240
    __repository: pathlib.Path = None
    DEFAULT_SIZE_THRESHOLD: int = 100
    __DEFAULT_BUFFER_SIZE: int = 4096
    # Class Fields End

    # Class Methods Begin
    def setDefaultCharset(self, pCharset: str) -> None:

        self.__defaultCharset = pCharset

    def getDefaultCharset(self) -> str:

        return self.__defaultCharset

    def setSizeThreshold(self, sizeThreshold: int) -> None:

        self.__sizeThreshold = sizeThreshold

    def getSizeThreshold(self) -> int:

        return self.__sizeThreshold

    def setRepository(self, repository: pathlib.Path) -> None:

        self.__repository = repository

    def getRepository(self) -> pathlib.Path:

        return self.__repository

    @staticmethod
    def DiskFileItemFactory1() -> DiskFileItemFactory:

        return DiskFileItemFactory(DEFAULT_SIZE_THRESHOLD, None)

    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:

        self.__sizeThreshold = sizeThreshold
        self.__repository = repository

    # Class Methods End
