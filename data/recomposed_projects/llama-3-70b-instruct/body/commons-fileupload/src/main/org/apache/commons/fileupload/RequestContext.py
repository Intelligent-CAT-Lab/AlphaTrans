from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class RequestContext(ABC):

    def getInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        return io.BytesIO()

    def getContentLength(self) -> int:
        return self.content_length

    def getContentType(self) -> str:
        return self.contentType

    def getCharacterEncoding(self) -> str:
        return "UTF-8"
