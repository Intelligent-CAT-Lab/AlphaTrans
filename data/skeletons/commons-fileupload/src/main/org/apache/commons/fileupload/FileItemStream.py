# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *
import typing
import io
from abc import ABC

# Imports End


class FileItemStream(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def isFormField(self) -> bool:
        pass

    def getFieldName(self) -> str:
        pass

    def getName(self) -> str:
        pass

    def getContentType(self) -> str:
        pass

    def openStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        pass

    # Class Methods End


class ItemSkippedException(IOException):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End
