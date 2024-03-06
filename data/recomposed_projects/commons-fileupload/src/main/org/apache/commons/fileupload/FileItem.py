# Imports Begin
from src.main.org.apache.commons.fileupload.FileItemHeadersSupport import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class FileItem(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getOutputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:

        try:
            return self.get_output_stream()
        except IOException as e:
            raise e

    def setFormField(self, state: bool) -> None:

        self.formField = state

    def isFormField(self) -> bool:

        return True

    def setFieldName(self, name: str) -> None:

        self.field_name = name

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
        except UnsupportedEncodingException as e:
            raise ValueError(f"Unsupported encoding: {encoding}") from e

    def get(self) -> typing.List[int]:

        return self._data

    def getSize(self) -> int:

        return self.size

    def isInMemory(self) -> bool:

        return True

    def getName(self) -> str:

        return self.name

    def getContentType(self) -> str:

        return "text/plain"

    def getInputStream(
        self,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:

        try:
            return io.BytesIO(self.getBytes())
        except IOException as e:
            raise e

    # Class Methods End
