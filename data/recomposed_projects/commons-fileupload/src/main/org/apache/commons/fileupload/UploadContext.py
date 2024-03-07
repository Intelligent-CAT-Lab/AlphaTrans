# Imports Begin
from src.main.org.apache.commons.fileupload.RequestContext import *
from abc import ABC

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class UploadContext(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def contentLength(self) -> int:

        return self.contentLength()

    # Class Methods End
