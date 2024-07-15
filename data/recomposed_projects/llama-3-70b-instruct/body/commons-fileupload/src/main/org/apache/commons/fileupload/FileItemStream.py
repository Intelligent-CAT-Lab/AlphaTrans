from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *


class ItemSkippedException:

    __serialVersionUID: int = -7280778431581963740


class FileItemStream(ABC):

    def isFormField(self) -> bool:
        return False

    def getFieldName(self) -> str:
        return self.fieldName

    def getName(self) -> str:
        return self.name

    def getContentType(self) -> str:
        return self.headers.get("Content-Type")

    def openStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        return io.BytesIO()
