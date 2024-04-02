# Imports Begin
import typing
from typing import *
from io import BytesIO
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

        raise NotImplementedError

    def getContentLength(self) -> int:

        pass

    def getContentType(self) -> str:

        pass

    def getCharacterEncoding(self) -> str:

        pass

    # Class Methods End
