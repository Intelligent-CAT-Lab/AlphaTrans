import pytest

# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
from abc import ABC

# Imports End


class FileItemHeadersSupport(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def setHeaders(self, headers: FileItemHeaders) -> None:

        self.headers = headers

    def getHeaders(self) -> FileItemHeaders:

        return self._headers

    # Class Methods End
