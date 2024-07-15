from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadException import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class FileItemIterator(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def next_(self) -> FileItemStream:
        pass

    def hasNext(self) -> bool:
        pass

    # Class Methods End
