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
    def getInputStream(self) -> io.BytesIO:

        return io.BytesIO(self.getBytes())

    def getContentLength(self) -> int:

        return self.contentLength

    def getContentType(self) -> str:

        return self.contentType

    def getCharacterEncoding(self) -> str:

        return self.characterEncoding

    # Class Methods End
