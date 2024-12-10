from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
import pathlib
from abc import ABC

# Imports End


class FileItem(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getOutputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:
        pass

    def setFormField(self, state: bool) -> None:
        pass

    def isFormField(self) -> bool:
        pass

    def setFieldName(self, name: str) -> None:
        pass

    def getFieldName(self) -> str:
        pass

    def delete(self) -> None:
        pass

    def write(self, file: pathlib.Path) -> None:
        pass

    def getString1(self) -> str:
        pass

    def getString0(self, encoding: str) -> str:
        pass

    def get(self) -> typing.List[int]:
        pass

    def getSize(self) -> int:
        pass

    def isInMemory(self) -> bool:
        pass

    def getName(self) -> str:
        pass

    def getContentType(self) -> str:
        pass

    def getInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        pass

    # Class Methods End
