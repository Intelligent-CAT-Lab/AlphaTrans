from __future__ import annotations
import re
import io
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileUploadBase import *


class FileUpload(FileUploadBase):

    __fileItemFactory: FileItemFactory = None

    def setFileItemFactory(self, factory: FileItemFactory) -> None:
        self.__fileItemFactory = factory

    def getFileItemFactory(self) -> FileItemFactory:
        return self.__fileItemFactory

    def __init__(self, constructorId: int, fileItemFactory: FileItemFactory) -> None:
        super().__init__()
        if constructorId == 1:
            self.__fileItemFactory = fileItemFactory
