from __future__ import annotations
import re
from abc import ABC
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *


class FileItem(ABC):

    def getOutputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:
        return io.BytesIO(self.get())

    def setFormField(self, state: bool) -> None:
        self.isFormField = state

    def isFormField(self) -> bool:
        return self.isFormField

    def setFieldName(self, name: str) -> None:
        self.fieldName = name

    def getFieldName(self) -> str:
        return self.name

    def delete(self) -> None:
        pass

    def write(self, file: pathlib.Path) -> None:
        with open(file, "wb") as f:
            f.write(self.get())

    def getString1(self) -> str:
        return self.getString("UTF-8")

    def getString0(self, encoding: str) -> str:
        return self.get().decode(encoding)

    def get(self) -> typing.List[int]:
        return self._data

    def getSize(self) -> int:
        return len(self.get())

    def isInMemory(self) -> bool:
        return self._inMemory

    def getName(self) -> str:
        return self.name

    def getContentType(self) -> str:
        return self.contentType

    def getInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        return io.BytesIO(self.get())
