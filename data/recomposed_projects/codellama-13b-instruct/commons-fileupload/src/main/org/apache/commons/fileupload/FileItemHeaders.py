# Imports Begin
import typing
from typing import *
from abc import ABC

# Imports End


class FileItemHeaders(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getHeaderNames(self) -> typing.Iterator[str]:

        return self.headers.keys()

    def getHeaders(self, name: str) -> typing.Iterator[str]:

        return self.headers.get(name)

    def getHeader(self, name: str) -> str:

        return name

    # Class Methods End
