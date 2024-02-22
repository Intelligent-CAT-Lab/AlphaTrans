# Imports Begin
from commons.fileupload.src.main.java.org.apache.commons.fileupload.FileUploadBase import (
    FileUploadBase,
)
from commons.fileupload.src.main.java.org.apache.commons.fileupload.FileItemFactory import (
    FileItemFactory,
)

# Imports End


class FileUpload(FileUploadBase):

    # Class Fields Begin
    __fileItemFactory: FileItemFactory = None
    # Class Fields End

    # Class Methods Begin
    def setFileItemFactory(self, factory: FileItemFactory) -> None:

        self.__fileItemFactory = factory

    def getFileItemFactory(self) -> FileItemFactory:

        return self.__fileItemFactory

    def __init__(self, constructorId: int, fileItemFactory: FileItemFactory) -> None:

        super().__init__()
        if constructorId == 1:
            self.__fileItemFactory = fileItemFactory

    # Class Methods End
