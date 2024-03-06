# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadException import *

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class FileCountLimitExceededException(FileUploadException):

    # Class Fields Begin
    __serialVersionUID: int = 6904179610227521789
    __limit: int = None
    # Class Fields End

    # Class Methods Begin
    def getLimit(self) -> int:

        return self.__limit

    def __init__(self, message: str, limit: int) -> None:

        super().__init__(message, None)
        self.limit = limit

    # Class Methods End
