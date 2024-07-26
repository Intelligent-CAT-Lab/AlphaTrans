from __future__ import annotations
import re
import pathlib
import io
import os
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *


class DiskFileItemFactory:

    DEFAULT_SIZE_THRESHOLD: int = 10240
    defaultCharset: str = DiskFileItem.DEFAULT_CHARSET
    __sizeThreshold: int = DEFAULT_SIZE_THRESHOLD
    __repository: pathlib.Path = None

    def setDefaultCharset(self, pCharset: str) -> None:
        self.defaultCharset = pCharset

    def getDefaultCharset(self) -> str:
        return self.defaultCharset

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
        return DiskFileItemFactory(DiskFileItemFactory.DEFAULT_SIZE_THRESHOLD, None)

    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:
        self.__sizeThreshold = sizeThreshold
        self.__repository = repository
