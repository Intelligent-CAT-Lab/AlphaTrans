from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from io import StringIO

# Imports End


class FileUploadException(Exception):

    # Class Fields Begin
    __serialVersionUID: int = None
    __cause: BaseException = None
    # Class Fields End

    # Class Methods Begin
    def getCause(self) -> BaseException:
        pass

    def printStackTrace1(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:
        pass

    def printStackTrace0(self, stream: typing.IO) -> None:
        pass

    def __init__(self, msg: str, cause: BaseException) -> None:
        pass

    @staticmethod
    def FileUploadException1(msg: str) -> FileUploadException:
        pass

    @staticmethod
    def FileUploadException0() -> FileUploadException:
        pass

    # Class Methods End
