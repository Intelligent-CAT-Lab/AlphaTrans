from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadBase import *
from src.main.org.apache.commons.fileupload.FileItemFactory import *
import io

# Imports End


class FileUpload(FileUploadBase):

    # Class Fields Begin
    __fileItemFactory: FileItemFactory = None
    # Class Fields End

    # Class Methods Begin
    def setFileItemFactory(self, factory: FileItemFactory) -> None:
        pass

    def getFileItemFactory(self) -> FileItemFactory:
        pass

    def __init__(self, constructorId: int, fileItemFactory: FileItemFactory) -> None:
        pass

    # Class Methods End
