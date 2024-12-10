from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.disk.DiskFileItem import *


class DefaultFileItem(DiskFileItem):

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
