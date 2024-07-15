import pytest

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class RequestContext(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:

        return io.BytesIO(self.getBytes())

    def getContentLength(self) -> int:

        return self.contentLength

    def getContentType(self) -> str:

        return self.contentType

    def getCharacterEncoding(self) -> str:

        return "UTF-8"

    # Class Methods End
