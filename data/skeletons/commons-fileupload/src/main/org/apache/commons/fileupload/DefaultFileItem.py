# Imports Begin
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *
import typing
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
        pass

    # Class Methods End
