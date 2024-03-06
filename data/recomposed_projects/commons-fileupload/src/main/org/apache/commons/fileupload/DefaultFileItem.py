# Imports Begin
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *
import os
import typing
from typing import *
import pathlib

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class DefaultFileItem(DiskFileItem):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self,
        fieldName: str,
        contentType: str,
        isFormField: bool,
        fileName: str,
        sizeThreshold: int,
        repository: pathlib.Path,
    ) -> None:

        super().__init__(
            fieldName, contentType, isFormField, fileName, sizeThreshold, repository
        )

    # Class Methods End
