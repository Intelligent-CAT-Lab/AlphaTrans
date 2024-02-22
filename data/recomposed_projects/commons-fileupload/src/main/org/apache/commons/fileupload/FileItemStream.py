# Imports Begin
from commons.fileupload.src.main.java.org.apache.commons.fileupload.ItemSkippedException import (
    ItemSkippedException,
)
from commons.fileupload.src.main.java.org.apache.commons.fileupload.FileItemHeadersSupport import (
    FileItemHeadersSupport,
)
from commons.fileupload.src.main.java.org.apache.commons.fileupload.FileItemStream import (
    FileItemStream,
)
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ItemSkippedException(IOException):

    # Class Fields Begin
    __serialVersionUID: int = -7280778431581963740
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class FileItemStream(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def isFormField(self) -> bool:

        return True

    def getFieldName(self) -> str:

        return self.fieldName

    def getName(self) -> str:

        return self.name

    def getContentType(self) -> str:

        return "text/html"

    def openStream(self) -> io.BytesIO:

        try:
            return io.BytesIO(self.read())
        except IOException as e:
            raise e

    # Class Methods End
