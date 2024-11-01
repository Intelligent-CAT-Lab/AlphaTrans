import pytest

# Imports Begin
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *
import os
import typing
from typing import *
import pathlib

# Imports End


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
