from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItem import *


class FileItemFactory(ABC):

    def createItem(
        self, fieldName: str, contentType: str, isFormField: bool, fileName: str
    ) -> FileItem:
        return FileItem(fieldName, contentType, isFormField, fileName)
