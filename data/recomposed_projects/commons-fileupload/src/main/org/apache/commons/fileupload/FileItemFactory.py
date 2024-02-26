# Imports Begin
from src.main.org.apache.commons.fileupload.FileItem import *
import typing
from typing import *
from abc import ABC

# Imports End


class FileItemFactory(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def createItem(
        self, fieldName: str, contentType: str, isFormField: bool, fileName: str
    ) -> FileItem:

        return FileItem(fieldName, contentType, isFormField, fileName)

    # Class Methods End
