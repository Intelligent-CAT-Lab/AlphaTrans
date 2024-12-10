from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import typing
from typing import *
import io

# Imports End


class FileItemHeadersImpl(FileItemHeaders):

    # Class Fields Begin
    __serialVersionUID: int = None
    __headerNameToValueListMap: typing.Dict[str, typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def getHeaders(self, name: str) -> typing.Iterator[str]:
        pass

    def getHeaderNames(self) -> typing.Iterator[str]:
        pass

    def getHeader(self, name: str) -> str:
        pass

    def addHeader(self, name: str, value: str) -> None:
        pass

    # Class Methods End
