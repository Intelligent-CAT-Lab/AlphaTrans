from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeaders import *
import io
from abc import ABC

# Imports End


class FileItemHeadersSupport(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def setHeaders(self, headers: FileItemHeaders) -> None:
        pass

    def getHeaders(self) -> FileItemHeaders:
        pass

    # Class Methods End
