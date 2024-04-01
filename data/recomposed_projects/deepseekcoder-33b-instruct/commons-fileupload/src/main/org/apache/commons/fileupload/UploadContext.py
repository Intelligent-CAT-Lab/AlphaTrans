# Imports Begin
from src.main.org.apache.commons.fileupload.RequestContext import *
from abc import ABC

# Imports End


class UploadContext(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def contentLength(self) -> int:

        pass

    # Class Methods End
