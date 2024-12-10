from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *
import os
import io
import pathlib

# Imports End


class DiskFileItemFactory:

    # Class Fields Begin
    DEFAULT_SIZE_THRESHOLD: int = None
    __repository: pathlib.Path = None
    __sizeThreshold: int = None
    __defaultCharset: str = None
    # Class Fields End

    # Class Methods Begin
    def setDefaultCharset(self, pCharset: str) -> None:
        pass

    def getDefaultCharset(self) -> str:
        pass

    def setSizeThreshold(self, sizeThreshold: int) -> None:
        pass

    def getSizeThreshold(self) -> int:
        pass

    def setRepository(self, repository: pathlib.Path) -> None:
        pass

    def getRepository(self) -> pathlib.Path:
        pass

    @staticmethod
    def DiskFileItemFactory1() -> DiskFileItemFactory:
        pass

    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:
        pass

    # Class Methods End
