from __future__ import annotations
import re
import io
from src.main.org.apache.commons.fileupload.FileUploadException import *


class FileCountLimitExceededException(FileUploadException):

    __limit: int = 0

    __serialVersionUID: int = 6904179610227521789

    def getLimit(self) -> int:
        return self.__limit

    def __init__(self, message: str, limit: int) -> None:
        super().__init__(message, None)
        self.__limit = limit
