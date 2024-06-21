from __future__ import annotations
import re
from dataclasses import field
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItem import *


class FileItemFactory(ABC):

    def createItem(
        self, fieldName: str, contentType: str, isFormField: bool, fileName: str
    ) -> FileItem:

        # Here you need to create an instance of FileItem and return it.
        # The exact implementation depends on the FileItem class and its constructor.
        # For example, if FileItem has a constructor that takes four arguments, you can do:

        return FileItem(fieldName, contentType, isFormField, fileName)
