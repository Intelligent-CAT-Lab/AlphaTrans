from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *


class FileUploadException(Exception):

    __cause: BaseException = None

    __serialVersionUID: int = 8881893724388807504

    def getCause(self) -> BaseException:
        return self.__cause

    def printStackTrace1(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:

        super().print_stack(file=writer)
        if self.__cause is not None:
            writer.write("Caused by:\n")
            self.__cause.print_stack(file=writer)

    def printStackTrace0(self, stream: typing.IO) -> None:

        import traceback

        traceback.print_exc(file=stream)

        if self.__cause is not None:
            stream.write("Caused by:\n")
            traceback.print_exception(
                type(self.__cause),
                self.__cause,
                self.__cause.__traceback__,
                chain=False,
                file=stream,
            )

    def __init__(self, msg: str, cause: BaseException) -> None:
        super().__init__(msg)
        self.__cause = cause

    @staticmethod
    def FileUploadException1(msg: str) -> FileUploadException:
        return FileUploadException(msg, None)

    @staticmethod
    def FileUploadException0() -> FileUploadException:
        return FileUploadException(None, None)
