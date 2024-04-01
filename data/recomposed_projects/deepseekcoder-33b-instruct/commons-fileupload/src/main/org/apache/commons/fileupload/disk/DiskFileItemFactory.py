# Imports Begin
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *
import os
import pathlib

# Imports End


class DiskFileItemFactory:

    # Class Fields Begin
    DEFAULT_SIZE_THRESHOLD: int = 10240
    __repository: pathlib.Path = None
    __sizeThreshold: int = DEFAULT_SIZE_THRESHOLD
    __defaultCharset: str = DiskFileItem.DEFAULT_CHARSET
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
    def DiskFileItemFactory1() -> "DiskFileItemFactory":

        pass  # LLM could not translate method body

    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:

        self.__sizeThreshold = sizeThreshold
        self.__repository = repository

    # Class Methods End
