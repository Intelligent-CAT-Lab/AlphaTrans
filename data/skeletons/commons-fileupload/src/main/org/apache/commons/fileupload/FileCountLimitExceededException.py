from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadException import *
import io

# Imports End


class FileCountLimitExceededException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __limit: int = None
    # Class Fields End

    # Class Methods Begin
    def getLimit(self) -> int:
        pass

    def __init__(self, message: str, limit: int) -> None:
        pass

    # Class Methods End
