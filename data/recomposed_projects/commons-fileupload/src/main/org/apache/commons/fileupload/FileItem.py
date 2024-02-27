# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

# Imports End


class FileItem(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getOutputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:

        try:
            return self.getOutputStream()
        except IOException as e:
            raise e

    def setFormField(self, state: bool) -> None:

        self.formField = state

    def isFormField(self) -> bool:

        return self.isFormField()

    def setFieldName(self, name: str) -> None:

        self.fieldName = name

    def getFieldName(self) -> str:

        return self.fieldName

    def delete(self) -> None:

        pass

    def write(self, file: pathlib.Path) -> None:

        with open(file, "w") as f:
            f.write(self.data)

    def getString1(self) -> str:

        return ""

    def getString0(self, encoding: str) -> str:

        try:
            return self.getString(encoding)
        except UnsupportedEncodingException:
            raise ValueError(f"Unsupported encoding: {encoding}")

    def get(self) -> typing.List[int]:

        return self._data

    def getSize(self) -> int:

        return self.size

    def isInMemory(self) -> bool:

        return True

    def getName(self) -> str:

        return self.name

    def getContentType(self) -> str:

        return "text/html"

    def getInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:

        return io.BytesIO(self.getBytes())

    # Class Methods End
