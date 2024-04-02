# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *
import typing
from typing import *
from io import BytesIO
import io
from abc import ABC

# Imports End


class ItemSkippedException(Exception):

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

        pass  # LLM could not translate method body

    def getFieldName(self) -> str:

        pass

    def getName(self) -> str:

        pass

    def getContentType(self) -> str:

        pass

    def openStream(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:

        raise NotImplementedError

    # Class Methods End
